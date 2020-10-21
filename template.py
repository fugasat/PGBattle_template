def get_answer(input_list):
    return None


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

