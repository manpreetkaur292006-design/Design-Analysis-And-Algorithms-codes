def analyze_recursive_iterative(n):
    # your code goes here
  
  # Factorial by iterative approach
  def fact(n):
    fact=1
    if n==0:
      return 1
    for i in range(1,n+1):
      fact*=i
    return fact

  # Factorial by recurssion
  def rfact(n):
    if n==0:
      return 1
    return n*rfact(n-1)

  # Fibonnacci by iteration 
  def fib(n):
    a,b=0,1
    for i in range(n):
      a,b=b,a+b
    return a

  # Fibonnacci by recurssion
  fib_count=0
  def rfib(n):
    nonlocal fib_count
    fib_count+=1
    if n<=1:
      return n
    return rfib(n-1)+rfib(n-2)

  # Calling the functions
  rfact_ans=rfact(n)
  fact_ans=fact(n)
  rfib_ans=rfib(n)
  fib_ans=fib(n)

  # Matching the output results
  result = [
        "Computation Analysis Report",
        f"Recursive Factorial: {rfact_ans}",
        f"Iterative Factorial: {fact_ans}",
        f"Recursive Fibonacci: {rfib_ans}",
        f"Iterative Fibonacci: {fib_ans}",
        "Operation Count Comparison",
        f"Recursive Factorial Count: {n + 1}",
        f"Iterative Factorial Count: {n}",
        f"Recursive Fibonacci Count: {fib_count}",
        f"Iterative Fibonacci Count: {n}",
    ]

  return result

# n=int(input())
# analyze_recursive_iterative(n)