def FacNum(n):
    if n == 0:
        return 0
    else:
         n = n + FacNum(n - 1)


FacNum(5)
