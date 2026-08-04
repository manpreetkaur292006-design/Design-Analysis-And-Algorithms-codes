# Linear Search and Binary Search Computation

n = int(input("Enter n: "))
arr = list(map(int, input("Enter array: ").split()))
target = int(input("Enter target: "))

def compare_search_algorithm(arr,target):

    # Binary Search 
    def binary_search(arr,target):
        low=0
        high=len(arr)-1
        comparisons=0
        while low<=high:
            mid=(low+high)//2
            comparisons+=1
            if arr[mid]==target:
                return mid, comparisons
            elif arr[mid]<target:
                low=mid+1
            else:
                high=mid-1
        return -1, comparisons

    # Linear Search
    def linear_search(arr,target):
        comparisons=0
        for i in range(len(arr)):
            comparisons+=1
            if arr[i]==target:
                return i,comparisons
        return -1,comparisons

    lin_index, lin_comp = linear_search(arr, target)
    bin_index, bin_comp = binary_search(arr, target)

    print("Search Comparison Report")
    print(f"Linear Search Result: {lin_index}, Comparisons: {lin_comp}")
    print(f"Binary Search Result: {bin_index}, Comparisons: {bin_comp}")

    if lin_comp < bin_comp:
        print("Better Algorithm: Linear Search")
    elif bin_comp < lin_comp:
        print("Better Algorithm: Binary Search")
    else:
        print("Better Algorithm: Both Equal")

    return []

compare_search_algorithm(arr, target)
