def maxArea(a,len)  :
    area = 0
    for i in range (len) :
        for j in range(i + 1,len)  :
            area = max(area, min(a[j],a[i])*(j-i))
        return area
    a=[1,5,4,3]
    len1 = len(a)
    print(maxarea(a,  len1))
