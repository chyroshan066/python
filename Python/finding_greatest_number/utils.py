def find_max(*lists):
    max = lists[0]
    for item in lists:
        if item > max:
            max = item
    return max