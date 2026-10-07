class Solution:
    def removeInvalidParentheses(self, s):
        
        def is_valid(string):
            balance = 0

            for ch in string:
                if ch == '(':
                    balance += 1

                elif ch == ')':
                    balance -= 1

                    if balance < 0:
                        return False

            return balance == 0

        # BFS
        queue = [s]
        visited = set([s])

        while queue:
            valid = []

            # Check current level
            for string in queue:
                if is_valid(string):
                    valid.append(string)

            # If valid strings found, minimum removals achieved
            if valid:
                return valid

            # Generate next level
            next_queue = []

            for string in queue:
                for i in range(len(string)):

                    # Only remove parentheses
                    if string[i] not in "()":
                        continue

                    new_string = string[:i] + string[i + 1:]

                    if new_string not in visited:
                        visited.add(new_string)
                        next_queue.append(new_string)

            queue = next_queue