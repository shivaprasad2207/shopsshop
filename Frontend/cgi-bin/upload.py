#!C:\Python36Active\python.exe
import cgi, os
import cgitb; cgitb.enable()
import json

try: # Windows needs stdio set for binary mode.
    import msvcrt
    msvcrt.setmode (0, os.O_BINARY) # stdin  = 0
    msvcrt.setmode (1, os.O_BINARY) # stdout = 1
except ImportError:
    pass

form = cgi.FieldStorage()

# A nested FieldStorage instance holds the file
fileitem = form['file']
rfile = form['rfile'].value
# Test if the file was uploaded
if fileitem.filename:

    # strip leading path from file name
    # to avoid directory traversal attacks
    root_name = 'htdocs'
    image_location = '/static/images/shopsshps/'
    path = os.path.dirname(os.path.realpath(__file__))
    path_r = path.replace('cgi-bin', root_name + image_location )
    fn = os.path.basename(fileitem.filename)
    rf = fileitem.filename
    open( path_r + rfile , 'wb+').write(fileitem.file.read())
    message = 'The file "' + fn + '" was uploaded successfully'

else:
    message = 'No file was uploaded'

print ("Content-type: application/json")
print ()
response={'status':'ok'}
print(json.JSONEncoder().encode(response))