from decimal import Decimal, localcontext


def main(a, b):
    a = Decimal(a)
    b = Decimal(b)
    return a+b


if __name__ == "__main__":
    sum = main('3.2', '4.3')
    # 使用上下文管理器更改输出的配置信息
    with localcontext() as ctx:
        ctx.prec = 3
        print(Decimal('3.2')/Decimal('2.3'))
    print(sum == 7.5)
