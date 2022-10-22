# # def in_range(input):
# #   x = range(1,20)
# #   return input in x

# # print(in_range(1))

# # def squared(n):
# #   for i in range(n):
# #         print(f'{i * i}')

# # squared(7)

# # def is_leap(year):
# #     leap = False
    
# #     # Write your logic here
# #     if year < 100 and year % 4 == 0:    
# #         leap = True
# #     elif year > 100 and year % 400 == 0:
# #         Leap = True
# #     return leap

# def is_leap(year):
#     leap = False
#     if year%4==0 and (year%100!=0 or year%400==0):
#          return True
#     return leap



# def plusMinus(arr):
#     zeros = 0
#     positives = 0
#     negatives = 0 
#     number_of_elements = len(arr)
#     for i in arr:
#         if i == 0:
#             zeros += 1
#         elif i > 0:
#             positives += 1
#         elif i < 0:
#             negatives += 1
#     print(positives/number_of_elements)
#     print(negatives/number_of_elements)
#     print(zeros/number_of_elements)

    

# plusMinus([0,1,2,0,-1])


# def miniMaxSum(arr):
#   arr.sort()
#   min_sum = 0
#   max_sum = 0 
#     # Write your code here
#   for i in arr[:-1]:
#     min_sum += i 
#     max_sum += i
#   max_sum = max_sum + arr[-1] - arr[0]

#   print(min_sum, max_sum)
 

# miniMaxSum([1,2,3,4,5])

# def timeConversion(s):
  
#     # Write your code here
#   if s[8:11] == 'PM' and s[:2] != '12':
#     integer_string = int(s[:2]) + 12
#     new_string = s.replace(s[:2], str(integer_string))
#     print(new_string.strip('PM'))
#   elif s[8:11] == 'AM' and s[:2] == '12':
#     new_string = s.replace(s[:2], '00')
#     print(new_string.strip('AM')) 
#   else:
#     print(s.strip('APM'))
    

# timeConversion('12:05:45AM')

# def fizzBuzz(n):
#     for i in range(1, n+1):
#         if i % 3 == 0 and i % 5 == 0:
#             print('FizzBuzz')
#         elif i % 3 == 0:
#             print('Fizz')
#         elif i % 5 == 0:
#             print('Buzz')
#         else:
#           print(i)
     

# fizzBuzz(14)

# def lonelyinteger(a):
#     # Write your code here
#     for n in a:
#         if a.count(n)==1:
#             return n 

def diagonalDifference(arr):
    # Write your code here
    sum1 = 0
    sum2 = 0 
    n = len(arr)
  
    for i in range(len(arr)):
      sum1 += arr[i][i]
      sum2 += arr[i][n-1]
      n = n-1 

    sum3 = sum1 - sum2
    print(abs(sum3))
      

diagonalDifference([[0,1,2],
                    [3,4,5],
                    [9,7,8]])