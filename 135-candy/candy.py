class Solution(object):
    def candy(self, ratings):
        """
        :type ratings: List[int]
        :rtype: int
        """
        n = len(ratings)
        # Every child must have at least one candy
        candies = [1] * n
        
        # Left-to-Right Pass: Ensure child gets more than left neighbor if rating is higher
        for i in range(1, n):
            if ratings[i] > ratings[i - 1]:
                candies[i] = candies[i - 1] + 1
        
        # Right-to-Left Pass: Ensure child gets more than right neighbor if rating is higher
        # We use max() to ensure we don't break the condition set in the first pass
        for i in range(n - 2, -1, -1):
            if ratings[i] > ratings[i + 1]:
                candies[i] = max(candies[i], candies[i + 1] + 1)
        
        # The sum of the array is the minimum total candies required
        return sum(candies)