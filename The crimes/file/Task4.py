from task1 import crimes

name = input("Name: ")

if name in crimes:
    print(crimes[name])
    for crime in crimes[name]:
        with open('file.csv', 'at') as file:
            file.write(str(crime)+ '\n')

