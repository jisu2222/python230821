# demoLoop.py
value = 5
while value > 0:
    print(value)
    value -= 1

print("---for in---")
lst= [100,"사과",3.14] 
for item in lst:
    print(item, type(item))

print("---break구문---") 
lst=[1,2,3,4,5,6,7,8,9,10]
for item in lst:
    if item  >5: 
        break
    print("item:{0}".format(item))

print("---continue구문---") 
lst=[1,2,3,4,5,6,7,8,9,10]
for item in lst:
    if item % 2 == 0: 
        continue
    print("item:{0}".format(item))        

print("---range()함수---") 
print(list(range(10))) 
print(list(range(2000,2024)))
print(list(range(1,32))) 
for i in range(5):
    print(i)   