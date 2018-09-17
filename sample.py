import datetime

today = datetime.date.today()

print(today)


num = 12

if num < 4 :
    cal = 10
    print(cal)
else :
    cal = 50
    print(cal)


list_max =[1,2,3,4]
print (list_max)

list_len = len(list_max)
print(list_len)

list_max.append(5)
print(list_max)

list_max.insert(0,0)
print(list_max)

list_max.pop(4)
print(list_max)

if num<10 :
    list_max.pop(1)


else :
    print("明日また遊ぶ")
