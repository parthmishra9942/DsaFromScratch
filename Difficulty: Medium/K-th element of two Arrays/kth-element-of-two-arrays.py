class Solution:
    def kthElement(self, a, b, k):
        n = len(a)
        m = len(b)
    
        # Always binary search on the smaller array
        if n > m:
            return self.kthElement(b, a, k)
    
        low = max(0, k - m)
        high = min(k, n)
    
        while low <= high:
            x = (low + high) // 2
            y = k - x
    
            # Boundary values
            aLeft = float('-inf') if x == 0 else a[x - 1]
            aRight = float('inf') if x == n else a[x]
    
            bLeft = float('-inf') if y == 0 else b[y - 1]
            bRight = float('inf') if y == m else b[y]
    
            # Correct partition
            if aLeft <= bRight and bLeft <= aRight:
                return max(aLeft, bLeft)
    
            # Too many elements taken from a
            elif aLeft > bRight:
                high = x - 1
    
            # Too few elements taken from a
            else:
                low = x + 1