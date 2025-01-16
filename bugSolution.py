def function_with_uncommon_bug_fixed(x):
    if x == 0:
        raise ZeroDivisionError("Division by zero")
    else:
        return 1 / x