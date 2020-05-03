def partition(arr, low, high):
    i = low-1
    pivot = arr[high][2]

    for j in range(low, high):
        if arr[j][2] <= pivot:
            i = i+1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i+1], arr[high] = arr[high], arr[i+1]
    return i+1 

def quick_sort(arr, low, high):
    if low < high:
        p = partition(arr,low,high)

        quick_sort(arr,low,p-1)
        quick_sort(arr,p+1,high)