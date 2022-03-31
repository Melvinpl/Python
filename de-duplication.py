input = [1,0,1,0,0,0,0,1,1,0,0,1,1]
output =[input[0]]

for n in range(0,len(input)-1):
    if input[n+1] != input[n]:
        output.append(input[n+1])
print(output)
