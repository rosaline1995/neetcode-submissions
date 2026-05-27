from collections import deque
class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        # I first tried Trie but got stuck 
        # because I still didn't know how to merge children,
        # which still required topological sort. 
        # BFS + indegree is an easier-to-understand solution.
        ind = {}
        graph = {}
        for w in words:
            for c in w:
                ind[c] = 0
                graph[c] = set()
        for i in range(len(words)-1):
            w1 = words[i]
            w2 = words[i+1]
            minL = min(len(w2), len(w1))
            if len(w1) > len(w2) and w1[:minL] == w2[:minL]:
                return ''
            for j in range(minL):
                if w1[j] != w2[j]:
                    if w2[j] not in graph[w1[j]]:
                        graph[w1[j]].add(w2[j])    
                        ind[w2[j]] += 1
                    break
        q = deque()
        for c in ind:
            if ind[c] == 0:
                q.append(c)
        ans = ''
        while q:
            c = q.popleft()
            ans += c
            for nb in graph[c]:
                ind[nb] -= 1
                if ind[nb] == 0:
                    q.append(nb)
        if len(ans) != len(ind):
            return ''
        return ans
