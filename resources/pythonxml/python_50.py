for i in range(size - 1, -1, -1):       
    for j in range(i + 1, size):        
        
        dp[i][j] = max(dp[i + 1][j - 1], dp[i + 1][j], dp[i][j - 1]) + cost[i][j]