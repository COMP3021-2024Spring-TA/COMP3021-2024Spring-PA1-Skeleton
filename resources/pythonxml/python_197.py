class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        queue = collections.deque(['0000'])
        visited = set(['0000'])
        deadset = set(deadends)
        level = 0
        while queue:
            size = len(queue)
            for _ in range(size):
                cur = queue.popleft()
                if cur in deadset:
                    continue
                if cur == target:
                    return level
                for i in range(len(cur)):
                    up = self.upward_adjust(cur, i)
                    if up not in visited:
                        queue.append(up)
                        visited.add(up)
                    down = self.downward_adjust(cur, i)
                    if down not in visited:
                        queue.append(down)
                        visited.add(down)
            level += 1
        return -1

    def upward_adjust(self, s, i):
        s_list = list(s)
        if s_list[i] == '9':
            s_list[i] = '0'
        else:
            s_list[i] = chr(ord(s_list[i]) + 1)
        return "".join(s_list)

    def downward_adjust(self, s, i):
        s_list = list(s)
        if s_list[i] == '0':
            s_list[i] = '9'
        else:
            s_list[i] = chr(ord(s_list[i]) - 1)
        return "".join(s_list)