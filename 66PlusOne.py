# -*- coding: utf-8 -*-
"""
Created on Wed Nov 28 15:24:33 2018

@author: 施腾芮
"""
digits = [2,4,9,3,9]
if digits[-1] != 9:
      digits[-1] = digits[-1] + 1
      print(digits)
elif digits.count(9) == len(digits):
      for i in range(len(digits)):
            digits[i] = 0
      digits.insert(0,1)
      print(digits)
else:
      for i in range(len(digits)):
            if digits[len(digits) - i - 1] != 9:
                  digits[len(digits) - i - 1] = digits[len(digits) - i - 1] + 1
                  break #如果用continue [2,4,9,3,9] 不能符合条件
            digits[len(digits) - i - 1] = 0
      print(digits)