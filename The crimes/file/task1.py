from json import dumps

indexes_to_int = [0, 2, 3, 4]
indexes_to_bool = [7]
INDEX_OF_NAME = 5

crimes = {}
with open('../Crimes.csv') as file:
    header = file.readline().rstrip().split(',')
    header.pop(INDEX_OF_NAME)
    for line in file:
        crime_list = line.rstrip().split(',')
        for index in indexes_to_int:
            if crime_list[index] != '-':
                crime_list[index] = int(crime_list[index])

        for index in indexes_to_bool:
            if crime_list[index] == "True":
                crime_list[index] = True
            else:
                crime_list[index] = False

        name = crime_list.pop(INDEX_OF_NAME)

        crime_dict = {}
        for i in range(len(header)):
            crime_dict[header[i]] = crime_list[i]

        if name in crimes:
            crimes[name].append(crime_dict)
        else:
            crimes[name] = [crime_dict]

# print(dumps(crimes, indent=4))


