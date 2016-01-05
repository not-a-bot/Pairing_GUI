import time
import authenticate as au

#this is for testing atm
def list_available_sheets(gc):
	all_sheets = []
	for sheet in gc.openall():
		all_sheets.append("{}".format(sheet.title))
	return all_sheets

#given a spreadsheet name, opens the spreadsheet
#and returns a sheet that you can manipulate.
def open_sheet(spreadsheet):
	#change into key usage later
	#key = turn_to_key(spreadsheet)

	#turn this into url to some cloud so dont have to
	#show the file on github.
	path2secretfile = '/home/justin/pairing-gui-eee6d5bb7e29.json'
	
	#load authentication with .json file
	#like the file once you open a txt file
	gc = au.LOAD(path2secretfile)
		
	#assume the sheet exists
	sheet = gc.open(spreadsheet).sheet1

	'''
	#list all workbooks you can edit and make sure
	#the user is opening one that they can.
	here = list_available_sheets(gc)
	if spreadsheet in here:
		#sheet = gc.open_by_key(key).sheet1
		sheet = gc.open(spreadsheet).sheet1
	else:
	#if spreadsheet isnt available tell user and give them a
	#list of all the ones that the user can edit.
		return "Spreadsheet is not available.", here
	'''
	return sheet


#list all values in a column below a header
def list_col_values(sheet_name, col_num):
	
	sheet = open_sheet(sheet_name)
	val = sheet.col_values(col_num)
	#google automatically initializes spreadsheets with 100 or 1000
	#empty cells so this will be a very large array of empty values
	#probably (if we dont have a lot of people signed up)
	#remove header
	values = val[1::]
	return values

#test should print first col with empty cells, not first cell tho
#print list_col_values('Test1', 1)

#return list, ignoring empty cells
def names_no_null(sheet_name, col_num):
	array = list_col_values(sheet_name, col_num)
	return [y for y in array if y != '']

#Test same as above but no empties
#print names_no_null('Test1', 1)

#given a sheet name and list of names this function
#writes those names to the sheet in a given column
#im not sure if i even need this function
#this function takes a while and will take about the length 
#of added names in seconds plus however many you want to overwrite
#is that O(n)? someone with a fetish for all things linear should let me know
#NVM you need to use this for add_to_queue
def rewrite_column(sheet_name, col_num, new_list_of_names):
	
	sheet = open_sheet(sheet_name)
	
	#add the new list of names
	i = 0
	while i < len(new_list_of_names):
		sheet.update_cell(i + 2, col_num, new_list_of_names[i])
		#each update_cell takes about 1 second to perform
		#so slow.
		i = i + 1
	
	#then overwrite the next 20 rows just in case, lets assume
	#that the new list of names is no smaller than 20
	#from the old one (plus or minus random empty cells)
	#i will now assume just 10 because we call it when we remove and add
	#so empty cells should not build up over time.
	j = 0
	while j <= 10:
		#use i because you must start from where you left off
		sheet.update_cell(i + 2, col_num, "")
		i = i + 1
		j = j + 1


#test that rewrite works... this is so slow.
#i think its the update_cell function. Its just super slow.
#also col_count is a very large number so we are calling update a lot.
#its still loading after 3 minutes, this is unusable... Good thing
#i havent used it. lol
#rewrite_column('Test1', 5, [5, 44, 63, 27, 8])
#print names_no_null('Test1', 5)


#this is mostly used to search the heading row
#for some value like NAME or NETID
def search_row(sheet, row_num, value):
	#find the first empty row in column 1 to update in.
	array = sheet.row_values(row_num)
	i = 0
	length = len(array)
	while i < length:
		if array[i].lower().strip() == value.lower().strip():
			#this is the number of the row the value is located
			#you MUST do +1 because the array starts at index 0
			#and sheets starts at 1.
			return i + 1
		else:
			i = i + 1
	#means entire thing is full and just start adding at the end
	return length

#this works for any case and with extra spaces
#sheet=open_sheet('Friend-List')
#row = search_row(sheet, 1, 'nAme ')

