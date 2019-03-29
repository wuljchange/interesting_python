import arrow


bracket_dct = {'(': ')', '{': '}', '[': ']', '<': '>'}


def bracket(arg: str):
    match_stack = []
    for char in arg:
        if char in bracket_dct.keys():
            match_stack.append(char)
        elif char in bracket_dct.values():
            if len(match_stack) > 0 and bracket_dct[match_stack.pop()] == char:
                continue
            else:
                return False
        else:
            continue
    return True


if __name__ == "__main__":
    test = '(12121){}dasda[oio{dad}232<asfsd>232]'
    print(arrow.now().format('YYYY-MM-DD HH:MM:SS'))
    print(bracket(test))
