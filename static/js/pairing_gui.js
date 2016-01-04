function pairClick()
{
	var friendName = document.getElementById('friendQueue').value
	var warriorName = document.getElementById('warriorQueue').value
	console.log(friendName)
	$('#testModal>h3').html('Are you sure you want to pair ' +friendName+' (Friend) with '+warriorName+' (Warrior)?');
	$('#testModal').modal('show');
}