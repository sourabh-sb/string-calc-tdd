def extract_delimiter_and_numbers(numbers: str) -> tuple:
    default_delimiter = ","
    if numbers.startswith("//"):
        parts = numbers[2:].split("\n", 1)
        return parts[0], parts[1]
    return default_delimiter, numbers.replace("\n", ",")


def parse_numbers(numbers: str, delimiter: str) -> list:
    return [int(num) for num in numbers.split(delimiter) if num]


def check_for_negatives(num_list: list) -> None:
    negative_numbers = [num for num in num_list if num < 0]
    if negative_numbers:
        raise ValueError(f"negative numbers not allowed: {','.join(map(str, negative_numbers))}")

def add(numbers: str) -> int:
    if not numbers:
        return 0

    delimiter, numbers = extract_delimiter_and_numbers(numbers)
    num_list = parse_numbers(numbers, delimiter)

    check_for_negatives(num_list)

    return sum(num_list)

