# The below function doesn't work correctly. It should sum all the numbers at the
# current time. For example, 01:02:03 should return 6. Improve and fix the function,
# and write unit test(s) for it. Use any testing framework you're familiar with.


# [TODO]: fix the function
def sum_current_time(time_str: str) -> int:
    """Expects data in the format HH:MM:SS"""
    list_of_nums = list(time_str.replace(":",""))
    list_of_nums = list(map(lambda x: int(x), list_of_nums))
    return sum(list_of_nums)


if __name__ == "__main__":
    print(sum_current_time('01:02:03'))