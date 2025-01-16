def function_with_uncommon_bug(x):
    if x == 0:
        return 0  # This line is problematic
    else:
        return 1 / x