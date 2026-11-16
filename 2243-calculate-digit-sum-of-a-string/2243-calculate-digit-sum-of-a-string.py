class Solution:  # Define the solution class as required by LeetCode
    def digitSum(self, s: str, k: int) -> str:  # Define the function that returns the final string
        while len(s) > k:  # Keep processing rounds while the string is longer than k
            new_s = ""  # Create a new string for the next round

            for i in range(0, len(s), k):  # Move through the string in steps of k
                group = s[i:i + k]  # Take a chunk of size k from the string
                group_sum = 0  # Initialize the sum for the current group

                for ch in group:  # Loop through each character in the group
                    group_sum += int(ch)  # Convert the digit to int and add it to the sum

                new_s += str(group_sum)  # Append the group sum as a string to the new result

            s = new_s  # Update s to the newly formed string for the next round

        return s  # Return the final string after all rounds are done