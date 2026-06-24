# Enumerate()

When you loop over a list, sometimes you need to know _where_ you are in the list, not just the item itself. Maybe you want to number a menu, or treat the first item differently.

You _could_ track your position with a counter variable:

```python
spells = ["Fireball", "Heal", "Frostbite"]
number = 1
for spell in spells:
    print(f"{number}. {spell}")
    number += 1
# 1. Fireball
# 2. Heal
# 3. Frostbite
```

That works, but babysitting the `number` variable by hand is easy to get wrong. Python's **enumerate()** does it for you. It hands you both the index _and_ the item on each pass of the loop:

```python
spells = ["Fireball", "Heal", "Frostbite"]
for i, spell in enumerate(spells):
    print(f"{i}: {spell}")
# 0: Fireball
# 1: Heal
# 2: Frostbite
```

Notice that `enumerate()` starts counting at `0`, just like list indexes do.

## Starting at a Different Number

Players don't read a menu starting from zero. `enumerate()` takes an optional second argument that sets the starting number:

```python
spells = ["Fireball", "Heal", "Frostbite"]
for i, spell in enumerate(spells, 1):
    print(f"{i}. {spell}")
# 1. Fireball
# 2. Heal
# 3. Frostbite
```

Same loop, but the count now starts at `1`, which is exactly what a player expects to see.

<details open>
<summary><h2>Assignment</h2></summary>

Time to render the spellbook menu for Fantasy Quest. Complete the `number_spells` function in `incomplete_main.py`. It takes `spells`, a list of spell-name strings.

1. Create an empty list to hold the finished menu lines.
2. Loop over `spells` with `enumerate()`, starting the count at `1`.
3. For each spell, build the string `"<number>. <spell>"` and add it to your list.
4. Return the list of strings.

Here's how it should work:

```python
print(number_spells(["Fireball", "Heal", "Frostbite"]))
# ['1. Fireball', '2. Heal', '3. Frostbite']
```

The text will need to match the expected results _exactly_, so double-check your spacing: a number, a period, a single space, then the spell name.

</details>

<details open>
<summary><h2>Note</h2></summary>

`enumerate()` gives you the index and the item _together_ on every pass. The two names in `for i, spell in ...` are unpacked in order: the first is always the number, the second is always the item.

</details>

<details>
<summary><h2>Tip</h2></summary>

An f-string is the cleanest way to glue the number and the spell together:

```python
line = f"{i}. {spell}"
```

</details>

<details>
<summary><h1>Multiple Choice Question</h1></summary>

## Syntax

How do you make `enumerate()` start counting from `1` instead of `0`?

1. `enumerate(spells, 1)` # Correct!
2. `enumerate(1, spells)` # Incorrect, the list comes first and the start value second.
3. `enumerate(spells).start(1)` # Incorrect, `enumerate` has no `.start()` method.

</details>
