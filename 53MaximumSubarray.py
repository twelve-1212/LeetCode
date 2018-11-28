# -*- coding: utf-8 -*-
"""
Created on Tue Nov 27 20:38:41 2018

@author: 施腾芮
"""

nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
smax = nums[0]
cmax = 0
for num in nums:
      cmax = cmax + num
      if cmax > smax:
            smax = cmax
      if cmax < 0:
            cmax = 0
            continue
print(smax)