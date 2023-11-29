import copy
#Find all up/ subsrting 
def helper(output,string,array):
    if len(string)==0:
        array.append(output)
        return
    helper(output+string[0],string[1:],array)
    helper(output,string[1:],array)
def sub_string(string):
    array = []
    output = ''
    helper(output,string,array)
    print(array)
# sub_string("abc")

#ASCII value of a character use ord()
# print(ord("A"))

#Substring/Subarray using iteration
#[1,2,3]
def sub_array(val):
    sol = [[]]
    for values in val:
        for j in range(len(sol)):
            temp = copy.deepcopy(sol[j])
            temp.append(values)
            sol.append(temp)
    return sol

print(sub_array([1,2,3]))

final =[]
def all_subset(output,input,final):
    if len(input) == 0:
        if output != '':
            final.append(output)
    else:
        char = input[0]
        #take char
        all_subset(output+char,input[1:],final)
        #Ignore char
        all_subset(output,input[1:],final)
# all_subset('','abc',final)
# print(final)

