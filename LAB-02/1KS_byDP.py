def knapsack_comparison(items, capacity):
    n = len(items)

   
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        item_id, value, weight = items[i - 1]

        for w in range(capacity + 1):
            if weight <= w:
                dp[i][w] = max(
                    dp[i - 1][w],
                    dp[i - 1][w - weight] + value
                )
            else:
                dp[i][w] = dp[i - 1][w]

    
    selected_01 = []
    w = capacity

    for i in range(n, 0, -1):
        item_id, value, weight = items[i - 1]

        if dp[i][w] != dp[i - 1][w]:
            selected_01.append(items[i - 1])
            w -= weight

   
    selected_01.reverse()

    total_value_01 = sum(item[1] for item in selected_01)
    total_weight_01 = sum(item[2] for item in selected_01)

    
  
    sorted_items = sorted(
        items,
        key=lambda x: (-x[1] / x[2], x[0])
    )

    selected_fractional = []
    remaining = capacity
    total_profit = 0.0
    total_weight_fractional = 0.0

    for item_id, value, weight in sorted_items:
        if remaining <= 0:
            break

        if weight <= remaining:
            fraction = 1.0
            used_weight = weight
        else:
            fraction = remaining / weight
            used_weight = remaining

        profit = value * fraction

        selected_fractional.append(
            (item_id, value, weight, fraction, profit)
        )

        total_profit += profit
        total_weight_fractional += used_weight
        remaining -= used_weight

    
    difference = abs(total_profit - total_value_01)

    if total_profit > total_value_01:
        better_result = "Fractional Knapsack"
    elif total_value_01 > total_profit:
        better_result = "0/1 Knapsack"
    else:
        better_result = "Both Equal"

   
    result = []

    result.append("Knapsack Comparison Report")

    result.append("0/1 Knapsack")
    result.append("Selected Items")
    result.append("Item Value Weight")

    for item_id, value, weight in selected_01:
        result.append(f"{item_id} {value} {weight}")

    result.append(f"Maximum Value: {total_value_01}")
    result.append(f"Total Weight: {total_weight_01}")

    result.append("Fractional Knapsack")
    result.append("Selected Items")
    result.append("Item Value Weight Fraction Profit")

    for item_id, value, weight, fraction, profit in selected_fractional:
        result.append(
            f"{item_id} {value:.2f} {weight:.2f} "
            f"{fraction:.2f} {profit:.2f}"
        )

    result.append(f"Maximum Profit: {total_profit:.2f}")
    result.append(f"Total Weight: {total_weight_fractional:.2f}")

    result.append("Comparison")
    result.append(f"Difference: {difference:.2f}")
    result.append(f"Better Result: {better_result}")
    result.append(
        "Justification: Fractional Knapsack can take item fractions, "
        "while 0/1 Knapsack selects complete items only"
    )

    return result

items = [
    ("A", 20, 2),
    ("B", 30, 5),
    ("C", 35, 7),
    ("D", 12, 3)
]

capacity = 7

result = knapsack_comparison(items, capacity)

for line in result:
    print(line)

# sample input

# 4 7
# A 20 2
# B 30 5
# C 35 7
# D 12 3