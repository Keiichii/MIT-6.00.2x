def max_contig_sum(L):
    """ L, a list of integers, at least one positive
    Returns the maximum sum of a contiguous subsequence in L """
    ans = L[0]
    end = None
    start = None
    tmp = None
    stop = None
    for i in range(len(L)):
        if L[i] > 0 and start == None:
            start = i
            end = None
        elif L[i] < 0:
            if i+1 < len(L) and L[i+1]>0:
                end = i+1
            else:
                end = i-1
            stop = True
        if i+1 == len(L) and L[i] > 0:
            end = i
        if start != None and end !=None:
            tmp = sum(L[start:end+1])
            if tmp > ans:
                ans = tmp
        if stop:
            start = None
            end = None
            stop = None
    return ans
    
L = [[1], [1, -1], [10, 9, 8, -1], [-2, 6, 8, 10], [5, -7, 1], [0, -2, -5, -1, 5],
    [-3, -2, 1, -1, -5],
    [3, 4, -1, 5, -4],
    [3, 4, -8, 15, -1, 2],
    [3, 4, -8, 3, 3, 1, -7, 15, -1, 2],
    [0, -2, -7, 3, 3, -7, 15, 2],
    [3, -3, 3, -3]
    ]
for l in L:
    print(max_contig_sum(l))
    
#s = l2[:-2]
#a = sum(l2[:-2])
#b = sum(l2[3:])
    