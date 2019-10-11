def numDecodings(s):
    if not s:
        return 0
    dp = [0] * (len(s) + 1)
    dp[0] = 1
    for i in range(1, len(s) + 1):
        print(dp)
        if s[i - 1] > '0':
            dp[i] = dp[i - 1]
            if i > 1 and s[i - 2] > '0' and (s[i - 2], s[i - 1]) <= ('2', '6'):
                dp[i] += dp[i - 2]
        else:
            if i > 1 and s[i - 2] > '0' and s[i - 2] < '3':
                dp[i] = dp[i - 2]
            else:
                return 0
    return dp[-1]
