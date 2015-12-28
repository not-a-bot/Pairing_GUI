import web
import convey as cv

urls = (
	'/pairing_gui', 'Pairing',
	'/add', 'Add',
	'/remove', 'Remove'
)

app = web.application(urls, globals())
render = web.template.render('templates/')

class Pairing(object):
	def GET(self):
	#once /Pairing webpage is loaded the GET method
	#renders the pairing gui.html from the templates folder
		#list names in the Friend and Warrior qs
		#both are formatted so names are in column 1
		friendq  = cv.names_no_null("Friend-Q", 1)
		warriorq = cv.names_no_null("Warrior-Q", 1)
		
		total = [friendq, warriorq]
		
		return render.pairing_gui(list_of_names = total)
#the rendered pairing gui contains a form on it, which
#once submitted calls on the POST method below	
	

	#the pairing gui in templates will call upon this method to
	#record information submitted to the website
	def POST(self):
#once this method is called upon it takes the pairs and 
#removes them from the current queue, adding them to the
#current pairings list. THIS IS WHERE THE MAGIC HAPPENS.		
		form = web.input(friend = 'friend', warrior = 'warrior')
		
	#let this if statement verify that the user submitted
	#everything correctly. that means ADD MORE HERE
	#ik what ur thinking, wheres the more? wheres
	#the if statements? well, now its dropdown, so user
	#would need to be rly dumb, i guess there could be
	#check that chosen is what they want... an r u sure button
		
		
		#for some reason, firt last becomes just first...
		chosen_pair = [form.warrior, form.friend]	

		#these three functions just updates sheets removing both 
		#from the queues and adding them to both pairing sheets
		cv.add_pair(chosen_pair)
		
		#this runs default and only removes their names once
		cv.remove_from_queue("Friend-Q", form.friend)
		cv.remove_from_queue("Warrior-Q", form.warrior)


		#redownload queues to display updated versions.
		friendq  = cv.names_no_null("Friend-Q", 1)
		warriorq = cv.names_no_null("Warrior-Q", 1)
		this = [chosen_pair, friendq, warriorq]
	

#this renders display.html. It shows the new queues and the
#pair of people you added to both pairings lists
		return render.display(all_lists = this)
		
		"""all_lists should be of the form
		[chosen_pair, friendQ, warriorq]
		where chosen_pair = [chosen_friend, chosen_warrior]
		"""

class Add(object):
	#this is the code for the buttons for friends to add 
	#themselves to the queue
	def GET(self):
		return render.add(stuff = 3)
		

	#THIS whole thing needs to be rewritten to check if 
	#a friend is verified and if they are then add them to the list
	#if not then display a correct error message of them either
	#not being verified or not being on the list
	#
	def POST(self):	
		ver = 0
		i = 1
		#im assuming this means the default setting is 1
		form = web.input(name = "name", number = 1)
		formatted_name = form.name.lower().strip()
		print form.number
		print form.name
		print formatted_name
		
		num = int(form.number)
		print num
		
		#check that they are on friend list AND verified
		name_col = 1

		the_list = cv.names_no_null("Friend-List", name_col)
		print the_list	
		for lines in the_list:
			if formatted_name == lines:
				ver = ver + 1
		#although it being >1 would be a mistake because a friend shouldnt
		#be on the list multiple times
		if ver >= 1:
			name_count = []
			while i <= num:
			#remember, names must be submitted as arrays.
				name_count.append(form.name)
				i = i + 1
			
			cv.add_to_queue("Friend-Q", name_count)				
			message = "Success! You have been added to the queue!"
		else:
			message = "Failure! You are either not on the list or not verified. If you believe this is a mistake please check with the Pairing Committee or somebody on exec board. It is possible that you were not verified after going through training."
		
		#display what new queue looks like and make sure it has their name
		#on it
		new_list = cv.names_no_null("Friend-Q", 1)
		return render.add(stuff = [message, i-1, new_list])


class Remove(object):
	#this is the code for the buttons for friends to 
	#remove themselves from the queue
	def GET(self):
		return render.remove(friendq = 3)
		
	#This requires a rewrite of the function remove_from_queue()
	#so that it allows a more lenient input
	def POST(self):
		form = web.input(name = "name")
		formatted_name = form.name.lower().strip()
		#if someone put there name on there more than 15 times then
		#I think we should just automatically add them to Warrior-Q
		#because they need help 
		cv.remove_from_queue("Friend-Q", formatted_name, 'rm all')
		new_list = cv.queues_as_arrays("Friend-Q")
		return render.remove(friendq = new_list)

if __name__ == '__main__':
	app.run()
