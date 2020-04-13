#!C:\Python36Active\python.exe
print ("Content-type:text/html\r\n\r\n")
s = """

<html lang="en">
  <head>
    <title>Mustache.js External Method</title>
    <script type="text/javascript" src="/static/js/jquery.js" ></script>
    <script type="text/javascript" src="/static/js/mustache.js" ></script>
    <script>
    
    $(document).ready(function(){

        $("#div1").load("/templet/tt.html");
        

});

function displayResult() {
            alert($("#div1").text());
}

</script>
</head>


<body>
<button onclick="displayResult()">Change text</button>

<div id="div1"></div>

</body>
</html>
"""

print (s)
