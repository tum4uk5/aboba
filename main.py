def _min(array):
    min_ = array[0]
    for i in array:
        if i < min_:
            min_ = i
    return min_

def _max(array):
    max_ = array[0]
    for i in array:
        if i > max_:
            max_ = i
    return max_

def _mult(array):
    mult_ = 1
    for i in array:
        mult_ *= i
    return mult_

def _sum(array):
    sum_ = 0
    for i in array:
        sum_ += i
    return sum_

f = open("data.txt")
array_str = f.readline().split()
array_int = []

for i in array_str:
    array_int.append(int(i))

print("Минимальное:", _min(array_int))
print("Максимальное:" ,_max(array_int))
print("Сумма:", _sum(array_int))
print("Произведение:", _mult(array_int))
f.close()

# f = open("10000.txt", "w")
# stri = ""
# for i in range(1, 10001):
#     stri += str(i) + " "
# f.write(stri)
#
# f = open("15000.txt", "w")
# stri = ""
# for i in range(1, 15001):
#     stri += str(i) + " "
# f.write(stri)
#
# f = open("20000.txt", "w")
# stri = ""
# for i in range(1, 20001):
#     stri += str(i) + " "
# f.write(stri)
#
# f = open("25000.txt", "w")
# stri = ""
# for i in range(1, 25001):
#     stri += str(i) + " "
# f.write(stri)