import web
import convey as cv
import json

#/interface webpy class
#user submits password then is
#redirected to Pairing
class Interface(object):
	def GET(self):
		return render.interface(message = 1)

	def POST(self):
		form = web.input(password = 'password')
		if form.password == cv.secret([3,3,0]):
			raise web.seeother('pairing_gui')
		else:
			error = ["Incorrect password! Please try again."]
			return render.interface(message = error)


#/pairing_gui webpy class
class Pairing(object):
	def GET(self):
		# update the warrior queue with any new entries then
		# get the friend and warrior queues from spreadsheets
		cv.update_warrior()
		friendq  = cv.names_no_null("Friend-Q", 1)
		warriorq = cv.names_no_null("Warrior-Q", 1)
		
		#render the pairing_gui webpage and pass queues as data to it
		return render.pairing_gui(list_of_names = [friendq, warriorq])
	
	def POST(self):
		#recieve friend and warrior name to be paired from request	
		form = web.input(friend = 'friend', warrior = 'warrior')
		

		# add the paired friend and warrior to the paired spreadsheet
		chosen_pair = [form.warrior, form.friend]
		cv.add_pair(chosen_pair)
		
		# remove the friend and warrior from respective 
		# queues as they have been paired
		cv.remove_from_queue("Friend-Q", form.friend)
		cv.remove_from_queue("Warrior-Q", form.warrior)

		# retrieve contact information for the friend and 
		# warrior to display to pairing committee member
		friendContact = cv.get_friend_info(form.friend, 'contact')
		warriorContact = cv.get_warrior_info(form.warrior, 'contact')

		#retrieve queues to display updated versions.
		friendq  = cv.names_no_null("Friend-Q", 1)
		warriorq = cv.names_no_null("Warrior-Q", 1)
		
		# create a single object to pass to /display webpage and render /display
		this = [chosen_pair, friendq, warriorq, friendContact, warriorContact]

		return render.display(this)
		
		"""all_lists should be of the form
		[chosen_pair, friendQ, warriorq]
		where chosen_pair = [chosen_friend, chosen_warrior]
		"""

# /add web.py class
class Add(object):
	def GET(self):
		return render.add(stuff = 3)
		
	# Recieves a friend's netid and number of pairs to be made
	# Checks that the friend is approved to help people 
	#and if so adds them to teh friend queue.
	def POST(self):	
		# recieve user information from POST request
		# form.netid - netid of the friend to be paired
		# form.number - number of times the friend wants to be paired
		form = web.input(netid = "netid", number = 1)
	
		# initialization
		num = int(form.number)
		sheet = cv.open_sheet('Friend-List')
		
		# find the column number for name, netid, and verified
		name_col  = cv.search_row(sheet, 1, 'name')
		netid_col = cv.search_row(sheet, 1, 'netid')
		veri_col  = cv.search_row(sheet, 1, 'verified')

		# find the users row within the spreadsheet
		row_num = cv.search_column(sheet, netid_col, form.netid)

		# if more than 1000 people sign up or if the spreadsheet is resized to > 1000.
		if row_num >= 1000:
			message = "FAILURE! We could not find your netID on the list. Please make sure you submitted the correct netID (%s). If this is the correct netID it is possible that was incorrectly entered on our spreadsheet or there is something wrong with this code (which is a very likely possibility). Please let us know about this problem, whether through our website, facebook, slack, next meeting, or randomly in the quad. THANK YOU!" % form.netid	

		else:
			the_values = sheet.row_values(row_num)
			
			# retrieve the friend's name and if they are verified
			name = the_values[name_col - 1] # -1 due to 1 indexing for spreadsheets
			verified = the_values[veri_col - 1]
	
			# if verified add to friend queue num (form.number) times.
			if verified.lower().strip() == 'yes':
				name_count = []
				for i in range(0, num):
					name_count.append(name)
			
				# names must be submitted as an array to the add_to_queue function
				cv.add_to_queue("Friend-Q", name_count)				
				message = "SUCCESS!"			
				
			else:
				message = "FAILURE! You're name is on the list but it looks like you have not been verified. In order to become verified you must come to a sufficient amount of trainings. At the trainings we go over situations you may encounter and talk about what the process of being a friend will be like (good ole logistics and all.) It is really quite fun. Once there was even candy. So please try to come out if you have not yet. If anything you'll at least learn how this stupid interface works. If you believe you have been verified though and have gone through trainings then please let somebody know so they can fix it. Again, its a stupid interface. But with your help maybe it can just be dumb."

		# render /add and pass the message and number of times added to the user
		return render.add(stuff = [message, num])

