class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # Using top down dp
        # Need to determine dimension, recurence relation, and base case
            # Only care about location i? 
            # Recurrence relation
                # At i = 0, length = 1
                # At i = 1, length = length at 0 + 1 if current value is greater than previous
                # At i = 2, length = length at 1 + 1 if current value is greater than previous 
                # if nums[i] > nums[i -1] then 1 + dp(i-1), else dp(i-1)
            # Base case
                # i == 0 return 1
        # memo: Dict[int, int] = {}
        # n = len(nums) - 1
        # max_seen:int = -math.inf

        # def dp(i: int) -> int:
        #     nonlocal max_seen
        #     # print("i state = ", i)
        #     if i == 0:
        #         return 1

        #     if i in memo:
        #         return memo[i]
            
        #     memo[i] = dp(i-1)

        #     if nums[i] > nums[i-1] and nums[i] >= max_seen:
        #         max_seen = nums[i]
        #         memo[i] += 1

        #     # else:
        #     #     for j in range(i-2,-1, -1):
        #     #         # print("i= ", i)
        #     #         # print("j= ", j)
        #     #         # print("memo= ", memo)
        #     #         if nums[i] >= nums[j]:
        #     #             break
        #     #         else:
        #     #             if memo[i] > 1:
        #     #                 memo[i] -= 1
        #     #             else: 
        #     #                 break

        #     return memo[i]
        
        # ans = dp(n)
        # print("memo= ", memo)
        # return dp(n)
        # Above doesn't work, but some of the pieces are correct
        # memo: Dict[int, int] = {}

        # def dp(i: int) -> None:
        #     ans = 1
        #     if i == 0: 
        #         return ans

        #     if i in memo:
        #         return memo[i]
            
        #     for j in range(i):
        #         if nums[i] > nums[j]:
        #             ans = max(ans, dp(j) + 1)

        #     return ans

        # all_ans: List[int] = []

        # for i in range(len(nums)):
        #     all_ans.append(dp(i))

        # return max(all_ans)
        # Above times out, the below does not for some reason
        @cache
        def dp(i):
            ans = 1 # Base case

            # Recurrence relation
            for j in range(i):
                if nums[i] > nums[j]:
                    ans = max(ans, dp(j) + 1)
            
            return ans

        return max(dp(i) for i in range(len(nums)))