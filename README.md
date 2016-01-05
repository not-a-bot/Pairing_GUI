#Open Ears Pairing

Open Ears pairing interface for pairing those who want someone to talk to with people who want to listen.

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
Available pages are:

  * /pairing_gui - pairing interface
  * /add - add self to the queue
  * /remove - remove self from the queue

  example: `http://0.0.0.0:8080/pairing_gui`

##Pages

####Pairing

`http://0.0.0.0:8080/paring_gui`
Someone in the Pairing Commmittee will see both of the queues and pair 
a warrior with a friend. This removes both people from
the queues and adds them as a pair to Current-Pairings and All-Pairings
along with the date that they were paired. 
####Add
Let's start with the friends. If a friend has gone through training and
has been verified, they can add themselves to a 
queue from the /add page. Once they add themselves to the queue the 
Pairing Committee will
know they are available to help a certain number of people
(however many they put down). 

####Remove
At any point, they may remove themselves 
from this queue. This will let us know that they are not capable of being
paired with anymore warriors at the moment for whatever reason. Be it school
work is piling up, they are beginning to feel mentally drained, etc.


####ANOTHER HOLE
Once the warrior is finished being helped, the pair is removed from
current pairings, but remains in the all pairings list so that we have
a record of everyone that we have helped and who helped who. This must
currently be done manually.



##Notes

* Only friends who are trained may add themselves to the queue. 

The pairing happens before the pair ever meets, so if someone gets cold feet then after a certain
amount of time they will be removed from the current pairings, but will remain
in all pairings with a description of what happened.
It would be nice if all pairings  would change inactive pairs to red 
and have active as greeen. (This is something to consider onces google 
sheets integration is complete.)
It is up to committe to manually place in reason pair ended, 
at the moment. We could create another interface that lets committee 
members end pairs and add reason.


###Sheet Formats
Current and All Pairings:
Columns must be organized as: Warrior - Friend - Date

Queues:
Single Column of Names
Current and All pairings must be formated as warrior, friend, date paired as

For friend and warrior list, we need three columns 'Name' 'netID' and 
'Verified.' The name under name column can be first, first/last, or whatever.
Under netId that is their netids. And
under verification it should say 'yes' if they are verified. Anything else
reads as they are not verified. For all of these, capitilization and extra
spaces before or after should not matter.


