def remove_a(output,input):
    if len(input)==0:
        print(output) 
    else:
        if input[0] != 'a':
            output+=input[0]
            input = input[1:]
            remove_a(output,input)
        else:
            input = input[1:]
            remove_a(output,input)
remove_a(output = "",input="bacacad")

#Now if we want to return a string 
#Here we can have something like rem_apple -> so essentially if string starts with apple ie s[:5] == 'apple' 
def rem_a(input):
    if len(input)==0:
        return ""
    ch = input[0]
    if ch == 'a':
        return rem_a(input[1:])
    else :
        return ch + rem_a(input[1:])

print(rem_a("baccad"))