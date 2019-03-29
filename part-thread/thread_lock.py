import threading
from socket import socket, AF_INET, SOCK_STREAM
from functools import partial
from contextlib import contextmanager


# State to stored info on locks already acquired
_local = threading.local()


@contextmanager
def acquire(*locks):
    locks = sorted(locks, key=lambda x: id(x))

    acquired = getattr(_local, 'acquire', [])
    if acquired and max(id(lock) for lock in acquired) >= id(locks[0]):
        raise RuntimeError('Lock order violation')

    acquired.extends(locks)
    _local.acquired = acquired

    try:
        for lock in locks:
            lock.acquire()
        yield
    finally:
        for lock in reversed(locks):
            lock.release()
        del acquired[-len(locks):]


class LazyConnection:
    def __init__(self, address, family=AF_INET, socket_type=SOCK_STREAM):
        self.address = address
        self.family = family
        self.socket_type = socket_type
        self.local = threading.local()

    def __enter__(self):
        if hasattr(self.local, 'sock'):
            raise RuntimeError('connection existed')
        self.local.sock = socket(self.family, self.socket_type)
        self.local.sock.connect(self.address)
        return self.local.sock

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.local.sock.close()
        del self.local.sock


def test(conn):
    with conn as c:
        c.send(b'test\n')
        resp = b''.join(iter(partial(c.recv, 8192), b''))
        print(len(resp))


if __name__ == "__main__":
    conn = LazyConnection(("www.test.com", 8081))
    t1 = threading.Thread(target=test, args=(conn,))
    t2 = threading.Thread(target=test, args=(conn,))
    t1.start()
    t2.start()
    t1.join()
    t2.join()
