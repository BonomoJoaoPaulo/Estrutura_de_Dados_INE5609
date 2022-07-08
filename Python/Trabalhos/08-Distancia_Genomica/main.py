values_number = int(input())

values_list = [int(n) for n in input().split()]

def BubbleSort(v):
    swapped = True
    permutations = 0
    while swapped:
        swapped = False
        for i in range(1, values_number):
            if v[i - 1] > v[i]:
                v[i - 1], v[i] = v[i], v[i - 1]
                permutations += 1
                swapped = True

    return permutations

print(BubbleSort(values_list))
