# -*- coding: utf-8 -*-
"""TASK_5_prob_3.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1z7ZCiffontEDXa1oQxALVxDy9UiZztmV
"""

def sumDigitSquare(n) :
	sq = 0
	while (n) :
		digit = n % 10
		sq = sq + digit * digit
		n = n // 10
	
	return sq
def SavedZarzorLife(n) :
	while (1) :
		if (n == 1) :
			return True
		n = sumDigitSquare(n)
		if (n == 4) :
			return False
	
	return False
n=int(input())
if (SavedZarzorLife(n)) :
	print("True")
else :
	print("Flase")

def sumDigitSquare(n) :
	sq = 0
	while (n) :
		digit = n % 10
		sq = sq + digit * digit
		n = n // 10
	
	return sq
def SavedZarzorLife(n) :
	while (1) :
		if (n == 1) :
			return True
		n = sumDigitSquare(n)
		if (n == 4) :
			return False
	
	return False
n=int(input())
if (SavedZarzorLife(n)) :
	print("True")
else :
	print("Flase")