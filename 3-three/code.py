N     = int(input().strip())
array = list(map(int, input().strip().split()))

def seperateEvenAndOdd(arr):
    even_numbers = [[],[]]

    for i in arr:
        even_numbers[i%2].append(i)
    
    return even_numbers[0] + even_numbers[1]

print(seperateEvenAndOdd(array))
