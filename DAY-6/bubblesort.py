# Bubble sort in Python
def bubble_sort(arr, n=None):
    if n is None:
        n = len(arr)
    if n == 1:
        return
    for i in range(n - 1):
        if arr[i] > arr[i + 1]:
            arr[i], arr[i + 1] = arr[i + 1], arr[i]
    bubble_sort(arr, n - 1)
if __name__ == "__main__":
    input_str = input("Enter a list of he number: ")
    arr = [int(x) for x in input_str.split()]
    bubble_sort(arr)
    print("Sorted array is:", arr)