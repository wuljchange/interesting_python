import io


if __name__ == "__main__":
    s = io.StringIO()
    s_byte = io.BytesIO()
    print('test', file=s, end="\t")
    s_byte.write(b'bytes')
    print("new")
    print(s.getvalue())
    print(s_byte.getvalue())
