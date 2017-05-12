from flask import Flask, render_template, request, redirect, session, Markup
import random
import datetime
app = Flask(__name__)

app.secret_key = 'ThisIsSecret'
goldNum = 0
pTag = ''

@app.route('/')
def index():
    return render_template('index.html', gold=goldNum, tags=pTag)

@app.route('/process_money', methods=['POST'])
def process():
    global goldNum
    global pTag
    if 'farm' in request.form:
        randomNum = random.randrange(10,21)
        goldNum += randomNum
        pTag += '<p>Earned ' + str(randomNum) +' gold from farm!</p>'
    if 'cave' in request.form:
        randomNum = random.randrange(5,11)
        goldNum += randomNum
        pTag += '<p>Earned ' + str(randomNum) +' gold from cave!</p>'
    if 'house' in request.form:
        randomNum = random.randrange(2,6)
        goldNum += randomNum
        pTag += '<p>Earned ' + str(randomNum) +' gold from house!</p>'
    if 'casino' in request.form:
        randomNum = random.randrange(-50,51)
        goldNum += randomNum
        if randomNum > 0:
            pTag += '<p>Earned ' + str(randomNum) +' gold from casino!</p>'
        else:
            pTag += '<p>Lost ' + str(abs(randomNum)) +' gold from casino!</p>'
        if goldNum < 0:
            goldNum = 0
    return redirect('/')

app.run(debug = True)

# tags = Markup("<p>some text here</p>")
