class Solution:
    def maxNumberOfApples(self, weight: List[int]) -> int:
# Want to get the most apples, so need to sort asending
# Can then iterate through the sorted list until all apples fit or when basket is at max weight
        weight.sort()
        basket_capacity = 5000
        apples = 0
        
        for apple in weight:
            if apple <= basket_capacity:
                basket_capacity = basket_capacity - apple
                apples += 1
            else:
                return apples
        
        return apples