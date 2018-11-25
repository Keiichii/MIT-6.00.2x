def greedySum(L, s):
    sumL = sum(L)
    m = []
    temp = s
    for i in L:
        if i <= temp:
            m_temp = temp//i
            m.append(m_temp)
            temp -= i*m_temp
        else:
            m.append(0)
        
    print('List of multipliers:', m)
    new_sum = 0
    for x in range(len(L)):
        new_sum += L[x]*m[x]
    print('new sum:', new_sum, '|| s:', s)
    if new_sum == s:
        return sum(m)
    else:
        return "no solution"
    
L = [9,8,7]
s = 16
print(greedySum( [10, 7, 6, 3], 19))