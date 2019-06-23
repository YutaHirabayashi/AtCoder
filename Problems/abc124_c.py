
#input S
S=input()

count=0
for i in range(1,len(S)):
    if S[i]==S[i-1]:
        if S[i]=='0':
            S=S[:i]+'1'+S[i+1:]
        else:
            S=S[:i]+'0'+S[i+1:]
        count=count+1

print(count)

