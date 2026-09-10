def complete_algorithm_performance_assessment(n, arr, target):
    # Recursive Factorial
    def rfact(n):
      if n<=1:
        return 1
      return n*rfact(n-1)
    # Iterative Factorial
    def ifact(n):
      fact=1
      for i in range(1,n+1):
        fact*=i
      return fact
    # Recursive Fibonnacci
    def rfib(n):
      if n<=1:
        return n
      return rfib(n-1)+rfib(n-2)
    # Iterative Fibonnacci
    def ifib(n):
      a,b=0,1
      for i in range(n):
        a,b=b,a+b
      return a
    # Linear Search
    def linear(arr,target):
      comparisons=0
      for i in range(len(arr)):
        comparisons+=1
        if arr[i]==target:
          return i,comparisons
      return -1,comparisons
    # Binary Search
    def binary(arr,target):
      arr.sort()
      comparisons=0
      low=0
      high=len(arr)-1
      result_idx=-1
      while low<=high:
        mid=(low+high)//2
        comparisons+=1
        if arr[mid]==target:
          result_idx=mid
          high=low-1
        elif arr[mid]<target:
          low=mid+1
        else:
          high=mid-1
      return result_idx,comparisons
    # Bubble Sort
    def bubble(arr):
      comparisons=0
      swaps=0
      n=len(arr)
      for i in range(n):
        swapped=False
        for j in range(n-i-1):
          comparisons+=1
          if arr[j]>=arr[j+1]:
            arr[j],arr[j+1]=arr[j+1],arr[j]
            swaps+=1
            swapped=True
        if not swapped:
          break
      return arr,comparisons,swaps
    # Insertion Sort
    def insertion(arr):
      comparisons=0
      shifts=0
      n=len(arr)
      for i in range(n):
        key=arr[i]
        j=i-1
        while j>=0:
          comparisons+=1
          if arr[j]>key:
            arr[j+1]=arr[j]
            shifts+=1
            j-=1
          else:
            break
        arr[j+1]=key
      return arr,comparisons,shifts
    # Calling all the functions and storing the outputs
    rfa=rfact(n)
    ifa=ifact(n)
    rfb=rfib(n)
    ifb=ifib(n)
    ls_idx,ls_comp=linear(arr.copy(),target)
    bs_idx,bs_comp=binary(arr.copy(),target)
    bub=bubble(arr.copy())
    ins=insertion(arr.copy())
    # Checking which searhing method is best(linear,binary)
    if ls_comp>bs_comp:
      bests="Binary Search"
    elif ls_comp<bs_comp:
      bests="Linear Search"
    else:
      bests="Both Equal"
    # Checking the best sorting algorithm
    if bub[1]>ins[1]:
      besta="Insertion Sort"
    elif bub[1]<ins[1]:
      besta="Bubble Sort"
    else:
      besta="Both Equal"
    # Creating the output array
    output = [
      "Algorithm Performance Assessment",
      "Computation Results",
      f"Factorial Recursive: {rfa}",
      f"Factorial Iterative: {ifa}",
      f"Fibonacci Recursive: {rfb}",
      f"Fibonacci Iterative: {ifb}",
      "Search Results",
      f"Linear Index: {ls_idx}",
      f"Linear Comparisons: {ls_comp}",
      f"Binary Index: {bs_idx}",
      f"Binary Comparisons: {bs_comp}",
      f"Search Best: {bests}",
      "Sorting Results",
      f"Bubble Sorted: {" ".join(map(str,bub[0]))}",
      f"Bubble Comparisons: {bub[1]}",
      f"Bubble Swaps: {bub[2]}",
      f"Insertion Sorted: {" ".join(map(str,(ins[0])))}",
      f"Insertion Comparisons: {ins[1]}",
      f"Insertion Shifts: {ins[2]}",
      f"Sorting Best: {besta}",
      "Complexity Summary",
      "Factorial: O(n)",
      "Fibonacci Recursive: O(2^n)",
      "Linaer Search: O(n)",
      "Binary Search: O(log n)",
      "Bubble Sort: O(n^2)",
      "Insertion Sort: O(n^2)"
    ]
    return output

# function calling statements
n=5
arr=[23,12,54,14,77]
target=14
print("\n".join(complete_algorithm_performance_assessment(n, arr, target)))