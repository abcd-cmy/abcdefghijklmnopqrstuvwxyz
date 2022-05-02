queue = [300,500,200,300]
n = 1000
for i in range(0,len(queue)):
    print('packet -',queue[i])
    if n>queue[len(queue)-1]:
        n = n - queue[i]
        print('',n)
        print('packet-',queue[i],'sent')
    else:
        n = 1000
        print('initalized back to 1000')