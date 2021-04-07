# Explain your work

# Answer 1
list = [1, 2, 3, 4, 5, 6, 7]
length = len(list)
left = 0  # at beginning this will point to first element of first half
for right in range(length - 1, length // 2, -1):  # then run a loop from last to half of list
    temp = list[left]  # store element present at left index in temp
    list[left] = list[right]  # store element present at right index in left index
    list[right] = temp  # store element present in temp in right index
    left = left + 1
print(list)
# Answer2
n = int(input("Enter the number :"))
for num in range(n + 1):  # run a loop from 0 to n
    if num % 2 == 0:  # check if the number is even
        print(num)  # then print that num
