from datetime import datetime

today = str(datetime.now().year) + '.' + str(datetime.now().month) + '.' + str(datetime.now().day)
yesterday = str(datetime.now().year) + '.' + str(datetime.now().month) + '.' + str(datetime.now().day-1)
someday = str(datetime.now().year) + '.' + str(datetime.now().month) + '.'
total = 0

time = input('time = ')

if len(time) == 0: # Print the data and count current overtimes
	over = open('over.txt','r')
	line = over.readline()
	while line:
		print(line)		
		line = line[5:-1] # Cutting the year and \n symbol
		if (line[:line.find('.')] == str(datetime.now().month-1) and int(line[line.find('.')+1:line.find('-')-1]) in range(25,32)) or \
		(line[:line.find('.')] == str(datetime.now().month) and int(line[line.find('.')+1:line.find('-')-1]) in range(1,25)): 
		# Choosing dates from 25 lats month till 24 of currents
			try: # Dismissing empty lines
				total += int(line[-4]) + int(line[-2:])/60
			except ValueError:
				pass
		line = over.readline()
	print('Totally ' + str(total) + ' hours')

elif time == 'help':
	print('''
Adding overtime for today: <time>
Adding overtime for yestarday: *<time>
Adding overtime for any day of current month: <day>*<time>
Adding overtime for any date this year: *<time>* and after that: <month>.<day>
Instance of <time>: 1, 1.30, 1.55, 1,00
		''')

elif '*' not in time: # Adding overtime for today 
	over = open('over.txt','a')
	if len(time) == 1:
		over.write(today + ' - ' + time + '.00' + '\n') # If only hour entered adding minutes
	else:
		over.write(today + ' - ' + time + '\n')

elif time[0] == '*' and time[-1] != '*': # Adding overtime for yestarday 
	over = open('over.txt','a')
	if len(time) == 2:
		over.write(yesterday + ' - ' + time[1:] + '.00' + '\n')
	else:
		over.write(yesterday + ' - ' + time[1:] + '\n')

elif time[0] == '*' and time[-1] == '*': # Adding time for any date this year
	month_day = input('Date: ')
	date = str(datetime.now().year) + '.' + month_day
	over = open('over.txt','a')
	if len(time) == 3:
		over.write(date + ' - ' + time[1:-1] + '.00' + '\n')
	else:
		over.write(date + ' - ' + time[1:-1] + '\n')

elif time[0] != '*' and '*' in time: # Adding time for any day of current month
	over = open('over.txt','a')
	if len(time[time.find('*'):]) < 3:
		over.write(someday + time[:time.find('*')] + ' - ' + time[time.find('*')+1:] + '.00' + '\n')
	else:
		over.write(someday + time[:time.find('*')] + ' - ' + time[time.find('*')+1:] + '\n')

elif time != 'help':
	over.close()
