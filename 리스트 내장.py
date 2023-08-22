print("---리스트 내장---")
lst = list(range(1,11))
print([1**2 for i in lst if i>5])
tp=("apple","kiwi","orange")
print([len(i) for i in tp])
fruits = {100:"apple", 200:"kiwi"}
print([v.upper() for v in fruits.values()])
