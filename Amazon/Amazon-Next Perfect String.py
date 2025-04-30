class Solution:
    def nextGreaterPerfectString(self, s: str) -> str:

        if len(s) == 0:
            return "-1"

        alphabet = "abcdefghijklmnopqrstuvwxyz"

        isPerfect = [True] * len(s)
        arrString = list(s)

        for i in range(1, len(s)):
            isPerfect[i] = isPerfect[i - 1] and (s[i] != s[i - 1])

        for i in range(len(s) - 1, -1, -1):

            if i > 0 and not isPerfect[i - 1]:
                continue

            for index in range(ord(s[i]) - ord('a') + 1, 26):
                letter = alphabet[index]

                if i > 0 and arrString[i - 1] == letter:
                    continue

                arrString[i] = letter

                ok = True
                for j in range(i + 1, len(s)):
                    for d in alphabet:
                        if d != arrString[j - 1]:
                            arrString[j] = d
                            break
                    else:
                        ok = False
                        break

                if ok:
                    return "".join(arrString)

            arrString[i] = s[i]

        return "-1"


# ── Test‑case suite for getMinSize ────────────────────────────────────
test_cases = [
    ("", "-1"),
    ("a", "b"),
    ("z", "-1"),
    ("aa", "ab"),
    ("ab", "ac"),
    ("az", "ba"),
    ("abzzzcd", "acababa"),
    ("zzab", "-1"),
    ("zaz", "zba"),
    ("xyz", "xza"),
    ("zzz", "-1"),
    ("pqq", "pqr"),  # will fail until you fix the alphabet string
]

# ── Runner ────────────────────────────────────────────────────────────
solver = Solution()
all_passed = True
sol = Solution()
for i, (inp, exp) in enumerate(test_cases, 1):
    out = sol.nextGreaterPerfectString(inp)
    status = "✓" if out == exp else f"✗  (got '{out}')"
    print(f"{i:2}.  {inp!r:10} → {out!r:10} {status}")

    if status == "FAIL":
        all_passed = False

print("\nOverall:", "ALL TESTS PASSED ✔️" if all_passed else "Some tests failed ❌")
