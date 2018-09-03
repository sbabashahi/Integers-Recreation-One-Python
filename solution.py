#Divisors of 42 are : 1, 2, 3, 6, 7, 14, 21, 42. These divisors squared are: 1, 4, 9, 36, 49, 196, 441, 1764.
#The sum of the squared divisors is 2500 which is 50 * 50, a square!
#
#Given two integers m, n (1 <= m <= n) we want to find all integers between m and n whose 
#sum of squared divisorsis itself a square. 42 is such a number.
#
#The result will be an array of arrays or of tuples (in C an array of Pair) or a string,
#each subarray having two elements, first the number whose squared divisors is a square and then the sum of the squared divisors.
#
#Examples:
#
#list_squared(1, 250) --> [[1, 1], [42, 2500], [246, 84100]]
#list_squared(42, 250) --> [[42, 2500], [246, 84100]]

from math import sqrt

temp_dict = {}
def divisor(item):
    temp = []
    for i in range(1, item+1):
        if item % i == 0:
            temp.append(i*i)
    return sum(temp)

def list_squared(m, n):
    temp_n = 0
    temp_m = 0
    temp_len = 0
    find = False
    for item in temp_dict.keys():
        if m <= item[0] and n >= item[1] and temp_len < item[1] - item[0]:
            temp_n = n
            temp_m = m
            temp_len = item[1] - item[0]
            find = True
    if not find:
        temp_list = []
        for item in range(m, n+1):
            sum_temp = divisor(item)
            if sqrt(sum_temp) % 1 == 0:
                temp_list.append([item, sum_temp])
        temp_dict.update({(m,n): temp_list})
        return temp_list
    else:
        temp_list = temp_dict[(temp_m, temp_n)]
        return temp_list
        for item in range(m, temp_m):
            sum_temp = divisor(item)
            if sqrt(sum_temp) % 1 == 0:
                temp_list.insert(0, [item, sum_temp])
        for item in rnage(temp_n, n):
            sum_temp = divisor(item)
            if sqrt(sum_temp) % 1 == 0:
                temp_list.append([item, sum_temp])
        temp_dict.update({(m,n): temp_list})
        return temp_list
