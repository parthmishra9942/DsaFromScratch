class Solution:
    def moreFrequent(self, arr, x, y):
        count_x = 0
        count_y = 0

        for num in arr:
            if num == x:
                count_x += 1
            if num == y:
                count_y += 1

        if count_x > count_y:
            return x
        elif count_y > count_x:
            return y
        else:
            return min(x, y)