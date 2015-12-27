import os
import time
import authenticate as au

#this is for testing atm
def list_available_sheets(gc)
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
	path2secretfile = '/home/glitch/my_scripts/github/first-eb1baeb00baf.json'
	
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
	val = sheet.row_values(col_num)
	#google automatically initializes spreadsheets with 100 or 1000
	#empty cells so this will be a very large array of empty values
	#probably (if we dont have a lot of people signed up)
	#remove header
	values = val[1::]
	return values

#return list, ignoring empty cells
def names_no_null(sheet_name, col_num):
	array = list_col_values(sheet_name, col_num)
	values = [y for y in array if y != '']
	return values


#given a sheet name and list of names this function
#writes those names to the sheet in a given column
def rewrite_column(sheet_name, col_num, new_list_of_names):
	
	sheet = open_sheet(sheet_name)
	
	#first clear the column.
	j = 0
	while j < sheet.row_count:
		sheet.update_cell(j + 2, col_num, '')
		j = j +1

	#then add the new list of names
	i = 0
	while i < len(new_list_of_names):
		sheet.update_cell(i + 2, col_num, new_list_of_names[i])
		i = i +1


def add_pair(chosen_pair):
	#given a pair, friend, warrior this will add the pair to the
	#current pairings sheet and the all pairings sheet
	#along with a time stamp and in the future a tag showing who
	#paired them.	

	#this assumes a sheet format of col_1 = warrior
	#then friend, then date paired
	for element in ["Current-Pairings", "All-Pairings"]:
		sheet = open_sheet(element)
		
		#find the first empty row to update in.
		array = sheet.row_values(1)
		i = 0
		length = len(array)
		while i < length:
			if array[i] == '':
				first_empty_row = i	
				i = length
			else:
				i = i + 1
		#once again, 1 is warriror, friend, date
		#given array should be of form, [warrior, friend]
		sheet.update_cell(first_empty_row, 1, chosen_pair[0])
		sheet.update_cell(first_empty_row, 2, chosen_pair[1])
		
		the_time = time.strftime("%m-%d-%y", time.gmtime())
		sheet.update_cell(first_empty_row, 3, the_time)

		

def remove_from_queue(sheet_name, name, number=1):
	#this removes a person from a queue a 'number' of times (1 or all)
	#used after they have been paired so dont need to be paired anymore
	#remove only one instance of name so that friends who place themselves
	#on the q multiple times to be paired multiple times dont have all of
	#their names they put on removed
	sheet = open_sheet(sheet_name)
	if number == 1:
		#this requires perfect case though..
		#ill get to it later,
		#THIS IS FOR Q SO COL_NUM IS 1!!!!
		#later, find name col. then search each cell.lower().strip()
		#if matches given name.lower().strip() then remove
		cell = sheet.find(name)
		sheet.update_cell(cell.row, cell.col, '')
	else:
		cell_list = sheet.findall(name)
		for cell in cell_list:
			sheet.update_cell(cell.row, cell.col, '')

#used to add friends who want to be added to queue, maybe also to create
#warrior queue from
#array of names without \n at the end already
def add_to_queue(sheet_name, list_of_names):
	names = names_no_null(sheet_name)
	#this is redundant but w.e.
	sheet = open_sheet()
	for name in list_of_names:
		names.append(name + '\n')
	rewrite_sheet(sheet_name, names)
		



