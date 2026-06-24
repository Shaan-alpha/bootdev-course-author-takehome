from incomplete_main import number_spells

run_cases = [
    (["Fireball", "Heal", "Frostbite"], ["1. Fireball", "2. Heal", "3. Frostbite"]),
    (["Mage Light"], ["1. Mage Light"]),
]

submit_cases = run_cases + [
    ([], []),
    (
        ["Lightning Bolt", "Freeze", "Daze", "Haste"],
        ["1. Lightning Bolt", "2. Freeze", "3. Daze", "4. Haste"],
    ),
    (["Heal", "Heal"], ["1. Heal", "2. Heal"]),
]


def test(spells, expected_output):
    print("---------------------------------")
    print(f"Inputs: {spells}")
    result = number_spells(spells)
    print(f"Expected: {expected_output}")
    print(f"Actual:   {result}")
    if result == expected_output:
        print("Pass")
        return True
    print("Fail")
    return False


def main():
    passed = 0
    failed = 0
    skipped = len(submit_cases) - len(test_cases)
    for test_case in test_cases:
        correct = test(*test_case)
        if correct:
            passed += 1
        else:
            failed += 1
    if failed == 0:
        print("============= PASS ==============")
    else:
        print("============= FAIL ==============")
    if skipped > 0:
        print(f"{passed} passed, {failed} failed, {skipped} skipped")
    else:
        print(f"{passed} passed, {failed} failed")


test_cases = submit_cases
if "__RUN__" in globals():
    test_cases = run_cases

main()
