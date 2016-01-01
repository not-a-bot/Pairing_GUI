#PAIRING GUI and SHEET ORGANIZER

This repository is the initial workings of an interface to simplify the
pairing process for Open Ears. People who are seeking help are nicknamed
'warriors' to simplify the coding and members of our organization who 
are giving the help are 'friends.'


###THE PROCESS

Let's start with the friends. If a friend has gone through training and
has been verified, they can then add themselves to a 
queue from the /add page. Once they add themselves to the queue we will
know they are available to help a certain amount of people
(however many they put down). At any point, they may remove themselves 
from this queue. This will let us know that they are not capable of being
paired with anymore warriors at the moment for whatever reason. Be it school
work is piling up, they are beginning to feel mentally drained, etc.

Now, there is also a list of people who want to be helped, warriors. All warriors
on this list are automatically added to the queue, setting them up to 
be helped by a friend.
Someone in the commmittee will see both the queues and pair someone in the 
warrior queue with someone in the friends queue. This removes both people from
the queues and adds them as a pair to the list of current pairings and all time
pairings along with the date that they were paired. 
Once the warrior is finished being helped, the pair is removed from
current pairings, but remains in all as a history of all people helped.
(This code still needs to be done.)


###"I WANT TO USE THIS!"

openearsuiuc@gmail.com has been authorized to use the drive API with google.
This means you do not have to go through the process of authorizing and sharing
with your own account. Just go to the Open Ears Exec folder. Open GUI_Interface
and download the .json file in there. It may be named pairing-gui or
open-service with a lot of numbers and letters after it, I'm not sure which one
it is. Download that file then change the path2secretfile variable in convey.py
in the function open_sheet point to wherever you store the .json file. If you 
did all of this correctly you should now be able to edit sheets and everything
should be working.


##NOTES


###REGARDING STUFF
Only friends who are trained may be added to the queue. The pairing happens
before the pair ever meets, so if someone gets cold feet then after a certain
amount of time they will be removed from the current pairings, but will remain
in all pairings with a description of what happened. 
It would be nice if all pairings  would change inactive pairs to red 
and have active as greeen. (This is something to consider onces google 
sheets integration is complete.)
It is up to committe to manually place in reason pair ended, 
at the moment. We could create another interface that lets committee 
members end pairs and add reason.


###REGARDING SHEET FORMATS
Current and All pairings must be formated as warrior, friend, date paired as
their columns, in that order. The 
queues must both conatain the names of people in the queue in the first column.
All sheets require headers in the first row, any values placed in the first
row will not be read. We also have the added pair be written to the row
with the first empty space in column one. So if you remove a pair from current
pair please make the entire row blank or remove the whole row. If you have
a blank cell in the first column for a pair you want to keep it will likely
be overwritten at some point.

As of now the queues MUST BE FIRST NAME ONLY (corresponding to a netid
in the frieds list). If they have full names on it 
everything breaks. So the name question in friends list must be one name. 
Ill change the code to search for first name or something like that. That means
we also need to validate that the first names are really just one name without
a space this can be done either in the google form or somewhere in this code.

For friend and warrior list, we need three columns 'Name' 'netID' and 
'Verified.' Everything under the name column MUST BE A FIRST NAME. That
is it must be a single word name. No spaces!! (Itd be best to mandate this
in the forms using data validation.) Under netId that is their netids. And
under verification it should say 'yes' if they are verified. Anything else
reads as they are not verified. For all of these, capitilization and extra
spaces before or after should not matter.
(THIS IS ALL VERY LIKELY TO CHANGE. SO ASK IF YOU
ARE UNSURE ASK! WE ARE HELPUL PEOPLE! I SWEAR!)



###REGARDING SUPER SECRET SENSITIVE INFORMATION
You need a .json file to authenticate yourself as able to use drive API.
Right now I am using my own email but I plan on swithing it to our 
open ears gmail. I stored the .json file one above the directory because
it contains sensitive information on account info so it shouldn't be public.
Idk how we will implement this in the future since everything is hosted
publicly. Maybe store the .json in a secure cloud, but the problem remains
that our public scripts still need to be able to access them and so anyone
would still be able to access them.


###ITS NOT A SCIENCE!
Something about how we need tests and people to break things and fix them
because this was not thoruoughly tested the first time and the second
rewrite of it (this version) I did not even check if a lot of it worked while
making it. Theres documentation in the gspread docs on how to test with nose.
You have to use a test.config sheet in gsheets but idk how to do it so help
would be nice.


I really hope that after I make this that it DOES NOT break horrendously in the future.
That'd be no bueno. (aaaaaaaaaaand its all deleted the next day... yay.
i should stop writing things like this in my code. bad omens)


###so sad
This is actually a rewrite of the original gspread code. Why is it a rewrite?
Because either my computer did not save my local change for some reason 
(it was being pretty glitchy last night) or the pull request I did from 
the master caused an overwrite of all my local files. I don't know if 
this is the reason though becuase I copied the directory before doing it and 
the copy only contained two functions with sheet functionality in convey.py, 
(which i just remember I had changed to conveyor.py so something mustve gone 
wonky with my computer...)
