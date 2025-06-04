"""Example script demonstrating json_validator usage."""

from json_validator import check_json


def main():
    example = '{"key": 1}'
    valid, message = check_json(example)
    print(message)


if __name__ == "__main__":
    main()
