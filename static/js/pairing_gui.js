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


function displayWarriorInfo(warriorName)
{
	var postreq = $.post( "http://0.0.0.0:8080/info", {name: warriorName}, null, 'json')
 		.done(function( data ) {
	   	 var interests = data.interests;
	   	 var hobbies = data.hobbies;
	   	 var struggle = data.struggle;
	   	 $('#warriorModal').find('h1').html(warriorName);
	   	 $('#warriorModal').find('p').html('<p><b>Interests: </b>' + interests + '</p>'
	   	 																		+ '<p><b>Hobbies: </b>' + hobbies + '</p>'
	   	 																		+ '<p><b>Struggles: </b>' + struggle + '</p>');
	   	 $('#warriorModal').modal('show');
		})
		.fail(function(){
			$('#warriorModal').find('h4').html(warriorName);
	   	$('#warriorModal').find('p').html('Could not find any data');
	   	$('#warriorModal').modal('show');
	});
}