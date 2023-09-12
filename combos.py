def recursive_combo(text, prefix="", k=0):
    if k == 0:
        all_combos.append([int(x) for x in list(prefix)])
        return
    for i in range(len(text)):
        new_prefix = prefix + text[i]
        recursive_combo(text, new_prefix, k - 1)


all_combos = [] # Contains all the combinations, even those that add up to more than the number of steps.
number_steps = 10 # The total of the numbers in the combinations must equal this.

# Generate combinations for all steps, one step at a time [n], [n, n], [n, n, n], etc...
for a in range(1, number_steps + 1):
    recursive_combo("12", "", a)

number_combos = 0 # Count the matching combinations.
for b in all_combos:

    if sum(b) == number_steps:
        number_combos += 1
        print(f"{number_combos}) {' + '.join([str(x) for x in b])} = {number_steps}")

print(f"The total number of combinations matching was {number_combos}")
