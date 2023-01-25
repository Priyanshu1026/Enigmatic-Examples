number_of_tests=int(input())
for i in range(number_of_tests):
    int(input())
    string=input()
    count=0
    for j in string:
        if j=='Q':
            count+=1
        else:
            count=max(0,count-1)
    if count==0:
        print("Yes")
    else:
        print("No")
