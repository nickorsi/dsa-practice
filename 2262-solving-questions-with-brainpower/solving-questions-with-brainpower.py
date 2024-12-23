class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        # Try using top down dp
        # Identify the equation dimension and what it will return
            # 1-d(?) and will return int for the max points earned
        # Identify the recurence relation
            # If at index 0 then just return the points
            # If at index 1 then max of
                # Points at 0
                # Points at 1
            # If at index 2 then must determine if
                # i > i - 2 + question[i - 2][1]
                    # Then max question[i] + question[i-2], question[i-1]
                # Else
                    # max question[i], question[i-2], question [i-1]
        # Identify base case
            # i == 0 then return question[i][0]
            # i == 1 then return max question[i][0], question[i-1][0]

        # memo: Dict[int, int] = {}

        # def dp(i: int) -> int:
        #     print("i= ", i)
        #     print("memo= ", memo)

        #     if i in memo:
        #         return memo[i]
            
        #     max_pts = questions[i][0]
        #     print("max_pts= ", max_pts)

        #     for j in range(i):
        #         if i > j + questions[j][1]:
        #             print("Here")
        #             max_pts = max(max_pts, questions[i][0] + dp(j))
        #         else:
        #             max_pts = max(max_pts, dp(j))
            
        #     memo[i] = max_pts

        #     print("max_pts= ", max_pts)
        #     return memo[i]

        # # return max(dp(i) for i in range(len(questions)))
        # ans = 0
        # for i in range(len(questions)):
        #     print("\n")
        #     print("start i = ", i)
        #     print("\n")
        #     ans = max(ans, dp(i))
        # # print(memo)
        # return ans

        # Above gets the wrong answer on test case 27, unsure where break in logic is
        # Below is from training course, take odd approach of starting at bottom and looking forward to get the next answer
        
        # memo: Dict[int, int] = {}

        # def dp(i: int) -> int:
        #     if i >= len(questions):
        #         return 0

        #     if i in memo: 
        #         return memo[i]

        #     j = i + questions[i][1] + 1

        #     memo[i] = max(questions[i][0] + dp(j), dp(i + 1)) # Is it better to take the current points plus the next available points or to skip and take next points

        #     return memo[i]
        
        # return dp(0)

        # Bottom Up Approach

        dp = [questions[i][0] for i in range(len(questions))]

        for i in range(len(questions) - 1, -1, -1):
            points, skip = questions[i]
            j = i + skip + 1

            if j < len(questions):
                dp[i] = max(points + dp[j], dp[i + 1])
            elif i + 1 < len(questions):
                dp[i] = max(points, dp[i + 1])
            else:
                dp[i] = points
        
        return dp[0]