class Solution:
    def __init__(self) -> None:
        self.map = {'2':['a','b','c'],
                '3':['d','e','f'],
                '4':['g','h','i'],
                '5':['j','k','l'],
                '6':['m','n','o'],
                '7':['p','q','r','s'],
                '8':['t','u','v'],
                '9':['w','x','y','z']}
        self.sol = []
        self.test = []
    def letterCombinations(self, digits: str):
        for number in digits:
            self.test.append(self.map[number])
        self.comb('',self.test)
        return self.sol
    
    def comb(self,output,test):
        if len(test) == 0:
            self.sol.append(output)
        else:
            t1 = test[0]
            t2 = test[1:]
            for ch in t1:
                self.comb(output+ch,t2)


a = Solution()

print(a.letterCombinations("23"))

# map = {'2':['a','b','c'],
#         '3':['d','e','f'],
#         '4':['g','h','i'],
#         '5':['j','k','l'],
#         '6':['m','n','o'],
#         '7':['p','q','r','s'],
#         '8':['t','u','v'],
#         '9':['w','x','y','z']}
# test = []
# dig = '234'
# for number in dig:
#     test.append(map[number])

# def comb(output,test,sol):
#     if len(test) == 0:
#         sol.append(output)
#     else:
#         t1 = test[0]
#         t2 = test[1:]
#         for ch in t1:
#             comb(output+ch,t2,sol)
# sol = []
# comb("",test,sol)
# print(len(sol))


print('a'+chr(1 ))