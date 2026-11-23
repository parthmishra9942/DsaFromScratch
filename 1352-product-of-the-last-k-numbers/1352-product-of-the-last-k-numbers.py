class ProductOfNumbers:
    def __init__(self):
        """
        Initialize the data structure.
        Maintains a prefix product array starting with 1.
        """
        # Prefix product array - stores cumulative products
        # Starting with 1 allows for easier calculation of products
        self.prefix_products = [1]

    def add(self, num: int) -> None:
        """
        Add a number to the stream.
      
        Args:
            num: The number to add to the stream
          
        If num is 0, reset the prefix products array since any product 
        containing 0 will be 0.
        Otherwise, append the cumulative product.
        """
        if num == 0:
            # Reset the array when encountering 0
            # Any product containing 0 will be 0
            self.prefix_products = [1]
            return
      
        # Append the cumulative product
        # New product = last cumulative product * current number
        self.prefix_products.append(self.prefix_products[-1] * num)

    def getProduct(self, k: int) -> int:
        """
        Return the product of the last k numbers in the stream.
      
        Args:
            k: Number of recent elements to multiply
          
        Returns:
            The product of the last k numbers, or 0 if any of them is 0
        """
        # If we don't have k elements in our prefix array,
        # it means there was a 0 in the last k elements
        if len(self.prefix_products) <= k:
            return 0
      
        # Calculate product of last k elements using prefix products
        # Product = (product of all elements) / (product of elements before the last k)
        return self.prefix_products[-1] // self.prefix_products[-k - 1]


# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)
