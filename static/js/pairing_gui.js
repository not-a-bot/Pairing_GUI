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
	var postreq = $.post( "http://0.0.0.0:8080/warriorinfo", {name: warriorName}, null, 'json')
 		.done(function( data ) {
 			 var sex = data.sex;
 			 var year = data.year;
	   	 var interests = data.interests;
	   	 var hobbies = data.hobbies;
	   	 var struggle = data.struggle;
	   	 $('#userModal').find('h1').html(warriorName);
	   	 $('#userModal').find('p').html('<p><p><b> Sex/Gender: </b>' + sex + '</p>'
	   	 																		+ '<p><b>Year: </b>' + year + '</p>'
	   	 																		+ '<p><b>Interests: </b>' + interests + '</p>'
	   	 																		+ '<p><b>Hobbies: </b>' + hobbies + '</p>'
	   	 																		+ '<p><b>Struggles: </b>' + struggle + '</p>');
	   	 $('#userModal').modal('show');
		})
		.fail(function(){
			$('#userModal').find('h4').html(warriorName);
	   	$('#userModal').find('p').html('Could not find any data');
	   	$('#userModal').modal('show');
	});
}

function displayFriendInfo(friendName)
{
	var postreq = $.post( "http://0.0.0.0:8080/friendinfo", {name: friendName}, null, 'json')
 		.done(function( data ) {
 			 var sex = data.sex
 			 var year = data.year
 			 var major = data.major
	   	 var interests = data.interests;
	   	 var hobbies = data.hobbies;
	   	 $('#userModal').find('h1').html(friendName);
	   	 $('#userModal').find('p').html('<p><p><b>Sex/Gender: </b>' + sex + '</p>'
	   	 																		+ '<p><b>Year: </b>' + year + '</p>'
	   	 																		+ '<p><b>Major: </b>' + major + '</p>'
	   	 																		+ '<p><b>Interests: </b>' + interests + '</p>'
	   	 																		+ '<p><b>Hobbies: </b>' + hobbies + '</p>');
	   	 $('#userModal').modal('show');
		})
		.fail(function(){
			$('#userModal').find('h4').html(friendName);
	   	$('#userModal').find('p').html('Could not find any data');
	   	$('#userModal').modal('show');
	});
}