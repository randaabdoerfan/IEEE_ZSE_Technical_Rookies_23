# -*- coding: utf-8 -*-
"""task_4_prob_6.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1LYqTDEYLcqHYyJ8a7-_4pveloMdu8TJq
"""

num=int(input())
num_before=num
def reversed(num) :
  reversed_num = 0
  while num != 0:
    digit = num % 10
    reversed_num = reversed_num * 10 + digit
    num //= 10
    sub=num_before - reversed_num
  return sub
reversed(num)