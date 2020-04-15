#!C:\Python36Active\python.exe

print ("Content-type:text/html\r\n\r\n")
s = """

<!DOCTYPE html>
<html lang="en">
<head>
  <title>Login Shop Admin</title>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <link rel="stylesheet" href="/static/css/bootstrap.css">
  <script src="/static/js/jquery.js"></script>
  <script type="text/javascript" src="/static/js/mustache.js" ></script>
  <script type="text/javascript" src="/static/js/me.js" ></script>
  <script src="/static/js/jquery.min.js"></script>
  <script src="/static/js/popper.js"></script>
  <script src="/static/js/bootstrap.js"></script>
  <script src="/static/js/admin.js"></script>
  <script src="/static/js/login.js"></script>
</head>
<body>

<nav class="navbar navbar-expand-sm bg-dark navbar-dark">
</nav>

<nav role="main" class="col-md-6 col-lg-5 pt-1 px-4">
<table class="table-bordered">

<tr>
<td>
<label> <b>Shop Admin Login</b></label><br>

<table> <tr> <td>
   <a class="btn btn-sm btn-primary text-uppercase" onclick="javascript:get_admin_login_form();return false;" >User login</a>  
</td> </tr>  </table>
<td>
 <div id="admin_login">  </div>
</td>
</tr>

<tr>
 <td>
  
  <label><b> Create a Shop</b> </label>
  <table>
  <tr> <td>
    <a class="btn btn-sm btn-primary text-uppercase" onclick="javascript:get_store_register_form();return false;" >Shop Register</a>
   </td> </tr>
  </table> 
  
  </td>
   <td>
  <div id="store_create"> </div>
  </td> 
  </tr>

</td>
</tr>


<tr>
 <td>
  
  <label><b> User Register </b> </label>
  <table>
  <tr> <td>
    <a class="btn btn-sm btn-primary text-uppercase" onclick="javascript:get_user_register_form();return false;" >User Register</a>
   </td> </tr>
  </table> 
  
  </td>
   <td>
  <div id="usr_create"> </div>
  </td> 
  </tr>

</td>
</tr>


<tr>
 <td>
  
  <label><b> User Login </b> </label>
  <table>
  <tr> <td>
   <a class="btn btn-sm btn-primary text-uppercase" onclick="javascript:get_user_login_form();return false;" >User login</a>  
   </td> </tr>
  </table> 
  
  </td>
   <td>
   <div id="usr_login"> </div>
  </td> 
  </tr>

</td>
</tr>



</table>

</body>
</html>
"""


print (s)
