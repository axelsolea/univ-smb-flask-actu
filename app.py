# save this as app.py
from flask import Flask, render_template, json, request, jsonify

app = Flask(__name__)

@app.route("/")
def concerts():
    f = open("static/concerts.json")
    jsonloade = json.load(f)
    f.close()
    return render_template('concerts.html', jsonloade=jsonloade)

@app.route("/actu")
def actu():
    return render_template('actu.html')

@app.route("/jazz", methods=['GET','POST'])
def jazz():
    if request.method == 'POST':
        return sent_comment()
    f = open("static/jazz.json")
    jsonloade = json.load(f)
    f.close()
    f = open("static/jazz_comments.json")
    json_comments = json.load(f)
    f.close()
    return render_template('jazz.html', jsonloade=jsonloade, json_comments=json_comments)

def sent_comment():
    with open('static/jazz_comments.json', 'r+') as f:
        json_comments = json.load(f)
        print(json_comments)
        json_comments.append({"nom" : str(request.form["nom"]), "message" : str(request.form["message"])})
        jsonify(json_comments)
        json.dump(json_comments, f)
        return render_template('jazz.html')


@app.route("/rock")
def rock():
    f = open("static/rock.json")
    jsonloade = json.load(f)
    f.close()
    return render_template('rock.html', jsonloade=jsonloade)

@app.route("/electro")
def electro():
    f = open("static/electro.json")
    jsonloade = json.load(f)
    f.close()
    return render_template('electro.html', jsonloade=jsonloade)