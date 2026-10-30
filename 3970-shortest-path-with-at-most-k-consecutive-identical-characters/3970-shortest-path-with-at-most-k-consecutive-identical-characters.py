class Solution:
    def shortestPath(self, n: int, edges: List[List[int]], labels: str, k: int) -> int:
        import heapq
        from collections import defaultdict

        graph = defaultdict(list)

        for u, v, w in edges:
            graph[u].append((v, w))

        pq = [(0, 0, labels[0], 1)]
        dist = {}

        while pq:
            cost, node, last_char, count = heapq.heappop(pq)

            state = (node, last_char, count)

            if state in dist:
                continue

            dist[state] = cost

            if node == n - 1:
                return cost

            for nei, weight in graph[node]:
                ch = labels[nei]

                if ch == last_char:
                    new_count = count + 1
                else:
                    new_count = 1

                if new_count <= k:
                    new_state = (nei, ch, new_count)

                    if new_state not in dist:
                        heapq.heappush(
                            pq,
                            (cost + weight, nei, ch, new_count)
                        )

        return -1