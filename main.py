x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)
print(x)

thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.append("orange")
thistuple = tuple(y)
print(thistuple)

thistuple = ("apple", "banana", "kiwi")
y = ("orange",)
thistuple += y
print(thistuple)


thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.remove("apple")
thistuple = tuple(y)
print(thistuple)


thistuple = ("tamil", "banana", "cherry")
for x in thistuple:
  print(x)

thistuple = ("math", "banana", "cherry")
for i in range(len(thistuple)):
  print(thistuple[i])

  thistuple = ("one", "banana", "cherry")
i = 0
while i < len(thistuple):
  print(thistuple[i])
  i = i + 1

a=int(input())
b=int(input())
c=int(input())
a=b+c 
d=a*b*c 
c=a/b 
print(d)

tuple1 = ("a", "b" , "c")
tuple2 = (1, 2, 3)
tuple3 = tuple1 + tuple2
print(tuple3)
