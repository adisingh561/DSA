def permutations(output,input,final):
    if len(input) == 0:
        final.append(output)
        return
    else:
        ch = input[0]
        input= input[1:]
        for i in range(len(output)+1):
            left = output[:i]
            right = output[i:]
            permutations(left+ch+right,input,final)

final = []
permutations('','abc',final)
print(final)