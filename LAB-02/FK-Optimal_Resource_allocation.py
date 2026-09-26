def fractional_knapsack_allocation(items, capacity):

    def sort_item(item):
        ratio = item[1] / item[2]
        return (-ratio, item[0])

    items.sort(key=sort_item)

    result = []
    total_profit = 0.0
    total_weight = 0.0
    remaining = float(capacity)

    def to_two_decimals(x):
        s = int(round(x * 100))
        integer_part = s // 100
        decimal_part = s % 100

        if decimal_part < 10:
            decimal_str = "0" + str(decimal_part)
        else:
            decimal_str = str(decimal_part)

        return str(integer_part) + "." + decimal_str

    result.append("Fractional Knapsack Report")
    result.append("Selected Items")
    result.append("Item Value Weight Fraction Profit")

    for item in items:
        item_id = item[0]
        value = item[1]
        weight = item[2]

        if remaining <= 0.000000001:
            break

        if weight <= remaining:
            fraction = 1.0
            profit = float(value)
            used_weight = float(weight)
        else:
            fraction = remaining / weight
            profit = value * fraction
            used_weight = remaining

        result.append(
            str(item_id) + " " +
            to_two_decimals(value) + " " +
            to_two_decimals(weight) + " " +
            to_two_decimals(fraction) + " " +
            to_two_decimals(profit)
        )

        total_profit = total_profit + profit
        total_weight = total_weight + used_weight
        remaining = remaining - used_weight

    result.append("Maximum Profit: " + to_two_decimals(total_profit))
    result.append("Total Weight Used: " + to_two_decimals(total_weight))
    result.append("Selection Strategy: Highest value-to-weight ratio first")

    return result

# function calling
items = [
    ("A", 60, 10),
    ("B", 100, 20),
    ("C", 120, 30)
]

capacity = 50

result = fractional_knapsack_allocation(items, capacity)

for line in result:
    print(line)