def max_stock_profit(trading_info):
    """given list of trading values where indices are minutes
        past opening time and values is stock price, determine
        when best time is to buy and sell. Must sell after buy."""
    best_profit = None

    for price in range(len(trading_info)-1):
        potential = - trading_info[price] + max(trading_info[price+1:])
        # find best profit
        if best_profit == None or potential > best_profit:
            best_profit = potential
    return best_profit


# Interview Question 2
# given an array of arbitrary number of arrays, all of the same lenght.
# elements are all intergers. print elements in a spiral fashion starting at [0][0]

example_1 = [[1,2,3,4],
             [5,6,7,8],
             [9,10,11,12],
             [13,14,15,16]]
# output should be: [1,2,3,4,8,12,16,15,14,13,9,5,6,7,11,10]

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

#  print(spiralPrintArray(example_1))


# LeetCode Contest 8/19
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
