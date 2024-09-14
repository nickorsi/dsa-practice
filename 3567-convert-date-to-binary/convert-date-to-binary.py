class Solution:
    def convertDateToBinary(self, date: str) -> str:
        return "-".join([format(int(e), "b") for e in date.split("-")])