from task1 import crimes

with open('files/types.txt') as file:
    crimes_spec = file.read().split(',')

for name in crimes:
    for crime in crimes[name]:
        type_ = crime["Type"]
        if type_ in crimes_spec:
            print(name)
            break





