def parity():
    c = 0
    data = input('enter the binary code')
    s = list(data)
    for i in range (len(s)):
        if(s[i]=='1'):
            c+=1
    print(c)
    if(c%2==0):
        print('even parity')
    else:
        print('odd parity')
parity()

