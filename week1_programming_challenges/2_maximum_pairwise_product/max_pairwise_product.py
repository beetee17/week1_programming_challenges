# python3


def max_pairwise_product(numbers):
    # The max product of an array of positive integers is simply the product of the 2 largest numbers in the array!
    n = len(numbers)
    high = numbers[0]
    prev_high = 0
    for i in range(1, n):
        if numbers[i] > high:
            prev_high = high
            high = numbers[i]
        elif numbers[i] > prev_high:
            prev_high = numbers[i]

    return high * prev_high


if __name__ == "__main__":
    input_n = int(input())
    input_numbers = [int(x) for x in input().split()]
    print(max_pairwise_product(input_numbers))
