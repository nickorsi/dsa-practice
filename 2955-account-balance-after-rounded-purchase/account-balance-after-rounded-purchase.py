import math
class Solution:
    def accountBalanceAfterPurchase(self, purchaseAmount: int) -> int:
        if purchaseAmount % 5 == 0:
            rounded_purchase = math.ceil(purchaseAmount / 10) * 10
        else:
            rounded_purchase = round(purchaseAmount, -1)

        return 100 - rounded_purchase