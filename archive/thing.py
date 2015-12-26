#take two lists of people. user pairs someone in first list
#with someone in the second list
#it will remove those people from original lists and 
#add them to a new list, the queue.


#assume names are already properly formatted
def pair(nh_q, f_q, current_pairings):
	new_list_one = []
	new_list_two = []

	print "Needs help: ", nh_q
	print "Friends: ", f_q

	print "Pair someone in first list with someone in second list."
	print "please use only lower case letters."
	needs_help = str(raw_input("NH: "))
	friend = str(raw_input("friend: "))

	#create the new lists for queue without people paired 
	for element in nh_q:
		if element != needs_help:
			new_list_one.append(element)
	for element in f_q:
		if element != friend:
			new_list_two.append(element)
	
	#add people to the list of people currently paired
	current_pairings.append([needs_help, friend])

	return new_list_one, new_list_two, current_pairings


def main():
	list_one = ['john','barb','sandy','bob','harry']
	list_two = ['max','jazzy','charles']
	paired = [['jose','julie'],['karl', 'brittni']]

	stuff = pair(list_one, list_two, paired)

	for element in stuff:
		print element

if __name__ == "__main__":
	main()
