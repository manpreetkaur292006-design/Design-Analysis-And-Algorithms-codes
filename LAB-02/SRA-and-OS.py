def job_sequencing_deadlines(jobs):
    jobs.sort(key=lambda x: (-x[2], x[1], x[0]))

    max_deadline = max(job[1] for job in jobs)
    slots = [None] * (max_deadline + 1)

    for job_id, deadline, profit in jobs:
        for slot in range(deadline, 0, -1):
            if slots[slot] is None:
                slots[slot] = (job_id, profit)
                break

    result = []
    total_profit = 0
    count = 0

    result.append("Job Sequencing Report")
    result.append("Scheduled Jobs")
    result.append("Slot Job Profit")

    for slot in range(1, max_deadline + 1):
        if slots[slot] is not None:
            job_id, profit = slots[slot]
            result.append(f"{slot} {job_id} {profit}")
            total_profit += profit
            count += 1

    result.append(f"Total Jobs Scheduled: {count}")
    result.append(f"Total Profit: {total_profit}")
    result.append("Strategy: Schedule highest profit jobs before their deadlines")

    return result

n = int(input())

jobs = []
for _ in range(n):
    job_id, deadline, profit = input().split()
    jobs.append((job_id, int(deadline), int(profit)))

result = job_sequencing_deadlines(jobs)

for line in result:
    print(line)


# sample input

# 5
# J1 2 100
# J2 1 19
# J3 2 27
# J4 1 25
# J5 3 15