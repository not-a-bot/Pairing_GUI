function pairClick()
{
	var friendName = document.getElementById('friendQueue').value;
	var warriorName = document.getElementById('warriorQueue').value;
	if(friendName == '--friend--' || warriorName == '--warrior--'){
		$('#testModal').find('h3').html('<font color="red">Invalid Pairing</font>');
	}
	else{
		$('#testModal').find('h3').html('<p style="text-align:center">Are you sure you want to pair: </p><p style="text-align:center"> <font color="green">' 
																	+friendName+' (Friend)</font> and <font color="red">'
																	+warriorName+' (Warrior) </font></p>');
	}
	$('#testModal').modal('show');
}