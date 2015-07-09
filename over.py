from datetime import datetime
import os.path

today = str(datetime.now().year) + '.' + str(datetime.now().month) + '.' + str(datetime.now().day)
yesterday = str(datetime.now().year) + '.' + str(datetime.now().month) + '.' + str(datetime.now().day-1)
someday = str(datetime.now().year) + '.' + str(datetime.now().month) + '.'
direction = os.path.expanduser(r'~\Dropbox\Work\Python\Programms\txt\over.txt')
total = 0

time = input('time = ')

if len(time) == 0: # Print the data and count current overtimes
	over = open(direction,'r')
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
	exit()

elif time == 'help':
	print('''
Adding overtime for today: <time> Note: if working day is not over the time will go for yestarday
Adding overtime for yestarday: *<time>
Adding overtime for any day of current month: <day>*<time>
Adding overtime for any date this year: *<time>* and after that: <month>.<day>
Instance of <time>: 1, 1.30, 1.55, 1,00
		''')
	exit()

elif '*' not in time and datetime.now().hour >= 19: # Adding overtime for today 
	over = open(direction,'a')
	# over = open('over.txt','a')
	if len(time) == 1:
		over.write(today + ' - ' + time + '.00' + '\n') # If only hour entered adding minutes
	else:
		over.write(today + ' - ' + time + '\n')

elif (time[0] == '*' and time[-1] != '*') or (datetime.now().hour < 19 and '*' not in time): # Adding overtime for yestarday
	if datetime.now().hour < 19:
		time = '*' + time
	over = open(direction,'a')
	if len(time) == 2:
		over.write(yesterday + ' - ' + time[1:] + '.00' + '\n')
	else:
		over.write(yesterday + ' - ' + time[1:] + '\n')

elif time[0] == '*' and time[-1] == '*': # Adding time for any date this year
	month_day = input('Date: ')
	date = str(datetime.now().year) + '.' + month_day
	over = open(direction,'a')
	if len(time) == 3:
		over.write(date + ' - ' + time[1:-1] + '.00' + '\n')
	else:
		over.write(date + ' - ' + time[1:-1] + '\n')

elif time[0] != '*' and '*' in time: # Adding time for any day of current month
	over = open(direction,'a')
	if len(time[time.find('*'):]) < 3:
		over.write(someday + time[:time.find('*')] + ' - ' + time[time.find('*')+1:] + '.00' + '\n')
	else:
		over.write(someday + time[:time.find('*')] + ' - ' + time[time.find('*')+1:] + '\n')

over.close()

o = open(direction,'r') # Adding all overtimes to list to show up the last one
line = o.readline()
data = []
while line:
	line = o.readline()
	data.append(line)
o.close()

print('\n' + data[-2])
print(today + ' - today')
