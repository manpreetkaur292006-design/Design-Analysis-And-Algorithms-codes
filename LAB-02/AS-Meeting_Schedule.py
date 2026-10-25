def select_meeting_activities(activities):

    def sort_activity(activity):
        return (activity[2], activity[1], activity[0])

    activities.sort(key=sort_activity)

    selected = []
    last_finish = -1

    for activity in activities:
        if activity[1] >= last_finish:
            selected.append(activity)
            last_finish = activity[2]

    result = []

    result.append("Activity Selection Report")
    result.append("Selected Activities")
    result.append("Activity Start Finish Reason")

    for i in range(len(selected)):
        activity_id = selected[i][0]
        start = selected[i][1]
        finish = selected[i][2]

        if i == 0:
            reason = "Selected first because it finishes earliest"
        else:
            reason = "Selected because start time is compatible"

        result.append(f"{activity_id} {start} {finish} {reason}")

    result.append(f"Total Selected: {len(selected)}")
    result.append("Justification: Greedy selection by earliest finish time maximizes compatible activities")

    return result

# function calling
activities = [
    ("A", 1, 3),
    ("B", 2, 5),
    ("C", 4, 6),
    ("D", 6, 7),
    ("E", 5, 9)
]

result = select_meeting_activities(activities)

for line in result:
    print(line)

