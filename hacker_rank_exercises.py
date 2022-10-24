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

# def diagonalDifference(arr):
#     # Write your code here
#     sum1 = 0
#     sum2 = 0 
#     n = len(arr)
  
#     for i in range(len(arr)):
#       sum1 += arr[i][i]
#       sum2 += arr[i][n-1]
#       n = n-1 

#     sum3 = sum1 - sum2
#     print(abs(sum3))
      

# diagonalDifference([[0,1,2],
#                     [3,4,5],
#                     [9,7,8]])

def findZigZagSequence(a, n):
    a.sort()
    mid = int((n + 1)/2) -1
    a[mid], a[n-1] = a[n-1], a[mid]

    st = mid + 1 
    ed = n - 2 
    while(st <= ed):
        a[st], a[ed] = a[ed], a[st]
        st = st + 1
        ed = ed - 1

    for i in range (n):
        if i == n-1:
            print(a[i])
        else:
            print(a[i], end = ' ')
    return




# def alphabet_addition(a, k):
#   incremented_char = (chr((ord(a) - 97 + k) % 26 + 97))
#   print(incremented_char)

# alphabet_addition('w', 5)

# def caesarCipherB(s, k):
#   def cypher(x):
#     if x.isalpha():
#       if x.isupper():
#         x = (chr((ord(x.lower()) - 97 + k) % 26 + 97))
#         return x.upper()
#       return (chr((ord(x) - 97 + k) % 26 + 97))
#     else:
#       return x 
#   string = map(cypher, s)
#   return ''.join(list(string))

# print(caesarCipherB('Hello', 2))


# def caesarCipher(s, k):
#     # Write your code here
#     encrypted = map(lambda x: (chr((ord(x) - 97 + k) % 26 + 97)) if x.isalpha() else x, s)
#     print(''.join(list(encrypted)))

# caesarCipher('Always-Look-on-the-Bright-Side-of-Life', 5)
