from task1 import crimes, dumps

year = int(input("Year: "))

for name in crimes:
    for crime_dict in crimes[name]:
        if crime_dict['Year'] == year:
            print(crime_dict["ID"])