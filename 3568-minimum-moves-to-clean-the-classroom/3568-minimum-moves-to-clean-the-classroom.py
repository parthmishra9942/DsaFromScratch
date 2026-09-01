from collections import deque

class Solution:
    def minMoves(self, classroom, energy):
        m = len(classroom)
        n = len(classroom[0])

        litter = {}
        sr = sc = 0
        count = 0

        for i in range(m):
            for j in range(n):
                if classroom[i][j] == 'S':
                    sr, sc = i, j
                elif classroom[i][j] == 'L':
                    litter[(i, j)] = count
                    count += 1

        if count == 0:
            return 0

        target = (1 << count) - 1

        # (row, col, energy, mask)
        q = deque([(sr, sc, energy, 0)])

        # Maximum remaining energy seen for each (r,c,mask)
        seen = {(sr, sc, 0): energy}

        moves = 0
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        while q:
            for _ in range(len(q)):
                r, c, e, mask = q.popleft()

                if mask == target:
                    return moves

                for dr, dc in directions:
                    nr, nc = r + dr, c + dc

                    if not (0 <= nr < m and 0 <= nc < n):
                        continue

                    if classroom[nr][nc] == 'X':
                        continue

                    if e == 0:
                        continue

                    ne = e - 1
                    nmask = mask

                    # Collect litter
                    if (nr, nc) in litter:
                        nmask |= 1 << litter[(nr, nc)]

                    # Reset energy
                    if classroom[nr][nc] == 'R':
                        ne = energy

                    state = (nr, nc, nmask)

                    # Only keep the state if it has more energy
                    if state not in seen or ne > seen[state]:
                        seen[state] = ne
                        q.append((nr, nc, ne, nmask))

            moves += 1

        return -1