class Solution:  # Define the solution class for LeetCode
    def multiply(self, num1: str, num2: str) -> str:  # Define the multiply function that takes two strings
        if num1 == "0" or num2 == "0":  # Check if either number is zero
            return "0"  # If yes, the product is zero

        m = len(num1)  # Store the length of the first number
        n = len(num2)  # Store the length of the second number
        result = [0] * (m + n)  # Create an array to store the product digits

        for i in range(m - 1, -1, -1):  # Loop through num1 from right to left
            digit1 = int(num1[i])  # Convert the current character of num1 to an integer

            for j in range(n - 1, -1, -1):  # Loop through num2 from right to left
                digit2 = int(num2[j])  # Convert the current character of num2 to an integer
                product = digit1 * digit2  # Multiply the two digits

                p1 = i + j  # Index for the carry position in result
                p2 = i + j + 1  # Index for the current digit position in result

                total = product + result[p2]  # Add the product to the existing value at p2
                result[p2] = total % 10  # Store the single digit at p2
                result[p1] += total // 10  # Add the carry to the left position

        start = 0  # Initialize pointer to skip leading zeros

        while start < len(result) and result[start] == 0:  # Skip all leading zeros
            start += 1  # Move to the next digit

        return "".join(str(digit) for digit in result[start:])  # Convert remaining digits to string and return