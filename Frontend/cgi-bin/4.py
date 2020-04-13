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
        var t = $("#div1").load("/templet/tt.html").text();
        var view = {
            name : "Joe",
            occupation : "Web Developer"
        };
        //alert (t);
        var output = Mustache.render($("#div1").text(), view);
        //alert (output);
        document.getElementById('div1').innerHTML = output;
});


</script>
</head>


<body>

<div id="div1"></div>

</body>
</html>
"""

print (s)
