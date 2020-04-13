

function showModifyContactForm(contact_id){
	window.location ='/cgi-bin/Contacts/contacts.py?appParam=showModifyContactForm&contact_id='+ contact_id ;	
}

function showPasswordChangeForm(){
		window.location ='/cgi-bin/Contacts/contacts.py?appParam=showPasswordChangeForm';
}
function loginPage (){
	window.location ='/cgi-bin/Contacts/contacts.py'
}

function changeUserInfo (){
		var params = $("#userIfno").serialize();
		window.location ='/cgi-bin/Contacts/contacts.py?appParam=changeUserInfo&'+params;
}
function showUserInfoChangeForm(){
		window.location ='/cgi-bin/Contacts/contacts.py?appParam=showUserInfoChangeForm';
}

function showNewUserForm (){
	window.location ='/cgi-bin/Contacts/contacts.py?appParam=showNewUserForm' ;

}
function addNewUserToApp (){
		var params = $("#newUser").serialize();
		window.location ='/cgi-bin/Contacts/contacts.py?appParam=addNewUserToApp&' + params ;
}	
	
function showLoginPage (){
	window.location ='/cgi-bin/Contacts/contacts.py'
}

function delContact(contact_id){
	window.location ='/cgi-bin/Contacts/contacts.py?appParam=delContact&contact_id='+ contact_id ;	
}

function showContactAddForm (){
    window.location ='/cgi-bin/Contacts/contacts.py?appParam=showContactAddForm' ;
}

function showContactList(){
	window.location ='/cgi-bin/Contacts/contacts.py?appParam=showContactList' ;
}

function showSearchForm (){
		window.location ='/cgi-bin/Contacts/contacts.py?appParam=showSearchForm'
}

function delSelected (){
	var allCheckBoxObj = document.querySelectorAll("[name^=chkBox_]");
	var index, len;
	var contact_ids= []; 
	for (index = 0, len = allCheckBoxObj.length; index < len; ++index) {
		if(allCheckBoxObj[index].checked){
			contact_ids.push(allCheckBoxObj[index].value);
      }
	} 
	window.location ='/cgi-bin/Contacts/contacts.py?appParam=delBulkContacts&contactIDs=' + contact_ids.join(',');
}


function searchContact (){
		var params = $("#searchForm").serialize();
		window.location ='/cgi-bin/Contacts/contacts.py?appParam=searchContact&' + params ;
}

function addContact (){
	var params = $("#contact_details").serialize();
	var url ='/cgi-bin/Contacts/ajaxCalls.py?appParam=addContact&' + params ;
	
	$.get(
                 url,
                 function(data, textStatus, jqXHR) {
						$("#dispset").html('<b style="color:green;"> Contact ADDED </b>');
                    },
                 "html"
            ); 
}

function modifyContact (){
	var params = $("#contact_details_m").serialize();
	var url ='/cgi-bin/Contacts/ajaxCalls.py?appParam=modifyContact&' + params ;		
	$.get(
                 url,
                 function(data, textStatus, jqXHR) {
						$("#dispset").html('<b style="color:green;"> Contact Modified </b>');
                    },
                 "html"
            ); 
}