class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return "1"
        elif n == 2:
            return "11"
        else:
            previous = self.countAndSay(n - 1)
            print("i = {}, ans = {}".format(n - 1, previous))
            answer = ""
            preceding_digit = previous[0]
            counter = 1
            for digit in previous[1:]:
                print("digit = {}, prec = {}".format(digit, preceding_digit))
                if digit == preceding_digit:
                    counter += 1
                else:
                    answer += "{}{}".format(counter, preceding_digit)
                    counter = 1
                    preceding_digit = digit
            answer += "{}{}".format(counter, preceding_digit)
            return answer


print([Solution().countAndSay(x) for x in range(1, 10)])
