import datetime
class Solution:
    def daysBetweenDates(self, date1: str, date2: str) -> int:
        date_obj1 = datetime.date.fromisoformat(date1)
        date_obj2 = datetime.date.fromisoformat(date2)

        diff = date_obj1 - date_obj2

        return abs(diff.days)