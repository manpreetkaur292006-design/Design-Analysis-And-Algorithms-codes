from math import floor,log2
def generate_execution_observation_table(sizes):
    # your code goes here
    def rfib(n):
      if n<=1:
        return 1
      return 1+rfib(n-1)+rfib(n-2)
    output = [
        "Algorithm Execution Observation Table",
        "InputSize RecursiveFactorial IterativeFactorial RecursiveFibonacci IterativeFibonacci LinearSearch BinarySearch BubbleSort InsertionSort"
    ]

    for n in sizes:
      rfact=n+1
      ifact=n
      rfibc=rfib(n)
      ifib=n
      lsearch=n
      bsearch=floor(log2(n))+1
      bubble=n*(n-1)//2
      insertion=n*(n-1)//2

      row=f"{n} {rfact} {ifact} {rfibc} {ifib} {lsearch} {bsearch} {bubble} {insertion}"

      output.append(row)
      
    return output