def backtrack(i):#global allows functions to handle variables outside of functions
    global bestV, curW, curV, x, bestx
    if i >= n:
        if bestV < curV:
            bestV = curV
            bestx = x[:]
    else:
        if curW + w[i] <= c:
            x[i] = True
            curW += w[i]
            curV += v[i]
            backtrack(i + 1)
            curW -= w[i]
            curV -= v[i]
        x[i] = False
        backtrack(i + 1)


if __name__ == '__main__':
    n = 5
    c = 10
    w = [2, 2, 6, 5, 4]
    v = [6, 3, 5, 4, 6]
    x = [False for i in range(n)]
    backtrack(0)
    print(bestV)
    print(bestx)