import web
import convey as cv
import json

# URLs and corresponding classes to handle requests to the URL for web.py
urls = (
	'/pairing_gui', 'Pairing',
	'/add', 'Add',
	'/remove', 'Remove', 
	'/warriorinfo', 'WarriorInfo',
	'/friendinfo', 'FriendInfo',
	'/add'        , 'Add',
	'/remove'     , 'Remove'
)

# Create the web application and set the render directory
app = web.application(urls, globals())
render = web.template.render('templates/')

#/pairing_gui webpy class
class Pairing(object):
	def GET(self):
		# get the friend and warrior queues from spreadsheets
		friendq  = cv.names_no_null("Friend-Q", 1)
		warriorq = cv.names_no_null("Warrior-Q", 1)
		
		#place in a single object to pass to webpage
		total = [friendq, warriorq]
		
		#render the pairing_gui webpage and pass queues as data to it
		return render.pairing_gui(list_of_names = total)
	
	def POST(self):
		#recieve friend and warrior name to be paired from request	
		form = web.input(friend = 'friend', warrior = 'warrior')
		
		# add the paired friend and warrior to the paired spreadsheet
		chosen_pair = [form.warrior, form.friend]
		cv.add_pair(chosen_pair)
		
		# remove the friend and warrior from respective queues as they have been paired
		cv.remove_from_queue("Friend-Q", form.friend)
		cv.remove_from_queue("Warrior-Q", form.warrior)

		# retrieve contact information for the friend and warrior to display to pairing committee member
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
	# Checks that the friend is approved to help people and if so adds them to teh friend queue.
	def POST(self):	
		# recieve user information from POST request
		# form.netid - netid of the friend to be paired
		# form.number - number of times the friend wants to be paired
		form = web.input(netid = "netid", number = 1)
	
		# initialization
		new_list =[]
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
				
				# retrieve the friend queue to pass to user
				# TODO: Remove following testing unless we want to display this
				new_list = cv.names_no_null("Friend-Q", 1)
			else:
				message = "FAILURE! You're name is on the list but it looks like you have not been verified. In order to become verified you must come to a sufficient amount of trainings. At the trainings we go over situations you may encounter and talk about what the process of being a friend will be like (good ole logistics and all.) It is really quite fun. Once there was even candy. So please try to come out if you have not yet. If anything you'll at least learn how this stupid interface works. If you believe you have been verified though and have gone through trainings then please let somebody know so they can fix it. Again, its a stupid interface. But with your help maybe it can just be dumb."

		# render /add and pass the message, number of times added and friend queue to the user
		return render.add(stuff = [message, num, new_list])

# /remove web.py class
class Remove(object):
	def GET(self):
		# default value of 3 to have the correct part of if statement - CHECK: this comment
		return render.remove(friendq = 3)
		
	def POST(self):
		# retrieve data from request
		# form.netid - friend's netid to remove from queue
		form = web.input(netid = "netid")

		# find the corresponding columns within the sheet Friend-List
		sheet = cv.open_sheet('Friend-List')
		name_col  = cv.search_row(sheet, 1, 'name')
		netid_col = cv.search_row(sheet, 1, 'netid')
		row_num = cv.search_column(sheet, netid_col, form.netid)

		# find the name of the user within the sheet
		name_values = sheet.col_values(name_col)
		name = name_values[row_num - 1]
		# print name_values, name, row_num #debugging purposes
		
		# remove the user from the queue
		cv.remove_from_queue("Friend-Q", name, 'rm all')
		
		# retrieve the friend qeuue to pass to /remove to ensure they are removed
		new_list = cv.names_no_null("Friend-Q", 1)
		
		# render /remove
		return render.remove(friendq = new_list)

# /warrior webpy class
# Purpose: POST request sent to server to retrieve warrior information to display to pairing committee
#		Requests currently recieved from /pairing_gui on click of a warrior's name
# Return: JSON object with information is sent back to the user
class WarriorInfo(object):
	def POST(self):
		warriorName = web.input()
		textName = warriorName['name']
		info = cv.get_warrior_info(textName, 'info')
		return json.dumps({'sex': info[0], 'year': info[1], 'interests': info[2], 'hobbies': info[3], 'struggle':info[4]})

# /friend webpy class
# Purpose: POST request sent to server to retrieve friend information to display to pairing committee
# 		Requests currently recieved from /pairing_gui on click of a friend's name
# Return: JSON object with information is sent back to the user
class FriendInfo(object):
	def POST(self):
		warriorName = web.input()
		textName = warriorName['name']
		info = cv.get_friend_info(textName, 'info')
		return json.dumps({'sex': info[0], 'year': info[1], 'major':info[2], 'interests':info[3], 'hobbies':info[4]})

if __name__ == '__main__':
	app.run()
