# List Comprehensions

A **list comprehension** is a shorthand for building a new list from an existing one. It's one of the most _loved_ features in Python, and once it clicks you'll reach for it all the time.

Let's say our hero just landed a few hits in Fantasy Quest, and we want to double every one of them. The way you already know is a `for` loop with `.append()`:

```python
attacks = [10, 25, 30]
doubled = []
for attack in attacks:
    doubled.append(attack * 2)
print(doubled)
# [20, 50, 60]
```

That works, but it's four lines to do one simple thing. A list comprehension does the exact same work in a single line:

```python
attacks = [10, 25, 30]
doubled = [attack * 2 for attack in attacks]
print(doubled)
# [20, 50, 60]
```

Read it left to right: _"give me `attack * 2` for each `attack` in `attacks`"_. The part _before_ the `for` is the expression that builds each new item.

## Filtering With an `if`

You can also tack an `if` onto the end to _keep only some_ of the items. This builds a new list of just the attacks that are `50` or higher:

```python
attacks = [10, 60, 30, 90]
big_hits = [attack for attack in attacks if attack >= 50]
print(big_hits)
# [60, 90]
```

With no `if`, every item makes it into the new list. With one, only the items where the condition is `True` are included.

<details open>
<summary><h2>Assignment</h2></summary>

We're building the post-battle damage report for Fantasy Quest. Complete the two functions in `incomplete_main.py`. Each one takes `attacks`, a list of integers.

1. Complete the `apply_rage` function. The Berserker's Rage buff doubles _every_ attack. Use a list comprehension to return a new list where each attack has been multiplied by `2`.
2. Complete the `get_critical_hits` function. A _critical hit_ is any attack of `50` or more. Use a list comprehension with an `if` to return a new list containing only the attacks that are `>= 50`.

Here's how they should work:

```python
print(apply_rage([10, 25, 30]))
# [20, 50, 60]
print(get_critical_hits([10, 60, 30, 90]))
# [60, 90]
```

</details>

<details open>
<summary><h2>Note</h2></summary>

A list comprehension always builds a _brand new_ list, it never changes the original. Think of it like copying your loot into a fresh bag one item at a time, instead of rummaging through the old one.

</details>

<details>
<summary><h2>Tip</h2></summary>

The shape of a filtering comprehension is:

```python
[item for item in old_list if condition]
```

When you don't need to transform the item, the expression at the front is just the item itself.

</details>

<details>
<summary><h1>Multiple Choice Question</h1></summary>

## Syntax

Which list comprehension keeps only the _even_ numbers from a list called `nums`?

1. `[n * 2 for n in nums]` # Incorrect, this doubles every number instead of filtering.
2. `[n for n in nums if n % 2 == 0]` # Correct!
3. `[n for n in nums]` # Incorrect, this copies every number with no filtering.

</details>
