from flask import Flask,render_template,request,make_response
from multiprocessing import Value

app = Flask(__name__)
counter = Value('i', 0)


@app.route("/")
def hello():
    return "Hello World from Flask in a uWSGI Nginx Docker container with Python 3.7 (from the example template)"

@app.route("/validate/",methods = ['POST','GET'])
def inputValPage():
    if request.method == 'GET':
        return render_template('inputval.html')
    if request.method == 'POST':
        result = request.form
        if (str(request.form['in']) == 'MONSEC'):
            return 'M0NS3C{bYp4ss3d}'
        else:
            return 'n00b'

@app.route("/user-agent/")
def userAgentHax():
    if('Googlebot' in request.headers.get('User-Agent')):
        return 'wow, google can you give me a job?? M0NS3C{Us3rs_4rnT_Ag4ntZ}'
    else:
        return 'This site is so secure only the robots at google can see my flags, and i dont even use robots.txt!!'
@app.route("/antibot/")
def antibotPage():
    return '<a href="/antibot/getCookie/"> Click here to get a cookie </a>  <br> <a href="/antibot/counter/"> Click here to try your hand at winning! </a>'  
@app.route("/antibot/getCookie/")
def cookie():  
    res = make_response("<h1>cookie is set</h1>")  
    res.set_cookie('foo','bar')  
    return res
@app.route("/antibot/counter/")
def counterPage():
    if(request.cookies.get('foo') != 'bar'):
        return "HEY, YOU DON'T HAVE A COOKIE... YOU'RE NOT A HUMAN!!!!"
    else:
        with counter.get_lock():
            counter.value += 1
            if(counter.value % 1000 == 0):
                return ("Congrats! You are the "+ str(counter.value) +"th User! The flag is: M0NS3C{C0UNT3D}")
            else:
                 return("Sad! You are the "+str(counter.value)+"th user. Come back when you're a multiple of 1000")

@app.route("/blind-guess/",methods=['POST','GET'])
def blindPage():
    if request.method == 'POST':
        result = request.form['in']
        if result in 'm0ns3c1s44gu44s':
            return 'Yes'
        else:
            return 'No'
    if request.method =='GET':
        return render_template('guessingGame.html')


if __name__ == "__main__":
    # Only for debugging while developing
    app.run(host='0.0.0.0', debug=False, port=80)
