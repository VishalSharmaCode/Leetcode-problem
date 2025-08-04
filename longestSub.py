def longestPalindrome(s: str) -> str:
    n = len(s)
    if n < 2:
        return s

    dp = [[False] * n for _ in range(n)]
    start = 0
    max_len = 1

    # Step 1: All substrings of length 1 are palindromes
    for i in range(n):
        dp[i][i] = True

    # Step 2: Check substrings of length 2
    for i in range(n - 1):
        if s[i] == s[i + 1]:
            dp[i][i + 1] = True
            start = i
            max_len = 2

    # Step 3: Check substrings of length 3 and more
    for length in range(3, n + 1):  # substring lengths
        for i in range(n - length + 1):
            j = i + length - 1  # ending index
            if s[i] == s[j] and dp[i + 1][j - 1]:
                dp[i][j] = True
                if length > max_len:
                    start = i
                    max_len = length

    return s[start:start + max_len]