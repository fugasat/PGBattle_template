def get_answer(input_list):
    c_list = [int(v) for v in input_list[0].split(" ")]

    n = c_list[0]
    m = c_list[1]
    p = [1] * m
    pt = [0] * n

    s = 0
    for i in range(n):
        pp = input_list[1 + i].split(" ")
        pt = int(pp[0]) + int(pp[1])
        pi = i - pt
        if pi >= 0 and pi < m and p[pi]:
            p[pi] = 0
            s += 1

    return s



if __name__ == "__main__":
    input_list = []
    while True:
        try:
            input1 = input()
            if not input1:
                break
            if len(input1) == 0:
                break
            input_list.append(input1)
        except EOFError:
            break
    print(get_answer(input_list))

