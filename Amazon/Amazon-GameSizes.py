class Solution:


    def getMinSize1(self, gameSize: list[int], k: int) -> int:
        gameSize.sort(reverse=True)
        maximum = gameSize[0]

        singleGames = 2*k - len(gameSize)

        #First k largest games get put into a penDrive for sure by themselves so n - k is the pivot point
        for i in range(len(gameSize) - k):
            maximum = max(maximum, gameSize[k - i - 1] + gameSize[k + i])

        return maximum



    def getMinSize(self, gameSize: list[int], k: int) -> int:

        gameSize.sort(reverse=True)

        low = gameSize[0]
        high = gameSize[0] + (gameSize[1] if len(gameSize) > 1 else 0)

        def feasible(capacity: int):
            l, r = 0, len(gameSize) - 1
            penDrives = 0

            while l <= r:
                if l == r:
                    penDrives += 1
                    return penDrives <= k

                if gameSize[l] + gameSize[r] <= capacity:
                    l += 1
                    r -= 1
                else:
                    l += 1

                penDrives += 1

            return penDrives <= k


        while low < high:
            mid = low + (high-low)//2

            if feasible(mid):
                high = mid
            else:
                low = mid + 1

        return low






# ── Test‑case suite for getMinSize ────────────────────────────────────
test_cases = [
    # (gameSize list, k, expected_min_capacity)

    # 1. Prompt/example case
    ([9, 2, 4, 6],                 3, 9),

    # 2.  n == k  → every child gets exactly one game
    ([5, 4, 3],                    3, 5),

    # 3.  n == 2k → every stick gets two games
    ([1, 2, 3, 4],                 2, 5),      # pairs: (4,1) & (3,2)

    # 4.  Mixed singles + pairs
    ([10, 8, 7, 3, 2],             3, 10),     # 10 single; (8,2) & (7,3)

    # 5.  Single game / single child
    ([1],                          1, 1),

    # 6.  Identical large games – capacity set by a pair
    ([8, 8, 8, 8],                 2, 16),     # two sticks, each 8+8

    # 7.  Largest game forces a high capacity when n == 2k
    ([12, 1, 1, 1, 1, 1],          3, 13),     # must pair 12+1

    # 8.  Already sorted descending, capacity decided by biggest single
    ([9, 8, 7, 2, 1, 1],           4, 9),      # singles: 9,8 ; pairs: (7,1), (2,1)
]

# ── Runner ────────────────────────────────────────────────────────────
solver = Solution()
all_passed = True
for idx, (games, k, expected) in enumerate(test_cases, 1):
    got = solver.getMinSize1(games.copy(), k)   # copy to avoid in‑place sort side‑effects
    status = "PASS" if got == expected else "FAIL"
    print(f"Test {idx}: expected={expected}, got={got}  →  {status}")
    if status == "FAIL":
        all_passed = False

print("\nOverall:", "ALL TESTS PASSED ✔️" if all_passed else "Some tests failed ❌")


all_passed = True
for idx, (games, k, expected) in enumerate(test_cases, 1):
    got = solver.getMinSize(games.copy(), k)   # copy to avoid in‑place sort side‑effects
    status = "PASS" if got == expected else "FAIL"
    print(f"Test {idx}: expected={expected}, got={got}  →  {status}")
    if status == "FAIL":
        all_passed = False

print("\nOverall:", "ALL TESTS PASSED ✔️" if all_passed else "Some tests failed ❌")