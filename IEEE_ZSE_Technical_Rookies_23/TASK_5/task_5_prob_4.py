# -*- coding: utf-8 -*-
"""TASK_5_prob_4.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1z7ZCiffontEDXa1oQxALVxDy9UiZztmV
"""

def primeFactors(num):
	x = 2
	while(num > 1):
		if(num % x == 0):
			print(x, end=" ")
			num = num / x
		else:
			x = x + 1
num=int(input())
primeFactors(num)