if hash remind 2>/dev/null; then
	#
	# this downloads events from google calendar and converts them
	# to remind's format 
	#
	GOOGLE_REMIND="$HOME/.remind.d/googleREM"

	# provides $GOOGLE_CALS (BASH array)
	source ~/.bash_secrets

	# if current reminders file is older than a day, delete it
	if [[ $(find "$GOOGLE_REMIND" -mtime +1 -print) ]]; then
		rm "$GOOGLE_REMIND"
	fi

	# if there isn't a reminders file, download it
	if [ ! -f "$GOOGLE_REMIND" ]; then 
		touch "$GOOGLE_REMIND"

		for i in "${GOOGLE_CALS[@]}"; do
			# ics2rem found in python library "remind"
			# pip3 install remind
			curl -s https://calendar.google.com/calendar/ical/$i/basic.ics | ics2rem >> $GOOGLE_REMIND 2>/dev/null
		done
	fi
    
    #
    # output the next two weeks
	#
	tput setaf 6
	remind -mc+2w$(tput cols) $HOME/.remind
	tput sgr0
fi
