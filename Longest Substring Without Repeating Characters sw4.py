s=input()
left=0
right=0
seen=set()
maxlen=0
n=len(s)
while(right<n):
    while(s[right] in seen):
        seen.remove(s[left])
        left += 1
    seen.add(s[right])
    maxlen = max(maxlen, right - left + 1)
    right += 1
print(maxlen)



