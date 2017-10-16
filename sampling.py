#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 15 13:37:16 2017

@author: mathias
"""

def spiralPrintArray(array_of_arrays):
    result_list = []
    coordinateY, coordinateX = 0, 0
    result_list.append(array_of_arrays[coordinateY][coordinateX])
    cordY_min, cordY_max = 0, len(array_of_arrays) - 1
    cordX_min, cordX_max = 0, len(array_of_arrays[0]) - 1
    result_max_length = len(array_of_arrays) * len(array_of_arrays[0])

    while len(result_list) < result_max_length:
        while coordinateX < cordX_max and len(result_list) < result_max_length:
            coordinateX += 1
            result_list.append(array_of_arrays[coordinateY][coordinateX])
        cordY_min += 1

        while coordinateY < cordY_max and len(result_list) < result_max_length:
            coordinateY += 1
            result_list.append(array_of_arrays[coordinateY][coordinateX])
        cordY_max -= 1

        while coordinateX > cordX_min and len(result_list) < result_max_length:
            coordinateX -= 1
            result_list.append(array_of_arrays[coordinateY][coordinateX])
        cordX_max -= 1

        while coordinateY > cordY_min and len(result_list) < result_max_length:
            coordinateY -= 1
            result_list.append(array_of_arrays[coordinateY][coordinateX])
        cordX_min += 1
    return result_list

#  print(spiralPrintArray([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16],[17,18,19,20]]))

import math

def imageSmoother(two_D_array):
    result = [[None] * len(two_D_array[0]) for i in two_D_array]

    for array in range(len(two_D_array)):
        for value in range(len(two_D_array[0])):
            total, count = 0, 0
            for i in range(max(value-1, 0), min(len(two_D_array[0]), value+2)):
                for j in range(max(array-1, 0), min(len(two_D_array), array+2)):
                    total, count = total + two_D_array[j][i], count + 1
            result[array][value] = math.floor(total/count)
    return result

example = [[1,1,1],[1,0,1],[1,1,1]]
#  print(imageSmoother(example))

