#Open Ears Pairing

Open Ears pairing interface for pairing those who want someone to talk to with people who want to listen.
The pairing interface is to be used to manage the queues for those who want to help/be helped and facilitate pairing by the pairing committee.

##Usage
###Requirements
 * python2
 * web.py
 * gspread
 * oauth2client

###Walkthrough
1. Ensure you have the required packages.

2. Download the .json file from the Open Ears google drive under Pairing-GUI

3. Create a file named path2secretfile.txt in main directory and put the path to the .json file in it (follow template)

```
pairing_gui
 |OPEN
 |static
 |templates
 |path2secretfile.txt
 |todo.txt
```

4. Run app.py from the main directory
  `python2.7 OPEN/app.py`
  
5.  Navigate to ```0.0.0.0:8080/pageToVisit``` in your web browser
	(localhost:8080 is completely valid as well)
Available pages are:

  * /interface - pairing interface
  * /add       - add self to the queue
  * /remove    - remove self from the queue
  * /end_pair  - end the current pairing

  example: `http://0.0.0.0:8080/add`

  NOTE: You may have to replace http://0.0.0.0:8080 with http://127.0.0.1:8080
	    or localhost:8080

##Pages

####Pairing

`http://0.0.0.0:8080/interface`

Someone in the Pairing Commmittee will see both of the queues and pair 
a warrior with a friend. This removes both people from
the queues and adds them as a pair to Current-Pairings and All-Pairings
along with the date that they were paired. 

####Add

`http://0.0.0.0:8080/add`

If a friend has gone through training and
has been verified, they can add themselves to the friend
queue from the /add page. Once they add themselves to the queue the 
Pairing Committee will know that
they are available to help a certain number of people
(however many they put down). 

####Remove

`http://0.0.0.0:8080/remove`

At any point a friend may remove themselves from the friend queue. 
This will let the Pairing Committee know that they are  incapable of being
paired with anymore warriors at the moment. The reason does not matter.Be it school
work is piling up, they are beginning to feel mentally drained, etc.

####EndPair

`http://0.0.0.0:8080/end_pair`

Once a pair is finished actively (definition currently fluid) meeting, the
friend will go to this page and mark the pair as inactive, including
any notes of significance. The pair is removed from the Current-Pairings sheet, 
but remains in the All-Pairings sheet so that we have
a record of everyone that we have helped and who helped who.

This is done by having the friend type in their netID and selecting
their warrior's name from a drop-down list.



##Notes

* Be careful that any html files you edit are indented properly. Improper
indentation results in the custom .css for the page to not load properly.
The reason is unkown and may just be a correlation.

* Only friends who are trained may add themselves to the queue. 

* For emphasis, The ending of a pair must be done for every warrior a 
friend is assigned too. Since the actual act of pairing occurs 
before the pair ever meets,
then even a pair that has never met (example: warrior gets cold feet)
must still be removed from Current-Pairings by the friend.

* Unfortunately, gspread does not allow formatting of updated data.
Therefore active and inactive pairs must be changed to red or green
manually, if we still wish to do this.



###Necessary Sheet Format
Columns must be organized as:

	Current-Pairings: Warrior - Friend - Start Date
	    All-Pairings: Warrior - Friend - Start Date - End Date - [Extra Col] - [Extra Col] - Notes
			  Queues: Single Column of Names


For Friend-List and Warrior-List we need three columns 'Name' 'netID' and 
'Verified.' These columns can be located anywhere in the first row, 
but they MUST be spelled this way. (capitalization does not matter)

(The location of other columns like sex and major are important as well
but the current necessary location of theses are still being worked out.)

The name under the name column may be first, first+last, or whatever.
Under netId that is their netids (no spaces).
Under 'Verified' it should say 'yes' if they are verified. ANYTHING else
means they are not verified. For all of these, capitilization and extra
spaces before or after should not matter.
