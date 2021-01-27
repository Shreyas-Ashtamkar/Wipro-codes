N     = int(input().strip())
array = list(map(int, input().strip().split()))

def bubbleSort(arr):
    N = len(arr)
    for i in range(N):
        for j in range(0, N-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

print(bubbleSort(array))
