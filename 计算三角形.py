a,b,c = (input("请输入三角形三边的长：").split())
a = int(a)
b = int(b)
c = int(c)

p = a + b + c

s = (p*(p-a)*(p-b)*(p-c))**0.5

print("三角形面积为:",format(s,'.2f'))

