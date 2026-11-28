class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:

        adj = {i:[] for i in range(n)}

        visited = set()
        res = 0

        for a,b in edges:
            adj[a].append(b)
            adj[b].append(a)   
        

        def dfs(root):

            if root in visited:
                return 
            
            visited.add(root)
            for v in adj[root]:
                dfs(v)
        
        for keys in adj:

            if keys not in visited:
                dfs(keys)
                res += 1
        
        return res

            
