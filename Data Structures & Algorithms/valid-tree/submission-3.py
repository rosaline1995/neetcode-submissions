from collections import deque
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if not edges:
            return n==1
        node = [[] for _ in range(n)]
        q = deque()
        for e in edges:
            a,b = e
            node[a].append(b)
            node[b].append(a)
            if not q:
                q.append((a, -1))
        visited = set()
        while q:
            cur, pcur = q.popleft()
            visited.add(cur)
            for nb in node[cur]:
                if nb == pcur:
                    continue
                if nb in visited:
                    return False
                q.append((nb, cur))
        return len(visited) == n
