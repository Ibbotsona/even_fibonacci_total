even_fibonacci_nums = []
target_figure = 4000000


# Function to generate fibonacci sequence based on the amount of terms
# specified as an arguement

# def generate_fibonacci_sequence(num_of_terms):
#     for num in range(2, num_of_terms):
#         fibonacci_nums.append(fibonacci_nums[num-1] + fibonacci_nums[num-2])
#     return fibonacci_nums


# Function to create a list of even numbers that
# are less than 4 million from the fibonacci sequence


def even_fibonacci_num_list(fibonacci_sequence):
    for num in fibonacci_sequence:
        if num > target_figure:
            break
        elif num % 2 == 0:
            even_fibonacci_nums.append(num)

    return even_fibonacci_nums


# Function to total the list of a sequence of numbers

# def fibonacci_sequence_total(num_list):
#     total_nums = sum(num_list)
#     return total_nums


# print(fibonacci_sequence_total(
#     even_fibonacci_num_list(
#         generate_fibonacci_sequence(60))))


# print("Total even fibonacci numbers up to 4 million is: {} ".format(
# fibonacci_sequence_total()))

# moved code into functions in order to appropriate an effective level
# of abstraction
