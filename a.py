def get_answer(input_list):
    c_list = [int(v) for v in input_list[0].split(" ")]
    w = c_list[0]
    k = c_list[1]
    d = c_list[2]

    if k > d or (w - k) > d:
        return "No"
    return "Yes"


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

