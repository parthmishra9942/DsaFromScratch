class Solution:
    def checkOverlap(self, radius, xCenter, yCenter, x1, y1, x2, y2):
        # Find the closest point on the rectangle to the circle's center
        closestX = max(x1, min(xCenter, x2))
        closestY = max(y1, min(yCenter, y2))

        # Calculate squared distance
        dx = xCenter - closestX
        dy = yCenter - closestY

        # Check if the closest point lies inside or on the circle
        return dx * dx + dy * dy <= radius * radius