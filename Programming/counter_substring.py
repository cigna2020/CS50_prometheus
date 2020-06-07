class CombStr(str):
    def __init__(self, string):
        self.string = string

    def count_substrings(self, length):
        self.length = length
        if self.length == '':
            return None
        if self.length == 0:
            return 0
        alent = 0
        lent = []

        while self.length < len(self.string) + 1:
            if self.string[alent:self.length] not in lent:
                lent.append(self.string[alent:self.length])
            alent += 1
            self.length += 1
        return len(lent)

# s0 = CombStr('qqqqqqweqqq%')
# print(s0.count_substrings(0)) # 0
# print(s0.count_substrings(1)) # 4