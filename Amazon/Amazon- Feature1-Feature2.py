class Solution:
    def lengthOfLIS(self, nums: list[int]) -> int:
        LIS = [1]*len(nums)

        #Start at the last index
        for i in range(len(nums)-1,-1,-1):
            #Check all future index, possabilities, we want the largest one
            for j in range(i+1, len(nums)):

                if nums[i] < nums[j]:
                    LIS[i] = max(LIS[i], 1+LIS[j])

        return max(LIS)

    def getLargestIndexLenS(self, feature1: list[int], feature2: list[int]) -> int:

        pair = [(feature1[i], feature2[i]) for i in range(len(feature1))]
        pair.sort(key=lambda p: (p[0], -p[1]))
        f2 = [x[1] for x in pair]
        return self.lengthOfLIS(f2)


# ── Test cases: (feature1, feature2, expected) ──────────────────────
test_cases = [
    ([1],                [10],             1),  # single element
    ([1, 2, 3],          [1, 2, 3],        3),  # strictly ↑↑
    ([1, 2, 3],          [3, 2, 1],        1),  # ↑ / ↓
    ([4, 5, 3, 1, 2],    [2, 1, 3, 4, 5],  2),  # prompt sample
    ([1, 1, 2, 2],       [1, 2, 3, 4],     2),  # tie on feature1
    ([5, 4, 3, 2, 1],    [5, 4, 3, 2, 1],  5),  # both ↓↓ (needs “down” pass too)
]

# ── Runner ──────────────────────────────────────────────────────────
solver = Solution()
all_passed = True
for idx, (f1, f2, expected) in enumerate(test_cases, 1):
    got = solver.getLargestIndexLenS(f1, f2)
    status = "PASS" if got == expected else "FAIL"
    print(f"Test {idx}: expected={expected}, got={got}  →  {status}")
    if status == "FAIL":
        all_passed = False

print("\nOverall:", "ALL TESTS PASSED ✔️" if all_passed else "Some tests failed ❌")