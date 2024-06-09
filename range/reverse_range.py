s1="qweertyu"
s2="123456789"
if len(s2)<len(s1):
    for i in range(len(s2)):
        s3=s1[i]+s2[i]
        print(s3)
else:
    for i in range(len(s1)):
        s3=s1[i]+s2[i]
        print(s3)
    
