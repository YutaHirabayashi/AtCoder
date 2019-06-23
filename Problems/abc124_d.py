
#input 
N,K=map(int,input().split())
S=input() #str

#s[j-1]=0,s[j]=1もしくはs[j-1]=1,s[j]=0になっているjをリストにしたものをiとする（スタート地点かつエンド地点候補）
i=[0]
for j in range(1,len(S)):
    if S[j]!=S[j-1]:
        i.append(j)

#スタート地点候補iに対して、
#s[i[m]]==1の場合、変更可能な変化点は2K個なので,その次の変化点までが求める文字数となり,X=i[2K+1+m]-i[m]
#s[i[m]]==0の場合、変更可能な変化点は2K-1個なので,その次の変化点までが求める文字数となり,X=i[2K+m]-i[m]

X=[]
for m in range(len(i)):
    if S[i[m]]=='1':
        #はみ出している->右方向は全て置換可能
        if 2*K+1+m >= len(i):
            X.append(N-i[m])
        else:
            X.append(i[2*K+1+m]-i[m])

    elif S[i[m]]=='0':
        #はみ出している->右方向は全て置換可能
        if 2*K+m >= len(i):
            X.append(N-i[m])
        else:
            X.append(i[2*K+m]-i[m])

print(max(X))
