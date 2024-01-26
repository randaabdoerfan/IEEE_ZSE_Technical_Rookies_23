# -*- coding: utf-8 -*-
"""TASK_4_prob_2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1z7ZCiffontEDXa1oQxALVxDy9UiZztmV
"""

s1 =str(input())
s2 =str(input())
def isSubSequence(s1, s2, m, n):
    if m == 0:
        return True
    if n == 0:
        return False
    if s1[m-1] == s2[n-1]:
        return isSubSequence(s1, s2, m-1, n-1)
    return isSubSequence(s1, s2, m, n-1)

if isSubSequence(s1, s2, len(s1), len(s2)):
    print ("true")
else:
    print ("False")