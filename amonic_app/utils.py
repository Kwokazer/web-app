import csv
from .models import Users, Roles, Offices


from datetime import datetime

# Пример функции преобразования даты из "M-D-YYYY" в "YYYY-MM-DD"
def convert_date_format(date_str):
    # Преобразование строки в объект datetime с текущим форматом 'M-D-YYYY'
    date_object = datetime.strptime(date_str, '%m-%d-%Y')
    # Преобразование объекта datetime обратно в строку в формате 'YYYY-MM-DD'
    return date_object.strftime('%Y-%m-%d')
def import_data_from_csv(file_path):
    with open(file_path, 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            role_title = row['role_title']
            email = row['email']
            password = row['password']
            firstname = row['firstname']
            lastname = row['lastname']
            office_title = row['office_title']
            birthdate = row['birthdate']
            active = row['active']

            # Получение или создание объекта Roles и Offices
            role, created_role = Roles.objects.get_or_create(title=role_title)
            office, created_office = Offices.objects.get_or_create(title=office_title)

            birthdate = convert_date_format(birthdate)

            # Создание объекта Users и сохранение данных из CSV
            user, created = Users.objects.get_or_create(
                roleid=role,
                email=email,
                password=password,
                firstname=firstname,
                lastname=lastname,
                officeid=office,
                birthdate=birthdate,
                active=active
            )
            if created == True:
                user.save()
            else:
                continue