def get_max(spisok):
    if not spisok:
        return None
    max, *rest = spisok
    for el in rest:
        if el > max:
            max = el
    return max


print(get_max([]))  # => None
print(get_max([3, 2, -10, 38, 0]))  #=> 38
