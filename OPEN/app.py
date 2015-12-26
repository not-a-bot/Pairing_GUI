import web
import convey as cv

urls = (
	'/pairing_gui', 'Pairing',
	'/add', 'Add',
	'/remove', 'Remove'
)

app = web.application(urls, globals())
render = web.template.render('templates/')


friendq  = cv.queues_as_arrays("Friend-Q")
warriorq = cv.queues_as_arrays("Warrior-Q")


class Pairing(object):
	def GET(self):
	#once /Pairing webpage is loaded the GET method
	#renders the pairing gui.html from the templates folder

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

		chosen_pair = [form.friend, form.warrior]	
		#will be finished in future
		#doesnt return anything, just updates sheets

		cv.add_pair(chosen_pair)
		cv.remove_from_queue("Friend-Q", form.friend + '\n')
		cv.remove_from_queue("Warrior-Q", form.warrior + '\n')

		#redownload queues to display updated versions.
		friendq  = cv.queues_as_arrays("Friend-Q")
		warriorq = cv.queues_as_arrays("Warrior-Q")
		this = [chosen_pair, friendq, warriorq]
	
#once all the form stuff is complete this will render
#the display html and show the new queues and the
#pair of people you added to current pairs
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
		
	def POST(self):	
		ver = 0
		i = 1
		#im assuming this means the default setting is 1
		form = web.input(name = "name", number = 1)
		bowl = form.name.lower().strip() + ' ' + 'yes' + '\n'
		print form.number
		print form.name
		print bowl
		
		num = int(form.number)
		print num
		
		#check that they are on friend list AND verified
		the_list = cv.queues_as_arrays("Friend-List")
		print the_list	
		for lines in the_list:
			if bowl == lines:
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
			message = "Success!"
		else:
			message = "Failure! You are either not on the list or not verified. If you believe this is a mistake please check with the Pairing Committee or somebody on exec board. It is possible that you were not verified after going through training."
		
		#display what new queue looks like and make sure it has their name
		#on it
		new_list = cv.queues_as_arrays("Friend-Q")
		return render.add(stuff = [message, i-1, new_list])


class Remove(object):
	#this is the code for the buttons for friends to 
	#remove themselves from the queue
	def GET(self):
		return render.remove(friendq = 3)
		
	def POST(self):
		form = web.input(name = "name")
		bowl = form.name.lower().strip() + '\n'
		#if someone put there name on there more than 15 times then
		#I think we should just automatically add them to Warrior-Q
		#because they need help 
		cv.remove_from_queue("Friend-Q", bowl, 15)
		new_list = cv.queues_as_arrays("Friend-Q")
		return render.remove(friendq = new_list)

if __name__ == '__main__':
	app.run()
