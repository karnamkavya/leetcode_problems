class Solution:
    def remainingMethods(self, n, k, invocations):

        graph = [[] for _ in range(n)]

        for a, b in invocations:
            graph[a].append(b)

        suspicious = [False] * n

        def dfs(node):
            suspicious[node] = True

            for nei in graph[node]:
                if not suspicious[nei]:
                    dfs(nei)

        dfs(k)

        # Check whether removal is possible
        for a, b in invocations:
            if not suspicious[a] and suspicious[b]:
                return list(range(n))

        # Return remaining methods
        ans = []

        for i in range(n):
            if not suspicious[i]:
                ans.append(i)

        return ans