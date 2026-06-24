from incomplete_main import apply_rage, get_critical_hits

run_cases = [
    ([10, 25, 30], [20, 50, 60], []),
    ([10, 60, 30, 90], [20, 120, 60, 180], [60, 90]),
]

submit_cases = run_cases + [
    ([], [], []),
    ([50], [100], [50]),
    ([49, 50, 51], [98, 100, 102], [50, 51]),
    ([5, 10, 15], [10, 20, 30], []),
    ([100, 100], [200, 200], [100, 100]),
]


def test(attacks, expected_rage, expected_crits):
    print("---------------------------------")
    print(f"Inputs: {attacks}")
    result_rage = apply_rage(attacks)
    print(f"Expected rage:  {expected_rage}")
    print(f"Actual rage:    {result_rage}")
    if result_rage != expected_rage:
        print("Fail")
        return False
    result_crits = get_critical_hits(attacks)
    print(f"Expected crits: {expected_crits}")
    print(f"Actual crits:   {result_crits}")
    if result_crits != expected_crits:
        print("Fail")
        return False
    print("Pass")
    return True


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
