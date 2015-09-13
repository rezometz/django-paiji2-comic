function _tokeifun(id, legend_id) {
	var date = new Date ;
	var h = date.getHours ();
	if (h < 10) { h = "0"+h ; }
	var m = date.getMinutes ();
	if (m < 10) { m = "0"+m ; }
	var choice = tokei_form.tokei_list.value
	var src = 'http://www.bijint.com/assets/pict/'+choice+'/pc/'+h+m+'.jpg';
	var link = '<a class="logo" href="'+src+'"><img style="width:100%;" src="'+src+'" alt="bijin tokei"/></a>';
	var legend = '<a target="_blank" class="text-center" href="http://www.bijint.com/'+choice+'">bijin tokei : '+choice+'</a>';
	document.getElementById(id).innerHTML = link ;
	document.getElementById(legend_id).innerHTML = legend ;
	return true ;
}

function tokeifun(id, legend_id) {
	_tokeifun(id, legend_id);
	var tokei_interval_ID = window.setInterval(_tokeifun, 60000, id, legend_id);
}
