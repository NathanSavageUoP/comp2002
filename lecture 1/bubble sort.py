def bubble_sort(src):
    for X in range(0, len(src) - 1):
        if src[X] > src[X + 1]:
            src[X], src[X + 1] = src[X + 1], src[X]

    ordered = True
    for i, X in enumerate(src):
        if X < src[max(i - 1, 0)]:
            ordered = False
            break
    if ordered:
        return src
    else:
        return bubble_sort(src)

print(bubble_sort([10, 16, 4, 32, 9, 9, -4]))