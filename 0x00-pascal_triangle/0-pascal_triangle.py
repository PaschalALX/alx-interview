from math import ceil


def pascal_triangle(n):
    if n <= 0:
        return []

    main_list = []

    for x in range(n):
        sub_list = list(range(x + 1))
        sub_list[0] = 1
        sub_list[x] = 1

        curr_n = x + 1
        idx_stop = ceil(curr_n / 2) - 1

        if curr_n >= 3:
            ini_sub_list = main_list[x - 1]
            isl_len = len(ini_sub_list)

            for idx, y in enumerate(ini_sub_list):
                if idx >= 1:
                    sub_list[idx] = y + ini_sub_list[idx - 1]
                    sub_list[isl_len - idx] = y + ini_sub_list[idx - 1]
                if idx == idx_stop:
                    break

        main_list.append(sub_list)

    return main_list
