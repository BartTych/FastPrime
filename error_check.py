import sys


def check_for_input_errors(N,start,size, type_of_action):

    if type_of_action not in [0, 1, 2]:
        print(f"no such action def {type_of_action}")
        sys.exit()

    if N < 1:
        print("N is smaller that 1")
        sys.exit()

    if start < N :
        print("start can`t be smaller that N")
        sys.exit()

    if size < 1:
        print("size can`t be smaller that 1")
        sys.exit()

    if not isinstance(N, int):
        print("N needes to be int")
        sys.exit()

    if not isinstance(start, int):
        print("start needes to be int")
        sys.exit()

    if not isinstance(size, int):
        print("size needes to be int")
        sys.exit()