def replace_all_occurrences(first_string, second_string):
    while first_string in second_string:
        second_string = second_string.replace(first_string, "")
    return second_string


first_string = input()
second_string = input()
print(replace_all_occurrences(first_string, second_string))
