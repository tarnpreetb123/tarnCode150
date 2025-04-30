class Solution:
    def useMinimumTokens(self, warehouse: list[int], catalog: list[list[int]]) -> list[int]:

        total_capacity = sum(warehouse)
        res = []

        for A, B in catalog:
            lowest_tokens = float("inf")

            for ware in warehouse:
                tokens = max(0, A - ware)
                backup = total_capacity - ware
                tokens_backup = max(0, B - backup)

                lowest_tokens = min(lowest_tokens, tokens + tokens_backup)

            res.append(lowest_tokens)

        return res


test_cases = [
    ([10, 5, 8], [[7, 12], [6, 19]], [0, 2]),
    ([3, 4], [[5, 0]], [1]),
    ([2, 2, 2], [[5, 4]], [3]),
    ([10, 1], [[5, 15]], [9]),
    ([8, 8, 8], [[10, 0], [0, 15]], [2, 0]),
]

solver = Solution()
all_ok = True

for idx, (ware, cat, expected) in enumerate(test_cases, 1):
    got = solver.useMinimumTokens(ware, cat)
    status = "PASS" if got == expected else "FAIL"
    print(f"Test {idx}: expected={expected}, got={got}  →  {status}")
    if status == "FAIL":
        all_ok = False

print("\nOverall:", "ALL TESTS PASSED ✔️" if all_ok else "Some tests failed ❌")