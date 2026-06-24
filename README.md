# Boot.dev Course Author — Take-Home

Two new lessons for Boot.dev's **Learn to Code in Python** course, written to match the existing
course's format, tone, and test structure.

## Lessons

| Lesson | Concept | Functions the student completes |
| --- | --- | --- |
| [`list-comprehension/`](./list-comprehension/) | Building new lists with comprehensions, including filtering with `if` | `apply_rage`, `get_critical_hits` |
| [`enumerate/`](./enumerate/) | Looping over index + element pairs with `enumerate()` and its `start` argument | `number_spells` |

Both lessons use the course's **Fantasy Quest** theme and build each new idea up from something the
student has already met — the `for` loop, and the manual counter variable.

## Files in each lesson

Each lesson directory holds the four standard files:

- `readme.md` — the lesson content shown on the left-hand side of the screen
- `incomplete_main.py` — the starter code the student fills in
- `complete_main.py` — the reference solution
- `test_main.py` — the test suite (Boot.dev's `run_cases` / `submit_cases` print-based runner)

## Running the tests locally

`test_main.py` imports from `incomplete_main.py` (the file the student edits), exactly as it does on
the platform. Run it against the untouched starter and you'll see `============= FAIL ==============`
— that's the work left for the student.

To watch the tests pass against the reference solution, point them at the completed code:

```bash
cd list-comprehension
cp complete_main.py incomplete_main.py   # temporarily drop in the solution
python3 test_main.py                     # => ============= PASS ==============
git checkout incomplete_main.py          # restore the starter stub
```

The same steps work in the `enumerate/` directory.
