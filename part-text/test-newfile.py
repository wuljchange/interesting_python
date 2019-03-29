import array


if __name__ == "__main__":
    # xt模式测试写入文件不能直接覆盖，只能写入到不存在的文件里面
    with open('test.file', 'xt') as f:
        f.write('test not exist')
    print("end", end='#')