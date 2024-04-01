class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
#   Given an array of arrays, where the first value is the winner and second id the loser
#   Return array of two arrays, first array reps all players losing no matches, second array representing players losing exactly 1 match
#   Create outcomeTracker as a dict
        outcome_tracker: dict[int, int] = {}
#   Create no_loss and one_loss as arrays of int
        no_loss: list[int] = []
        one_loss: list[int] = []
#   Iterate through array
        for match in matches:
#       if 1st element doesn't exist in outcomeTracker, create with value 1
            if match[0] not in outcome_tracker:
                outcome_tracker[match[0]] = 1
#       if 2nd element doesn't exist in outcomeTracker, create with value 0
            if match[1] not in outcome_tracker:
                outcome_tracker[match[1]] = 0
#       else decrement 2nd element value in outcomeTracker by 1
            else:
                outcome_tracker[match[1]] -= 1
#   Iterate through outcomeTracker
        for player in outcome_tracker:
#       if value is 1, push into no_loss array
            if outcome_tracker[player] == 1:
                no_loss.append(player)
#       if value is 0, push into one_loss array
            if outcome_tracker[player] == 0:
                one_loss.append(player)
#   Return [no_loss, one_loss] after sorting
        no_loss.sort()
        one_loss.sort()
        return [no_loss, one_loss]