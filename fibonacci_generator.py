def generate_fibonacci_sequence(num_of_terms):
    fibonacci_nums = [1, 2]

    for num in range(2, num_of_terms):
        fibonacci_nums.append(fibonacci_nums[num - 1] + fibonacci_nums[num - 2])
    return fibonacci_nums
