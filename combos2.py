# From the assignment of Caleb Liu
# With minor modifications by Brendan Wood
#
def skip_step(n, path=None):

    if path is None:
        path = []

    if n < 0:
        return []

    if n == 0:
        return [path]

    paths = []

    for step in [1, 2]:
        sub_paths = skip_step(n - step, path + [step])
        paths.extend(sub_paths)

    return paths


total_steps = input("Enter a positive number: ")

if total_steps is None or not total_steps.isdigit():
    print("{} is not a valid number".format(total_steps))
else:
    number = int(total_steps)
    steps = skip_step(number)

    print(f'Total ways to reach {total_steps} stairs:')
    for s in steps:
        print(s)

    print(f"Total combinations: {len(steps)}")
