def find_three(ls:list):
    target = 3
    options = []
    for item in ls:
        if item <= target:
            temp_opt = []
            for option in options:
                if sum(option) +item <= target and (*option, item,) not in options:
                    # print((*option, item,))
                    temp_opt.append((*option, item,))
            if 'temp_opt' in locals():
                options += temp_opt
            if (item,) not in options:
                options.append((item,))

    return [item for item in options if sum(item) == target]





sample = [1, 0, -1, 0, 3, 2]
print(find_three(sample))