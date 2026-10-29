class Solution:
    def palindromePath(self, n: int, edges: list[list[int]], s: str, queries: list[str]) -> list[bool]:
        g = [[] for _ in range(n)]

        for u, v in edges:
            g[u].append(v)
            g[v].append(u)

        parent = [-1] * n
        depth = [0] * n
        order = []
        stack = [0]

        while stack:
            u = stack.pop()
            order.append(u)

            for v in g[u]:
                if v != parent[u]:
                    parent[v] = u
                    depth[v] = depth[u] + 1
                    stack.append(v)

        size = [1] * n
        heavy = [-1] * n

        for u in reversed(order):
            for v in g[u]:
                if v != parent[u]:
                    size[u] += size[v]
                    if heavy[u] == -1 or size[v] > size[heavy[u]]:
                        heavy[u] = v

        head = [0] * n
        pos = [0] * n
        cur = 0
        stack = [(0, 0)]

        while stack:
            u, h = stack.pop()

            while u != -1:
                head[u] = h
                pos[u] = cur
                cur += 1

                for v in g[u]:
                    if v != parent[u] and v != heavy[u]:
                        stack.append((v, v))

                u = heavy[u]

        bit = [0] * (n + 1)
        mask = [1 << (ord(c) - ord('a')) for c in s]

        def update(i, val):
            i += 1
            while i <= n:
                bit[i] ^= val
                i += i & -i

        def prefix(i):
            res = 0
            i += 1
            while i > 0:
                res ^= bit[i]
                i -= i & -i
            return res

        def range_xor(l, r):
            res = prefix(r)
            if l > 0:
                res ^= prefix(l - 1)
            return res

        for u in range(n):
            update(pos[u], mask[u])

        def path_xor(u, v):
            res = 0

            while head[u] != head[v]:
                if depth[head[u]] < depth[head[v]]:
                    u, v = v, u

                res ^= range_xor(pos[head[u]], pos[u])
                u = parent[head[u]]

            if depth[u] > depth[v]:
                u, v = v, u

            res ^= range_xor(pos[u], pos[v])
            return res

        ans = []

        for q in queries:
            parts = q.split()

            if parts[0] == "update":
                u = int(parts[1])
                new_mask = 1 << (ord(parts[2]) - ord('a'))

                if mask[u] != new_mask:
                    update(pos[u], mask[u] ^ new_mask)
                    mask[u] = new_mask

            else:
                u = int(parts[1])
                v = int(parts[2])
                ans.append(path_xor(u, v).bit_count() <= 1)

        return ans