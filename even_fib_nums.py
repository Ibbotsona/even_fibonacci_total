def even_fibonacci_num_list(fibonacci_sequence):
    even_fibonacci_nums = []
    target_figure = 4000000
    for num in fibonacci_sequence:
        if num > target_figure:
            break
        elif num % 2 == 0:
            even_fibonacci_nums.append(num)

    return even_fibonacci_nums
