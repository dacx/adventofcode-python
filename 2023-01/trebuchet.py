import regex


def solve():
    def parse_str_to_int(digit_str: str) -> int:
        mapping: dict = {
            "one": "1",
            "two": "2",
            "three": "3",
            "four": "4",
            "five": "5",
            "six": "6",
            "seven": "7",
            "eight": "8",
            "nine": "9",
            "zero": "0",
        }
        if digit_str in mapping:
            return int(mapping[digit_str])
        return int(digit_str)

    def calc_number_for_line(current_line: str) -> int:
        first = regex.search(
            r"\d|zero|one|two|three|four|five|six|seven|eight|nine", current_line
        )
        first = first.group(0)
        # use reverse because otherwise parts such as `twone`, which share the letter o would only match the first
        # occurrence and show 2, and not also 1.
        # python's builtin `re` module does not support reverse search, so we use the `regex` module instead.
        last = regex.search(
            r"(?r)\d|zero|one|two|three|four|five|six|seven|eight|nine", current_line
        )
        last = last.group(0)

        return parse_str_to_int(first) * 10 + parse_str_to_int(last)

    with open("input", "r") as f:
        line: str
        total: int = 0
        while line := f.readline().strip():
            total += calc_number_for_line(line)

        print(total)


if __name__ == "__main__":
    solve()
