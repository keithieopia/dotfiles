#!/usr/bin/env python3

import sys, os
from datetime import datetime

LOGFILE = ".timeclock.log"
PAYPERIOD_KNOWN = "2019-01-21"
PAYPERIOD_DAYS = "14"

def print_red(msg): print("\033[91m{}\033[00m" .format(msg)) 
def print_green(msg): print("\033[92m{}\033[00m" .format(msg)) 

#def usage():
	# TODO

def find_payperiod(ts):
	interval = int(PAYPERIOD_DAYS) * 86400
	
	dt = datetime.strptime(PAYPERIOD_KNOWN, '%Y-%m-%d')
	offset = int( timestamp(dt) )
	
	while offset < int(ts):
		offset = offset + interval
		
	return ((offset - interval), offset)

def curr_payperiod():
	t = timestamp()
	(start, end) = map(datetime.fromtimestamp, find_payperiod(t)) 
	return (start,end)

def payperiod_days_left():
	(start, end) = curr_payperiod()
	end = int( timestamp(end) )
	ts = int( timestamp() )
	return int( ((end - ts) / 86400) - 1 )

def payperiod_total():
	t = timestamp()
	(pstart, pend) = map(int, map(timestamp, map(datetime.fromtimestamp, find_payperiod(t))))
	worked = 0
	
	with open(LOGFILE) as f:
		for line in f:
			line = line.split()
			
			if len(line) == 2:
				(start, end) = map(int, line)
				
				if start > pstart:
					worked = worked + (end - start)

	return worked

def print_payperiod_total():
	return secs_to_hour_min( payperiod_total() )

def secs_to_hour_min(worked):
	worked_hours = int(worked / 3600)
	worked_mins  = int( (worked - (worked_hours * 3600)) / 60 )

	return str(worked_hours) + ":" + "{:0<2}".format( str(worked_mins))

def print_status():
	(start, end) = curr_payperiod()
	period = start.strftime("%-m/%d") + " - " + end.strftime("%-m/%d")
	days = str(payperiod_days_left())
	
	line = period + " | " + days + " days left"
	print(line)
	print( ('-' * len(line)) + "\n")
	
	print("STATUS:     ", end="")
	if status() == "in":
		print_green("on the clock")
		
		ts = get_last_line().strip()
		th = ts_to_human(ts)
		print("STARTED:    " + th[1], end="")
		
		worked = secs_to_hour_min(int(timestamp()) - int(ts))
		print(" (" + worked + " hours)")
		
	else:
		print_red("off the clock")

	print ("PAYPERIOD:  " + print_payperiod_total())

def ts_to_human(t):
	t = datetime.fromtimestamp( int(t) )
	return (t.strftime("%-m/%d"), t.strftime("%-I:%M %p"))

def log(showall = False):
	last = 0
	(pstart, pend) = map(timestamp, curr_payperiod())
	
	with open(LOGFILE) as f:
		for line in f:
			line = line.split()

			if line[0] >= pstart or showall == True:
				start = ts_to_human(line[0])			

				if start[0] != last:
					last = start[0]
					print("{:>5}".format(start[0]) + " | ", end="")
				else:
					print("      | ", end="")

				if len(line) == 2:
					end = ts_to_human(line[1])
					print('{:<8}'.format(start[1]) + " - " + end[1])
				else:
					print('{:<8}'.format(start[1]) + " ~ ")

def get_last_line():
	for line in open(LOGFILE):
		pass

	return line

def status():
	line = get_last_line()

	if len(line.split()) == 2:
		return "out"
	else:
		return "in"

def timestamp(now = datetime.now()):
	return str(int(datetime.timestamp(now)))

def start():
	if status() == "in":
		print_red("Already clocked in!")
		sys.exit(1)
	else:
		now = datetime.now()

		with open(LOGFILE, "a+") as f:
			f.write("\n")
			f.write( timestamp(now) )
			f.close()

		print_green("Clocked in at " + now.strftime("%-I:%M %p"))

def stop():
	if status() == "out":
		print_red("Already clocked out!")
		sys.exit(1)
	else:
		now = datetime.now()
		started = get_last_line()

		with open(LOGFILE, "rb+") as f:
			f.seek(0, os.SEEK_END)
			f.write( (" " + timestamp(now)).encode() )
			f.close()

		print_red("Clocked out at " + now.strftime("%-I:%M %p") + "\n")

		worked = get_last_line().split()
		worked = int(worked[1]) - int(worked[0])
		
		print("Worked " + secs_to_hour_min(worked) + " hours, grand total " + print_payperiod_total() + " hours")
		
		
if len(sys.argv) == 1:
	print_status()

elif sys.argv[1] == "log":
	log()

elif sys.argv[1] == "all":
	log(True)

elif sys.argv[1] == "start":
	start()

elif sys.argv[1] == "stop":
	stop()

elif sys.argv[1] == "status":
	print("Clocked " + status())

else:
	print_red("Unknown command " + sys.argv[1])
	sys.exit(1)