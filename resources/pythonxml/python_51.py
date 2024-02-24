for l in range(1, n):               
    for i in range(n):              
        j = i + l - 1               
        if j >= n:
            break
        dp[i][j] = float('-inf')    
        for k in range(i, j + 1):   
            
            dp[i][j] = max(dp[i][j], dp[i][k] + dp[k + 1][j] + cost[i][j])