#im basically using this instead of rewrite so i know where to write
#instead of just aimlessly rewriting the column, however, this method
#only works if you know that there are no random empty cells between names
#using rewrite will work better in that case.
def search_column(sheet, col_num, value):
	#find the first empty row in column 1 to update in.
	array = sheet.col_values(col_num)
	i = 0
	length = len(array)
	while i < length:
		#be aware that this means if you search for an empty cell, a cell
		#with a space in it will also be considered empty (that seems good)
		if array[i].lower().strip() == value.lower().strip():
			#this is the number of the row the value is located
			#you MUST do +1 because the array starts at index 0
			#and sheets starts at 1.
			return i + 1
		else:
			i = i + 1
	#means entire thing is full and just start adding at the end
	return length

#yeah, i searched for john and it didnt show up because my name was
#john d. its harder to standardize name, (FIRst, Last?) but 
#netID will be easier so officially changing it to that now.
#but we would still have to display names instead of netids..
#wed just use netids for adding to queue then add their name to list
#This works btw.
#print search_column(sheet, row, 'john d')

def add_pair(chosen_pair):
	#given a pair, friend, warrior this will add the pair to the
	#current pairings sheet and the all pairings sheet
	#along with a time stamp and in the future a tag showing who
	#paired them.	

	#this assumes a sheet format of col_1 = warrior
	#then friend, then date paired
	for element in ["Current-Pairings", "All-Pairings"]:
		sheet = open_sheet(element)
		

		first_empty_row = search_column(sheet, 1, '')
		
		#once again, 1 is warriror, friend, date
		#given array should be of form, [warrior, friend]
		sheet.update_cell(first_empty_row, 1, chosen_pair[0])
		sheet.update_cell(first_empty_row, 2, chosen_pair[1])
		
		the_time = time.strftime("%m-%d-%y", time.gmtime())
		sheet.update_cell(first_empty_row, 3, the_time)

#test add pair, works. cool. kinda slow, not as bad as rewrite.
#tho i made rewrite better (even though it is never used)
#add_pair(['George', 'Freud'])



#THIS NEEDS TO BE ABLE TO REMOVE NAMEs REGARDLESS OF CASE OR FORMAT
#FIX it is fixed now
def remove_from_queue(sheet_name, name, number=1):
	#this removes a person from a queue a 'number' of times (1 or all)
	#used after they have been paired so dont need to be paired anymore
	#remove only one instance of name so that friends who place themselves
	#on the q multiple times to be paired multiple times dont have all of
	#their names they put on removed

	#return all names in current
	current_names = names_no_null(sheet_name, 1)
	i = 0
	new_names = []
	if number == 1:
		for element in current_names:
			if element.lower().strip() == name.lower().strip() and i==0:
				i = i + 1
			else:
				new_names.append(element.strip())
		#rewrite and nnn both call open_sheet which makes
		#this pretty slow probably, col_num always 1 for a queue
		rewrite_column(sheet_name, 1, new_names)
	else:
		#only change this to no i so it will remove all instances of name
		for element in current_names:
			if element.lower().strip() == name.lower().strip():
				i = i + 1
			else:
				new_names.append(element.strip())
		#rewrite and nnn both call open_sheet which makes
		#this pretty slow probably
		rewrite_column(sheet_name, 1, new_names)

#this works for all upper/lower cases
#remove_from_queue('Friend-Q', 'jessica jones', 3)


#used to add friends who want to be added to queue, maybe also to create
#warrior queue from
#THIS SHOULD USE REWRITE_SHEET BECAUSE THERE IS LIKELY
#TO BE RANDOM EMPTY CELLS IN THE COL FROM REMOVE FUNCTION
def add_to_queue(sheet_name, list_of_names):
	#the queue is in column one
	names = names_no_null(sheet_name, 1)
	for element in list_of_names:
		names.append(element)
	
	#this opens the same sheet twice and is kinda
	#redundant but w.e.
	#rewrite old names with new attatched
	rewrite_column(sheet_name, 1, names)
	
#this test works, along with overwriting blanks in rewrite now (didnt 
#before) because i forgot to increment i again in second loop		
#add_to_queue('Friend-Q', ['Maria', 'Daniel', 'Daniel', 'Daniel'])


