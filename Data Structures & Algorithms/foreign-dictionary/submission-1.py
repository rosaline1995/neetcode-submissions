class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        # I first tried Trie but got stuck 
        # because I still didn't know how to merge children,
        # which still required topological sort. 
        # I don't think DFS topological sort is easy to understand,
        # but I will implement it just in case
        state = {} # state=0 means never visited, state=1 means visiting, state=2 means visited
        graph = {}
        for w in words:
            for c in w:
                graph[c] = set()
                state[c] = 0
        for i in range(len(words)-1):
            w1 = words[i]
            w2 = words[i+1]
            minL = min(len(w2), len(w1))
            if w1[:minL] == w2[:minL] and len(w1) > len(w2):
                return ''
            for ic in range(minL):
                if w1[ic] != w2[ic]:
                    graph[w1[ic]].add(w2[ic])
                    break
        print(graph)
        res = []
        def dfs(c):
            if state[c] != 0:
                return state[c]
            state[c] = 1
            for nb in graph[c]:
                if dfs(nb) == 1:
                    return state[nb] 
            state[c] = 2
            res.append(c)
            return state[c]
        for c in graph:
            if dfs(c) == 1:
                return ''
        return (''.join(res))[::-1]


            
