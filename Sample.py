# Removing duplicates from a list without using a new list
def remove_duplicates(lst):
    seen = set()
    i = 0
    while i < len(lst):
        if lst[i] in seen:
            lst.pop(i)
        else:
            seen.add(lst[i])
            i += 1


# Example usage
my_list = [1, 2, 3, 2, 1, 4, 5, 3]
remove_duplicates(my_list)
print(my_list)


