import json


def check_json(text: str):
    """Check whether the provided string is valid JSON.

    Returns a tuple (is_valid, message). If the JSON is valid,
    is_valid is True and message contains a success message.
    Otherwise, is_valid is False and message contains details
    about the problem.
    """
    try:
        json.loads(text)
        return True, "JSON корректен."
    except json.JSONDecodeError as exc:
        return False, f"Ошибка: {exc.msg} (позиция {exc.pos})."


if __name__ == "__main__":
    import sys

    if len(sys.argv) != 2:
        print("Usage: python json_validator.py '<json_string>'")
    else:
        valid, msg = check_json(sys.argv[1])
        print(msg)
