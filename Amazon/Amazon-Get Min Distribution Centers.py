class Solution:
    def getMinimumNumberOfUniqueDistributionCenters(self, n: int, dailyTrend: list[int]) -> int:

        low = 0
        high = 0

        counter = 0
        for i in range(1, len(dailyTrend)):
            prev = dailyTrend[i - 1]
            curr = dailyTrend[i]
            diff = curr - prev
            if diff > 0:
                counter += 1
            elif diff < 0:
                counter -= 1
            low = min(low, counter)
            high = max(high, counter)

        return (high - low) + 1


# ── Test cases: (feature1, feature2, expected) ──────────────────────
# ── Test cases for getMinimumNumberOfUniqueDistributionCenters ─────
test_cases = [
    # 1) Edge‑case: only one day → always 1 centre
    (1, [42], 1),
    # 2) All demands equal → never move up or down
    (4, [7, 7, 7, 7], 1),
    # 3) Strictly increasing each day → need a new, higher id every day
    #    levels visited: 0, 1, 2, 3  ⇒ 4 unique ids
    (4, [1, 2, 3, 4], 4),
    # 4) Strictly decreasing each day → symmetric to case 3
    #    levels visited: 0, -1, -2, -3  ⇒ 4 unique ids
    (4, [4, 3, 2, 1], 4),
    # 5) Prompt’s worked example
    #    10 → 20 → 30 ↑↑, then 30 → 15 ↓, 15 → 10 ↓
    (5, [10, 20, 30, 15, 10], 3),
    # 6) Up, plateau, down, plateau, down
    #    levels: 0,1,1,0,1,1,0  ⇒ min=0, max=1  ⇒ 2 ids
    (7, [10, 20, 20, 15, 25, 25, 10], 2),
    # 7) Larger swing: climb to peak level 3 then descend
    #    levels: 0,1,2,3,2,1,0  ⇒ min=0, max=3  ⇒ 4 ids
    (7, [10, 20, 30, 40, 30, 20, 10], 4),
]

solver = Solution()
all_ok = True
for idx, (n, trend, expected) in enumerate(test_cases, 1):
    got = solver.getMinimumNumberOfUniqueDistributionCenters(n, trend)
    status = "PASS" if got == expected else "FAIL"
    print(f"Test {idx}: expected={expected}, got={got}  →  {status}")
    if status == "FAIL":
        all_ok = False

print("\nOverall:", "ALL TESTS PASSED ✔️" if all_ok else "Some tests failed ❌")


