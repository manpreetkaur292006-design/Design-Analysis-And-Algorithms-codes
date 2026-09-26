def complete_algorithm_performance_assessment(n, arr, target):
  
  # Recursive Factorial
  def rfact(x):
    if x<=1:
      return 1
    return x*rfact(x-1)

  # Iterative Factorial
  def ifact(x):
    result=1
    for i in range(1,x+1):
      result*=i
    return result

  # Recursive Fibonacci
  def rfib(x):
    if x<=0:
      return 0
    if x==1:
      return 1
    return rfib(x-1)+rfib(x-2)

  # Iterative Fibonacci
  def ifib(x):
    a,b=0,1
    for i in range(2,x+1):
      a,b=b,a+b
    return b

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
    left=0
    right=len(arr)-1
    comparisons=0
    while left<=right:
      mid=(left+right)//2
      comparisons+=1
      if arr[mid]==target:
        return mid,comparisons
      elif target<arr[mid]:
        right=mid-1
      else:
        left=mid+1
    return -1,comparisons

  # Bubble Sort
  def bubble(arr):
    a=arr.copy()
    comparisons=0
    swaps=0
    l=len(a)
    for i in range(l):
      swapped=False
      for j in range(l-1-i):
        comparisons+=1
        if a[j]>a[j+1]:
          a[j],a[j+1]=a[j+1],a[j]
          swaps+=1
          swapped=True
      if not swapped:
        break
    return a, comparisons,swaps

  # Insertion Sort
  def insertion(arr):
    a=arr.copy()
    comparisons=0
    shifts=0
    l=len(a)
    for i in range(1,l):
      key=a[i]
      j=i-1
      while j>=0:
        comparisons+=1
        if a[j]>key:
          a[j+1]=a[j]
          shifts+=1
          j-=1
        else:
          break 
      a[j+1]=key
    return a, comparisons, shifts

  # Function Calling Statements 
  rec_fact=rfact(n)
  it_fact=ifact(n)
  rec_fib=rfib(n)
  it_fib=ifib(n)

  bub_s,bub_comp,bub_swap=bubble(arr)
  ins_s,ins_comp,ins_shift=insertion(arr)

  l_idx,l_comp=linear(arr,target)
  b_idx,b_comp=binary(bub_s,target)

    # Best Searching
  if l_comp<b_comp:
    best_s="Linear Search"
  elif b_comp<l_comp:
    best_s="Binary Search"
  else:
    best_s="Both Equal"

    # Best Sorting
  if bub_comp<ins_comp:
    best_sort="Bubble Sort"
  elif bub_comp>ins_comp:
    best_sort="Insertion Sort"
  else:
    best_sort="Both Equal"

    # Output
  output=["Algorithm Performance Assessment",
  "Computation Results",
  f"Factorial Recursive: {rec_fact}",
  f"Factorial Iterative: {it_fact}",
  f"Fibonacci Recursive: {rec_fib}",
  f"Fibonacci Iterative: {it_fib}",
  "Search Results",
  f"Linear Index: {l_idx}",
  f"Linear Comparisons: {l_comp}",
  f"Binary Index: {b_idx}",
  f"Binary Comparisons: {b_comp}",
  f"Search Best: {best_s}",
  "Sorting Results",
  f"Bubble Sorted: {' '.join(map(str,bub_s))}",
  f"Bubble Comparisons: {bub_comp}",
  f"Bubble Swaps: {bub_swap}",
  f"Insertion Sorted: {' '.join(map(str,ins_s))}",
  f"Insertion Comparisons: {ins_comp}",
  f"Insertion Shifts: {ins_shift}",
  f"Sorting Best: {best_sort}",
  "Complexity Summary",
  "Factorial: O(n)",
  "Fibonacci Recursive: O(2^n)",
  "Linear Search: O(n)",
  "Binary Search: O(log n)",
  "Bubble Sort: O(n^2)",
  "Insertion Sort: O(n^2)"]

  return output


# function calling
n = 5
arr = [5, 2, 8, 1, 3]
target = 3

result = complete_algorithm_performance_assessment(n, arr, target)

for line in result:
    print(line)