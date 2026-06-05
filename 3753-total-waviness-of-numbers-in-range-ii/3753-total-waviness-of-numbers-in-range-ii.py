from functools import cache
class Solution:
    def totalWaviness(self, num1: int, num2: int) -> int:
        def solve(x: int) -> int:
            if x < 0:
                return 0
            s = str(x)
            @cache
            def count(pos, tight, started, prev2, prev1):
                if pos == len(s):
                    return 1
                limit = int(s[pos]) if tight else 9
                ans = 0
                for d in range(limit + 1):
                    ntight = tight and d == limit
                    if not started and d == 0:
                        ans += count(pos + 1, ntight, False, -1, -1)
                    elif not started:
                        ans += count(pos + 1, ntight, True, -1, d)
                    elif prev2 == -1:
                        ans += count(pos + 1, ntight, True, prev1, d)
                    else:
                        ans += count(pos + 1, ntight, True, prev1, d)
                return ans
            @cache
            def wave(pos, tight, started, prev2, prev1):
                if pos == len(s):
                    return 0
                limit = int(s[pos]) if tight else 9
                ans = 0
                for d in range(limit + 1):
                    ntight = tight and d == limit
                    if not started and d == 0:
                        ans += wave(pos + 1, ntight, False, -1, -1)
                    elif not started:
                        ans += wave(pos + 1, ntight, True, -1, d)
                    elif prev2 == -1:
                        ans += wave(pos + 1, ntight, True, prev1, d)
                    else:
                        add = (
                            (prev1 > prev2 and prev1 > d)
                            or
                            (prev1 < prev2 and prev1 < d)
                        )
                        ans += wave(pos + 1, ntight, True, prev1, d)
                        if add:
                            ans += count(
                                pos + 1,
                                ntight,
                                True,
                                prev1,
                                d
                            )
                return ans
            return wave(0, True, False, -1, -1)
        return solve(num2) - solve(num1 - 1)