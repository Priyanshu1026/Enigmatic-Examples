number_of_testcases=int(input())
for i in range(number_of_testcases):
    int(input())
    string=input()
    while 'QA' in string:
        string=string.replace('QA','')
    if 'Q' in string:
        print("No")
    else:
        print("Yes")
