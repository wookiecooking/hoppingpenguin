import re
from random import randint
from flask import Flask
from flask import request

app = Flask(__name__)

def select(m):
    choices = m.group(1).split('|')
    return choices[randint(0, len(choices)-1)]

def spinner(s):
    r = re.compile('{([^{}]*)}')
    while True:
        s, n = r.subn(select, s)
        if n == 0: break
    return s.strip()

@app.route("/", methods=['POST','GET'])
def hello():
  if request.method == 'POST':
    doh = request.form['content']
    spun = spinner(doh)
    return '''<h1>hoppingpenguin</h1><b>Example: </b><span>I'm fairly new to {ASP.NET|PHP|Node.js|Python|Ruby|Golang}, I have just uploaded my files via {FileZilla|Cyberduck|SSH|Rsync|Form|CPANEL} but my {web config|settings|config|yaml} file isn't in the {root|top directory|same path} & it doesn't seem to be anywhere. {How can I retrieve it again?|How can I find my missing file?|How do I edit my .gitignore?}</span><br><br><b>Returns: </b><span>I'm fairly new to Ruby, I have just uploaded my files via CPANEL but my web config file isn't in the same path & it doesn't seem to be anywhere. How can I find my missing file?</span><br><br><form action="/" method=post enctype=multipart/form-data><textarea name=content style="width:100%;height:200px"></textarea><br><input type=submit value=Submit></form><h1>Results:</h1><hr>'''+spun
  else:
    return '''<h1>hoppingpenguin</h1><b>Example: </b><span>I'm fairly new to {ASP.NET|PHP|Node.js|Python|Ruby|Golang}, I have just uploaded my files via {FileZilla|Cyberduck|SSH|Rsync|Form|CPANEL} but my {web config|settings|config|yaml} file isn't in the {root|top directory|same path} & it doesn't seem to be anywhere. {How can I retrieve it again?|How can I find my missing file?|How do I edit my .gitignore?}</span><br><br><b>Returns: </b><span>I'm fairly new to Ruby, I have just uploaded my files via CPANEL but my web config file isn't in the same path & it doesn't seem to be anywhere. How can I find my missing file?</span><br><br><form action="/" method=post enctype=multipart/form-data><textarea name=content style="width:100%;height:200px"></textarea><br><input type=submit value=Submit></form><h1>Results:</h1>'''

if __name__ == "__main__":
    app.run()