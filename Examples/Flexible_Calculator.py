def flex_stats(*args, round_to=None, unique=False):

    numbers = list(args)

    for i, num in enumerate(numbers):

        if isinstance(num, bool):
            raise TypeError(f"Argument {i+1} cannot be bool: {num}")

        elif isinstance(num, int):
            pass

        elif isinstance(num, float):
            pass

        else:
            raise TypeError(f"Argument {i+1} is not a number: {num}")

    if len(numbers) == 0:
        raise ValueError("You must enter at least one number")

    if unique:
        numbers = list(set(numbers))

    total = sum(numbers)
    count = len(numbers)
    average = total / count
    minimum = min(numbers)
    maximum = max(numbers)

    if round_to is not None and isinstance(round_to, int):
        total = round(total, round_to)
        average = round(average, round_to)

    return {
        "count": count,
        "sum": total,
        "mean": average,
        "min": minimum,
        "max": maximum,
    }


def combine(*args, op="sum"):

    if len(args) == 0:
        raise ValueError("You must enter at least one number.")

    numbers = []

    for i, x in enumerate(args):
        try:
            numbers.append(float(x))

        except:
            raise TypeError(f"Could not convert to float: {x}")

    op = op.lower().strip()

    if op == "sum":
        result = sum(numbers)

    elif op == "mul":
        result = 1
        for num in numbers:
            result = result * num

    elif op == "max":
        result = max(numbers)

    elif op == "min":
        result = min(numbers)

    else:
        raise ValueError(f"Unknown operation: {op}")

    return result


def pow_op(a, b, **kwargs):
    try:
        a = int(a)
        b = int(b)

    except:
        raise TypeError("a and b must be integers")

    mod = kwargs.get("mod", None)

    if mod is None:
        return pow(a, b)

    else:
        mod = int(mod)
        if mod == 0:
            raise ValueError("mod cannot be 0")

        return pow(a, b, mod)


def dispatch(command, *args, **kwargs):

    command = command.lower().strip()

    if command == "stats":
        return flex_stats(*args, **kwargs)
    elif command == "combine":
        return combine(*args, **kwargs)
    elif command == "pow":
        return pow_op(*args, **kwargs)
    else:
        raise ValueError(f"Unknown command: {command}")


def format_line(*args, **kwargs):

    sep = kwargs.get("sep", ", ")
    prefix = kwargs.get("prefix", "")
    suffix = kwargs.get("suffix", "")

    text = sep.join(str(x) for x in args)

    return prefix + text + suffix


if __name__ == "__main__":

    print("1) flex_stats(1, 2, 2, 4, round_to=2, unique=True)")
    result = flex_stats(1, 2, 2, 4, round_to=2, unique=True)
    print(f"result: {result}\n")

    print("2) combine(2, 3, 4, op='mul')")
    result = combine(2, 3, 4, op="mul")
    print(f"result: {result}\n")

    print("3) pow_op(2, 10, mod=1000)")
    result = pow_op(2, 10, mod=1000)
    print(f"result: {result}\n")

    print("4) dispatch('stats', 5, 5, 7, round_to=1)")
    result = dispatch("stats", 5, 5, 7, round_to=1)
    print(f"result: {result}\n")

    print("5) format_line('a', 'b', 'c', sep=' - ', prefix='[', suffix=']')")
    result = format_line("a", "b", "c", sep=" - ", prefix="[", suffix="]")
    print(f"result: {result}\n")
