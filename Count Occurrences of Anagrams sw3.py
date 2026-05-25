from collections import Counter
s=input()
p=input()
count=0
left=0
right=0
k=len(p)
window=Counter()
pattern=Counter(p)
n=len(s)
while(right<n):
    window[s[right]]+=1
    if(right-left+1<k):
        right+=1
    elif(right-left+1==k):
        if(window==pattern):
            count+=1
        window[s[left]]-=1
        if(window[s[left]]==0):
            del window[s[left]]
        left+=1
        right+=1
print(count)            