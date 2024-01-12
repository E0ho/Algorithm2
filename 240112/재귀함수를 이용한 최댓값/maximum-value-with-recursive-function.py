n = int(input())

li = list(map(int, input().split()))
val = n - 1

def max_val(val):
    if val == 0:
        return li[val]

    return max(max_val(val-1), li[val])


result = max_val(val)
print(result)