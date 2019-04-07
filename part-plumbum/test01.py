from plumbum import local, FG, BG
from plumbum.cmd import grep, awk, wc, head, cat, ls, tail, sudo, ifconfig


if __name__ == "__main__":
    ls = local["ls"]
    print(ls())
    # 环境在linux
    # 管道符 pipe
    command = ls["-a"] | awk['{if($2="100") print $2}'] | wc["-l"]
    print(command())
    # 重定向
    command = cat['test.file'] | head["-n", 5]
    print(command())
    # 后台运行和当前终端运行
    command = (cat['test.file'] | grep["-v", "test"] | (tail["-n", 5] > "out.file")) & FG
    print(command())
    command = (awk['-F', '\t', '{print $1, $2}', 'test.file'] | (head['-n', 5] >> 'out.file')) & BG
    print(command())
    # 嵌套命令
    command = sudo[ifconfig['-a']]
    command1 = (sudo[ifconfig["-a"]] | grep["-i", "loop"]) & FG
    print(command())
    print(command1())
