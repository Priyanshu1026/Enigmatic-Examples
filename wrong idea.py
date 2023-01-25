number_of_tests=int(input())
for i in range(number_of_tests):
    int(input())
    string=input()
    if string.count('Q')<=string.count('A') and string[-1]!='Q':
        print('Yes')
    else:
        print('No')
