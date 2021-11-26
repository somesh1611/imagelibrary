s1='abc'
s2='fsgetcccaueioe'
l1=len(s1)
s3="".join(sorted(s1))
print(s3)
for i in range(len(s2)):
    if s2[i] in s3:
        x="".join(sorted(s2[i:i+l1]))
        print(x)
        if x==s3:
            print("True")
            break
else:
    print("False")


#Working for smaller inputs.