# /remove web.py class
# Purpose: GET disp
class Remove(object):
	def GET(self):

		# option = 1 is initial page, 2 if POST works, 3 if error
		return render.remove(option = 1)
		
	def POST(self):
		# retrieve data from request
		# form.netid - friend's netid to remove from queue
		form = web.input(netid = "netid")

		# find the corresponding columns within the sheet Friend-List
		sheet = cv.open_sheet('Friend-List')
		name_col  = cv.search_row(sheet, 1, 'name')
		netid_col = cv.search_row(sheet, 1, 'netid')
		
		row_num = cv.search_column(sheet, netid_col, form.netid)
		
		#this wont work if we have more than 950 entries.
		#thats ALOOOOOOT of people on the queue
		if row_num < 950:
			# find the name of the user within the sheet
			name_values = sheet.col_values(name_col)
			name = name_values[row_num - 1]
		
			# remove the user from the queue
			cv.remove_from_queue("Friend-Q", name, 'rm all')
			choice = 2
		else:
			#cant find netid error message
			choice = 3		
			
		# render /remove
		return render.remove(option = choice)


# /warrior webpy class
# Purpose: POST request sent to server to retrieve warrior information to display to pairing committee

# Requests currently recieved from /pairing_gui on click of a warrior's name
# Return: JSON object with information is sent back to the user
class WarriorInfo(object):
	def POST(self):
		warriorName = web.input()
		textName = warriorName['name']
		info = cv.get_warrior_info(textName, 'info')
		return json.dumps({'sex'       :info[0], 'year'    : info[1], 
						   'interests' :info[2], 'hobbies' : info[3],
						   'struggle'  :info[4]})

# /friend webpy class
# Purpose: POST request sent to server to retrieve friend information 
# to display to pairing committee

# Requests currently recieved from /pairing_gui on click of a friend's name
# Return: JSON object with information is sent back to the user
class FriendInfo(object):
	def POST(self):
		warriorName = web.input()
		textName = warriorName['name']
		info = cv.get_friend_info(textName, 'info')
		return json.dumps({'sex'    :info[0], 'year'     :info[1], 
						   'major'  :info[2], 'interests':info[3],
						   'hobbies':info[4]})


class EndPair(object):
	def GET(self):
		#display warrior names for dropdown list
		warriors = cv.names_no_null('Current-Pairings', 1)
		
		#for testing
		#warriors = ['Hannah', "montana"]
		return render.end_pair(table = [warriors])

	def POST(self):
		# password gaurentees someone IN open ears ends the pair
		form = web.input(warrior="warrior", netid   ="netid",
						 notes  ="notes"  , password="password")
		
		if form.password == cv.secret([3,3,1]):
			#friend types netID and uses it to pair
			sheet = cv.open_sheet('Friend-List')
			name_col  = cv.search_row(sheet, 1, 'name')
			netid_col = cv.search_row(sheet, 1, 'netid')
			row_num = cv.search_column(sheet, netid_col, form.netid)

			# find the name of the user within the sheet
			name_values = sheet.col_values(name_col)
			friend = name_values[row_num - 1]
		
		
			pair = [form.warrior, friend]
			#removes given pair from Current-Pairings 
			#and updates status in All-Pairings
			if cv.remove_pair(pair) == 'Pair Removed':
					cv.update_all_pair(pair, form.notes)
			else:
				pair = [['PAIR NOT'],['FOUND']]
			
			data = [pair, form.notes]
		else:
			#extras because len(1 and 2) conditionals already taken
			data = ["Incorrect Password! Please try again.",3 ,4]
		
		return render.end_pair(table = data)


if __name__ == '__main__':
#URLs and corresponding classes to handle requests to the URL for web.py
	
	urls = (
		'/pairing_gui', 'Pairing',
		'/interface'  , 'Interface', 
		'/warriorinfo', 'WarriorInfo',
		'/friendinfo' , 'FriendInfo',
		'/add'        , 'Add',
		'/remove'     , 'Remove',
		'/end_pair'   , 'EndPair'
	)
	
	# Create the web application and set the render directory
	app = web.application(urls, globals())
	render = web.template.render('templates/')
	app.run()
