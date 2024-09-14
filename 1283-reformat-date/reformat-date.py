import datetime
class Solution:
    def reformatDate(self, date: str) -> str:
        date_list = date.split(" ")
        day_list = list(date_list[0])
        if len(day_list) == 4:
            date_list[0] = day_list[0] + day_list[1]
        else:
            date_list[0] = "0" + day_list[0]

        formatted_date = " ".join(date_list)

        date_obj = datetime.datetime.strptime(formatted_date, "%d %b %Y")

        return date_obj.strftime("%Y-%m-%d")