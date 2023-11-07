#Remove a from string using recursion
#baccad
def remove_a(string):
    ch = ""
    if len(string)==1:
        if string == "a":
            return ""
        else :
            return string 
    if string[0] != "a":
        ch = string[0]
    return ch+remove_a(string[1:])

# print(remove_a("aflkjdshfalkjsdhfaldsjf"))

#If starts eith apple skip full -> can use inbuilt str.startswith("apple") -> then substring[5:]