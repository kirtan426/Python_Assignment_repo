# Use a greedy + min-heap to track task durations.
# Remove longest-duration task if it exceeds deadline.

tasks = [
    {'name': 'Task 1', 'deadline': 4, 'duration': 2},
    {'name': 'Task 2', 'deadline': 3, 'duration': 1},
    {'name': 'Task 3', 'deadline': 2, 'duration': 1},
    {'name': 'Task 4', 'deadline': 1, 'duration': 2},
]

def max_tasks(tasks):
    tasks.sort(key=lambda x: x['deadline'])
    time = 0
    completed = []
    for task in tasks:
        if time + task['duration'] <= task['deadline']:
            completed.append(task['name'])
    return completed

print(max_tasks(tasks))