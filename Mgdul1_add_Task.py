my_dict = {}
grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}

a = sum (grades[0]) / len (grades[0])
grades[0]= a
b = float(sum (grades[1]) / len (grades[1]))
grades[1]= b
c = float(sum (grades[2]) / len (grades[2]))
grades[2]= c
d = float(sum (grades[3]) / len (grades[3]))
grades[3] = d
e = float(sum (grades[4]) / len (grades[4]))
grades[4]= e
print(grades)
my_list = list(students)
print(my_list)
print(type(my_list))
f = grades
print(f)
f_ = [[my_list[4], f[0]], [my_list[1], f[1]], [my_list[0], f[2]], [my_list[2], f[3]], [my_list[3],f[4]]]
   #if my_list[4] == 'Aaron' and my_list[1] == 'Bilbo' and my_list[0] == 'Johnny' and my_list[2] == 'Khendrik' and my_list[3] == 'Steve':
print(f_)
print(type(f_))
dict(f_)
my_dict = dict(f_)
print(type(dict(my_dict)))

print(my_dict)
print(type(my_dict))

