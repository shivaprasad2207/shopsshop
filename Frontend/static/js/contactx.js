function delSelected (){
	var allCheckBoxObj = document.querySelectorAll("[name^=chkBox_]");
	var index, len;
	for (index = 0, len = allCheckBoxObj.length; index < len; ++index) {
		alert (allCheckBoxObj[index].value);
	} 
}