team1_num = 5
team2_num = 6
score1 = 40
score2 = 40
team1_time = 1552.5
team2_time = 2153.3
tasks_total = score1 + score2
time_avg = (team1_time + team2_time) / tasks_total
if score1 > score2 or score1 == score2 and team1_time < team2_time:
    challenge_result = 'Победа команды Мастера кода!'
elif score1 < score2 or score1 == score2 and team1_time > team2_time:
    challenge_result = 'Победа команды Волшебники Данных!'
else:
    challenge_result = 'Ничья!'

print('В команде Мастера кода участников: %d!' % team1_num)
print('Итого сегодня в командах участников: %d и %d!' % (team1_num, team2_num), end='\n\n')
print('Команда Волшебники данных решила задач: {}!'.format(score2))
print('Волшебники данных решили задачи за {} с !'.format(team2_time), end='\n\n')
print(f'Команды решили {score1} и {score2}.')
print(f'Результат битвы: {challenge_result}')
print(f'Сегодня было решено {tasks_total} задач, в среднем по {time_avg:.1f} секунд на задачу!')
