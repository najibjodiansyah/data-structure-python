def bin_search(lists, x):
    low, high = 0, len(lists)-1
    while low <= high:
        mid = (low + high)//2
        if lists[mid] == x:
            return mid
        elif lists[mid] > x:
            high = mid - 1
        else:
            low = mid + 1
    return -1

sequence = [11,22,33,44,55,66,77]
x = int(input("angka yang di cari: "))

if bin_search(sequence, x) != -1:
    print(f"ada nih {x} dalem sequence")
else: 
    print(f"tetot")

