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
</head>
<body>

<nav class="navbar navbar-expand-sm bg-dark navbar-dark">

  
</nav>

<nav role="main" class="col-md-6 col-lg-5 pt-1 px-4">
<form class="form-signin">
              <div class="form-label-group">
                <input type="text" id="inputEmail"  placeholder="Email address" required autofocus>
              </div>

              <div class="form-label-group">
                <input type="password" id="inputPassword"  placeholder="Password" required>
              </div>
              <a class="btn btn-lg btn-primary text-uppercase" onclick="javascript:admin_signin();return false;" >Sign in</a>
        
</form>  
</nav>


</body>
</html>
"""


print (s)
