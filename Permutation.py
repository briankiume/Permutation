def soln(a):
    a.sort()
    index = 0
    for i in range(1, (len(a) + 1)):
        if a[i - 1] == i:
            index += 1
    if index != len(a):
        val = 0
    else:
        val = 1

    return val


print(soln([4, 1, 3, 2]))
print(soln([4, 1, 3]))
