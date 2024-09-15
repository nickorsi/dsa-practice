class MyCalendar:

    def __init__(self):
        self.bookings: List[List[int]] = []

    def book(self, start: int, end: int) -> bool:
        if len(self.bookings) == 0: 
            self.bookings.append([start, end])
            return True
        else:
            opening = 0
            for meeting_slot in range(len(self.bookings)):
                # print(self.bookings)
                scheduled_start, scheduled_end = self.bookings[meeting_slot]
                if start >= scheduled_start and start < scheduled_end:
                    return False
                if start < scheduled_start and end > scheduled_start:
                    return False
                if meeting_slot == len(self.bookings) - 1:
                    if start >= scheduled_end:
                        self.bookings.append([start, end])
                        return True
                if end <= scheduled_start:
                    opening = meeting_slot
                    break
            self.bookings = [*self.bookings[0:opening], [start, end], *self.bookings[opening:]]
            return True
            


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)