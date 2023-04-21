# first_name = 'Sumitta'
# last_name = 'Nauli'
# full_name = first_name + ' ' + last_name  #CARA 1
# full_name = f'{first_name} {last_name}'  #CARA 2
# print(full_name)


from datetime import datetime

today = datetime.now()

date_time = today.strftime('%Y-%m-%d %H:%M:%S')
print(date_time)