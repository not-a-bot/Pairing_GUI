from nose.tools import *

import OPEN
from OPEN import convey as cv

def test_remove_newlines():
	print "Test: remove_newlines"
	print "removes \\n characters from the end of matrix elements"

	matrix = ['this is\\n','incredible\\n','is it not\\n', '\\n']
	desired_result = ['this is','incredible','is it not', '']
	thing = cv.remove_newlines(matrix)
	assert_equal(thing, desired_result)

#test for list lines as well
def test_queues_as_arrays():
	print "Test: list_lines"
	print "lists all lines in a .txt file"

	result = cv.list_lines('test')
	desired_result = [  'Arnold',
						'I will be back',
						'yes',
						'kanye',
						'kim',
						'north by north West']
	assert_equal(result, desired_result)

def test_rewrite_sheet():
	import random
	print "Test: rewrite_sheet"
	print "given a sheet in /spreadsheets and an array of names"
	print 'rewrites the sheet to contain those names in array'

	#randomly add choices to list so that the test file doesnt
	#assert equal when failed because writing the same thing
	choices = ['michael', 'Harris', 'Gonzu', 'Yolo', 
				'hiro', 'MAx', 'kyle', 'Hank', 'Crazy Kat']
	names = []
	for i in random.randrange(8):
		names.append(choices[i])

	cv.rewrite_sheet('test2', names)

	assert_equal(cv.list_lines('test2'), names)



	


