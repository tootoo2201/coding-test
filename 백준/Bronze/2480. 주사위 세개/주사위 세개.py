f,s,t = map(int,input().split())

if(f==s==t):
    result = 10000 + f*1000
elif(f==s!=t):
    result = 1000 + f*100
elif(f!=s==t):
    result = 1000 + s*100
elif(f==t!=s):
    result = 1000 + t*100
elif(f!=s!=t):
    result = max(f,s,t)*100

print(result)