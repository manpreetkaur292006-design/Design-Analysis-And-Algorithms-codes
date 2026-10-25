def generate_optimization_reflection_report(scenarios):
    output = []
    output.append("Optimization Technique Reflection Report")
    output.append("Technique Comparison")
    output.append("Technique BestUsedFor Limitation Example")
    output.append("Divide-and-Conquer Large independent subproblems Extra merging or partition overhead Merge Sort and Quick Sort")
    output.append("Greedy Locally optimal choices May not always give global optimum Activity Selection and Fractional Knapsack")
    output.append("Dynamic Programming Overlapping subproblems Requires more memory 0/1 Knapsack and LCS")
    output.append("Scenario Recommendations")
    output.append("Scenario Technique Reason")
    
    rules = {
        "TASK_SORTING": ("Divide-and-Conquer", "Problem can be divided and combined"),
        "MEETING_SCHEDULE": ("Greedy", "Earliest finish time maximizes compatible activities"),
        "RESOURCE_FRACTION": ("Greedy", "Highest ratio choice gives optimal fractional result"),
        "JOB_PROFIT": ("Greedy", "Highest profit job is placed before deadline"),
        "ZERO_ONE_KNAPSACK": ("Dynamic Programming", "Complete item choices require optimal subproblem table"),
        "SEQUENCE_MATCHING": ("Dynamic Programming", "Overlapping subsequences are reused")
    }
    
    for sc in scenarios:
        if sc in rules:
            tech, reason = rules[sc]
            output.append(f"{sc} {tech} {reason}")
            
    output.append("Summary")
    output.append("Most Reliable for Exact Optimization: Dynamic Programming")
    output.append("Fastest for Simple Scheduling Decisions: Greedy")
    output.append("Best for Sorting Large Data: Divide-and-Conquer")
    output.append("Conclusion: Algorithm choice depends on problem structure and constraints")
    
    return output


scenarios = [
    "TASK_SORTING",
    "MEETING_SCHEDULE",
    "RESOURCE_FRACTION",
    "JOB_PROFIT",
    "ZERO_ONE_KNAPSACK",
    "SEQUENCE_MATCHING"
]

result = generate_optimization_reflection_report(scenarios)

for line in result:
    print(line)