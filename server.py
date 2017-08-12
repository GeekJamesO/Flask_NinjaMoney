from flask import Flask, render_template, session, request, redirect
import random

app = Flask(__name__)
app.secret_key = "h.ufriyw3aq34hiucv"

@app.route("/", methods=["GET"])
def index():
    return render_template('index.html')

@app.route("/process_money", methods=["POST"])
def process():
    gold = 0
    newgold = 0
    try:
        gold = session['gold']
    except Exception as e:
        session['gold'] = 0

    try:
        temp = session['messages']
    except Exception as e:
        session['messages'] = ["no Message", "non messages"]

    verb = request.form['building']
    if (verb == "farm"):
        newgold = random.randrange(10,20)
    elif (verb == "cave"):
        newgold = random.randrange(5,10)
    elif (verb == "house"):
        newgold = random.randrange(2,5)
    elif (verb == "casino"):
        newgold = random.randrange(0,50)
    else:
        print "Something is wrong, I don't know what verb '{0}' is.".format(verb)

    gold += newgold
    session['gold'] = gold
    msgString = "process {0}, added {1} gold for a total of {2}".format(verb, newgold, gold)
    session['messages'] = [msgString] + session['messages']
    print msgString
    return redirect('/')


@app.route("/reset", methods=["POST"])
def reset():
    print "reset"
    session['gold'] = 0
    session['messages'] = ["reset"]
    return redirect('/')

app.run(debug=True)
