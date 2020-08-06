import itertools
def findsubsets(S,m):
    return list(itertools.combinations(S, m))

def find_gcd(x, y): 
   while(y): 
       x, y = y, x % y 
  
   return x


S = [2,3,4,5]
m = 3
sub = []
for i in range(2, len(S)+1) :
    sub.append((findsubsets(S, i)))

tmp = []
for i in range(len(sub)) :
    for j in range(len(sub[i])) :
        tmp.append(list(sub[i][j]))
        
cnt = 0
for i in range(len(tmp)) :
    for j in range(len(tmp[i])) :
        if len(tmp[i]) > 2 :
            num1 = tmp[i][0] 
            num2 = tmp[i][1] 
            gcd = find_gcd(num1, num2) 
  
            for i in range(2, len(tmp[i])): 
                gcd = find_gcd(gcd, tmp[i][j])
        else :
            gcd = find_gcd(tmp[i][0], tmp[i][1])
        
    if gcd==1 :
        cnt+=1
print(cnt)