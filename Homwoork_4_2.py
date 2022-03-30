import random
nuv_s = []
for i in range(30):
    nuv_s.append((random.randint(0, 10)))
print(nuv_s)

ans_s = []
for i in range(len(nuv_s)-1):
    if nuv_s[i]<nuv_s[i + 1]:
        ans_s.append((nuv_s[i + 1]))
print((ans_s))
