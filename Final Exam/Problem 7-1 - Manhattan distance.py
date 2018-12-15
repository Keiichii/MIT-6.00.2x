# -*- coding: utf-8 -*-
"""
Created on Sat Dec 15 20:01:54 2018

@author: ART
"""

class person():
    def __init__(self, name, income, distance):
        self.name = name
        self.income = income
        self.distance = distance
        self.d_to = {}
        self.nearest = ()
        self.farthest = ()
        
    def calc_dist(self, p2):
        if self.name != p2.name:
            d = abs(self.distance - p2.distance)
            i = abs(self.income - p2.income)
            self.d_to[self.name+'-'+p2.name] = d+i
        
    def get_n_f(self):
#        print(self.d_to)
        for k,v in self.d_to.items():
#            print(k,v)
            if not self.nearest:
                self.nearest = self.farthest = (k, v)
            elif v < self.nearest[1]:
                self.nearest = (k, v)
            elif v > self.farthest[1]:
                self.farthest = (k, v)
        
incomes = [10, 30, 90, 100, 120, 60]
miles = [4, 10, 5, 1, 1, 6]
persons = []
for i in range(1, 7):
    persons.append(person('Person'+str(i), incomes[i-1], miles[i-1]))
#print(persons)

for p1 in persons:
    for p2 in persons:
        p1.calc_dist(p2)
        
nearest = {}
farthest = {}
for p in persons:
    p.get_n_f()
    nearest[p.nearest[0]] = p.nearest[1]
    farthest[p.farthest[0]] = p.farthest[1]
    
#print('nearest:', nearest, '\n')
#print('farthest:', farthest)

ans_n = []
near = min(list(nearest.values()))
for k,v in nearest.items():
    if v == near:
        ans_n.append(k)
        
ans_f = []
far = max(list(farthest.values()))
for k,v in farthest.items():
    if v == far:
        ans_f.append(k)

print('Two nearest:', ans_n[0], ans_n[1], '\n')
print('Two farthest:', ans_f[0], ans_f[1])
