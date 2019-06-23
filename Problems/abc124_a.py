
#input:A B
A,B=map(int,input().split())

#判定
max_value=0
if A!=B:
    lerger=max(A,B)
    max_value=lerger+(lerger-1)

else:
    max_value=A+A


print('{}'.format(max_value))