map = {'2':['a','b','c'],
                '3':['d','e','f'],
                '4':['g','h','i'],
                '5':['j','k','l'],
                '6':['m','n','o'],
                '7':['p','q','r','s'],
                '8':['t','u','v'],
                '9':['w','x','y','z']}

digits = "29"
#output = ["ad","ae","af","bd","be","bf","cd","ce","cf"]
final_output = []

def get_combination(digits,i,output):
    if i == len(digits):
        final_output.append(output)
    else:
        v = map[digits[i]]
        for letter in v:
            get_combination(digits,i+1,output= output+letter)

get_combination(digits,0,'')

print(final_output)