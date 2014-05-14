import re
from random import randint
from flask import Flask
from flask import request
from flask import render_template

app = Flask(__name__)

s = "I'm fairly new to {ASP.NET|PHP|Node.js|Python|Ruby|Golang}, I have just uploaded my files via {FileZilla|Cyberduck|SSH|Rsync|Form|CPANEL} but my {web config|settings|config|yaml} file isn't in the {root|top directory|same path} & it doesn't seem to be anywhere. {How can I retrieve it again?|How can I find my missing file?|How do I edit my .gitignore?}"

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
    if doh:
        spun = spinner(doh)
        return spun
    else:
        return spinner(s)
  else:
    return render_template('index.html', example = s, spun=spinner(s)) 

if __name__ == "__main__":
    app.run()