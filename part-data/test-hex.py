import base64
import binascii


if __name__ == "__main__":
    s = b'hello world!'
    # 2进制转换成16进制
    h = binascii.b2a_hex(s)
    print(h)
    # 16进制转换成2进制
    print(binascii.a2b_hex(h))
    h1 = base64.b16encode(s)
    print(h1)
    print(base64.b16decode(h1))