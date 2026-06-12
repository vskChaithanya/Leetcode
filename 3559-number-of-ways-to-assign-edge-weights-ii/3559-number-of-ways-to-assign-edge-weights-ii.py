class Solution:
    def assignEdgeWeights(self, edges: List[List[int]], queries: List[List[int]]) -> List[int]:
        MOD = 10**9 + 7

        n = len(edges) + 1

        g = [[] for _ in range(n + 1)]

        for u, v in edges:

            g[u].append(v)

            g[v].append(u)

        LOG = (n).bit_length()

        depth = [0] * (n + 1)

        up = [[0] * (n + 1) for _ in range(LOG)]

        def dfs(u, p):

            up[0][u] = p

            for v in g[u]:

                if v != p:

                    depth[v] = depth[u] + 1

                    dfs(v, u)

        dfs(1, 1)

        for j in range(1, LOG):

            for v in range(1, n + 1):

                up[j][v] = up[j - 1][up[j - 1][v]]

        def lca(a, b):

            if depth[a] < depth[b]:

                a, b = b, a

            diff = depth[a] - depth[b]

            bit = 0

            while diff:

                if diff & 1:

                    a = up[bit][a]

                diff >>= 1

                bit += 1

            if a == b:

                return a

            for j in range(LOG - 1, -1, -1):

                if up[j][a] != up[j][b]:

                    a = up[j][a]

                    b = up[j][b]

            return up[0][a]

        ans = []

        for u, v in queries:

            w = lca(u, v)

            dist = depth[u] + depth[v] - 2 * depth[w]

            if dist == 0:

                ans.append(0)

            else:

                ans.append(pow(2, dist - 1, MOD))

        return ans