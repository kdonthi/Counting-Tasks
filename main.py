# tasks = ["A", "A", "A", "B", "B", "B"]
# idle_time = 2

# tasks = ["A", "A", "A", "B", "B", "B"]
# idle_time = 0
#
# tasks = ["A", "A", "A", "A", "A", "A", "B", "C", "D", "E", "F", "G"]
# idle_time = 2

tasks = ["C", "A", "B", "C", "C"]
idle_time = 5

# Get number of each letter
task_to_count = {}
for task in tasks:
    if task in task_to_count:
        task_to_count[task] += 1
    else:
        task_to_count[task] = 1

#print(task_to_count)

# Create a list where each of the highest count letter has the designated idle time
list_task_to_count = [(k, v) for k, v in task_to_count.items()]
sorted_task_list = sorted(list_task_to_count, key=lambda l: l[1], reverse=True)

# Go through the letters by order of count
new_list = []
for task, count in sorted_task_list:
    index = 0

    for i in range(count):
        while True:
            if len(new_list) - 1 < index:
                new_list.append(task)
                break
            elif new_list[index] == "":
                new_list[index] = task
                break
            else:
                index += 1
        if i != count - 1:
            for i in range(idle_time + 1):
                index += 1
                if len(new_list) - 1 < index:
                    new_list.append("")

print(new_list)
print(len(new_list))
# Try to fill in the spaces or add more if we need to




