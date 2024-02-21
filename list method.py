a = [4,5,7,9,6,2,1]
a.sort()
print(a)

a = [4,5,8,9,4,3,2]
a.sort(),a.reverse()
print(a)

x = ['d','f','h','a','b','c']
x.sort()
print(x)

x = ['c','d','g','b','a']
x.sort(reverse=True)
print(x)


num = [1,2,3,4]
num.reverse()
print(num)

a = ["hope","foundation","ai"]
b = ["skill","training","center"]
a.extend(b)
print(a)

a = ['raj','chandu','kalyan','arjuna']
b =a.count("arjuna")
print(b)

a = [8,2,3,1]
print(max(a))
print(min(a))

a = ["a","p","b","c"]
a.append("b")
print(a)

a = ['apple','orange','banana']
b = ["a","b","c"]
a.extend(b)
print(a)

a = [1,2,3,5]
b = [6,7,8,9]
print(a+b)

a = [1,2,1,3,4,5,6,4,6,7,4,7]
x = (set(a))
print(x)

a =input([6,3,4,5,7,8,9,5])
y = input(a[0])
x = input(a[-1])
print(y,x)
