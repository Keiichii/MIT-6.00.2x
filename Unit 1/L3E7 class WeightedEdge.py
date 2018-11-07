# -*- coding: utf-8 -*-
"""
Created on Wed Nov  7 22:49:11 2018

@author: ART
"""

class WeightedEdge(Edge):
    def __init__(self, src, dest, weight):
        Edge.__init__(self, src, dest)
        self.weight = weight
    def getWeight(self):
        return self.weight
    def __str__(self):
        return self.src.getName() + '->' + self.dest.getName() \
            + ' (' + str(self.getWeight()) + ')'
