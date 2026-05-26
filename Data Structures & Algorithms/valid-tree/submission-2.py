class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if not edges:
            return n==1
        node = [[] for _ in range(n)]
        for e in edges:
            a,b = e
            node[a].append(b)
            node[b].append(a)
        visited = set()
        def dfs(cur, seen, prev):
            # print(cur, seen, prev, node[cur])
            visited.add(cur)
            for nb in node[cur]:
                print(cur, nb, node[cur], prev, seen)
                if nb == prev:
                    continue
                if nb in seen:
                    return False
                seen.add(cur)
                if not dfs(nb, seen, cur):
                    return False
            return True
        ans = True
        for i in range(len(node)):
            if node[i]:
                ans = dfs(i, set(), -1)
                break
        if ans:
            return len(visited) == n
        return False