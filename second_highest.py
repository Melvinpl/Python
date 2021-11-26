
n = int(input("Number of integer : "))
arr = map(int, input("Numbers : ").split())

arr_list = list(arr)
maxi = max(arr_list)
arr_list_new =[]

for i in range(0, n):
    if arr_list[i] < maxi:
        arr_list_new.append(arr_list[i])

sec_maxi = max(arr_list_new)
print(sec_maxi)