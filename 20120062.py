count =0
for i in range(0,8):
    line=raw_input()
    if i%2==0:
        for j in range(0,8):
            if j%2==0:
                if line[j]=='F':
                    count=count+1
    elif i%2==1:
        for j in range(0,8):
            if j%2==1:
                if line[j]=='F':
                    count=count+1
print count