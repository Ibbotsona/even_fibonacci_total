from even_fib_nums import *
from total_num_list import *
from fibonacci_generator import *


def main():
    num_of_terms = 35
    # fibonacci_sequence = generate_fibonacci_sequence(num_of_terms)
    # even_fibonacci_sequence = even_fibonacci_num_list(fibonacci_sequence)
    # total_of_even_nums = fibonacci_sequence_total(even_fibonacci_sequence)

    print(
        "Total of even numbers in fibonacci "
        "sequence up to 4 million is: {}".format(
            fibonacci_sequence_total(
                even_fibonacci_num_list(generate_fibonacci_sequence(num_of_terms))
            )
        )
    )


if __name__ == "__main__":
    main()
