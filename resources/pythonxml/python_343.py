class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0
        
        visited = set([amount])
        queue = collections.deque([amount])

        step = 0
        while queue:
            step += 1
            size = len(queue)
            for _ in range(size):
                cur = queue.popleft()
                for coin in coins:
                    if cur == coin:
                        step += 1
                        return step
                    elif cur > coin and cur - coin not in visited:
                        queue.append(cur - coin)
                        visited.add(cur - coin)
            
        return -1