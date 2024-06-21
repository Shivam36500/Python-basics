def longest_common_subsequence(str1, str2):
    m = len(str1)
    n = len(str2)

    # Create a 2D list to store lengths of longest common subsequence.
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    # Building the dp table in bottom-up manner
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if str1[i - 1] == str2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    # dp[m][n] contains the length of LCS
    lcs_length = dp[m][n]

    # Recovering the LCS itself
    lcs = []
    i, j = m, n
    while i > 0 and j > 0:
        if str1[i - 1] == str2[j - 1]:
            lcs.append(str1[i - 1])
            i -= 1
            j -= 1
        elif dp[i - 1][j] >= dp[i][j - 1]:
            i -= 1
        else:
            j -= 1

    # Since we built the LCS backwards, reverse it
    lcs.reverse()

    return ''.join(lcs)

# Example usage:
if __name__ == "__main__":
    str1 = "ABCDGH"
    str2 = "AEDFHR"
    print("Longest Common Subsequence:", longest_common_subsequence(str1, str2))  # Output: "ADH"

    str3 = "AGGTAB"
    str4 = "GXTXAYB"
    print("Longest Common Subsequence:", longest_common_subsequence(str3, str4))  # Output: "GTAB"

