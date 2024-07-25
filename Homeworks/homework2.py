homework_done_count = 12
hour_spent_count = 1.5
name_course = 'Python'
homework_per_hour = hour_spent_count/homework_done_count

print('Курс:', name_course + ', всего задач:' + str(homework_done_count) + ', затрачено часов:',
      str(hour_spent_count) + ', среднее время выполнения',
      homework_per_hour, 'часа.')
