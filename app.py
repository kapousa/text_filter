import requests as requests
from flask import Flask, render_template, request

from lib.TextRephraser import TextRephraser

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return render_template('index.html', mood="")

@app.route('/ethicalvalidation', methods=['POST'])
def ethicalvalidation():  # put application's code here
    if request.form.get('user_text') != None:
        user_text = request.form.get('user_text')

        #URL = 'http://127.0.0.1:5000/api/v1/92640494227942/classifydata'
        URL = 'https://bmapiproject.herokuapp.com/api/v1/92640494227942/classifydata'

        # defining a params dict for the parameters to be sent to the API
        PARAMS = {'data': user_text}

        # sending get request and saving the response as response object
        r = requests.post(url=URL, json=PARAMS)
        mood = "None"
        if r.status_code == 200:
            return_data = r.json()
            for k, v in return_data.items():
                mood = "Entered text is {}".format(v)

        mood = "" if mood == "None" else mood

        return render_template('is_ethical.html', mood=mood, user_text=user_text)
    else:
        return render_template('is_ethical.html', mood="", user_text="")

@app.route('/toxicvalidation', methods=['POST'])
def toxicvalidation():  # put application's code here
    if request.form.get('user_text') != None:
        user_text = request.form.get('user_text')

        #URL = 'http://127.0.0.1:5000/api/v1/79165892196618/classifydata'
        URL = 'https://bmapiproject.herokuapp.com/api/v1/79165892196618/classifydata'

        # defining a params dict for the parameters to be sent to the API
        PARAMS = {'data': user_text}

        # sending get request and saving the response as response object
        r = requests.post(url=URL, json=PARAMS)
        mood = "None"
        if r.status_code == 200:
            return_data = r.json()
            for k, v in return_data.items():
                mood = "Entered text is {}".format(v)

        mood = "" if mood == "None" else mood
        if mood == "Entered text is -":
            mood = mood.replace("-", "not toxic")
        return render_template('is_toxic.html', mood=mood, user_text=user_text)
    else:
        return render_template('is_toxic.html', mood="", user_text="")

@app.route('/ethicguard')
def ethicguard():  # put application's code here
    return render_template("/ethicguard.html")

@app.route('/rephrasegenius')
def rephrasegenius():  # put application's code here
    return render_template("/rephrasegenius.html")

@app.route('/maintanetext', methods=['POST'])
def maintanetext():  # put application's code here
    user_text = request.form.get('user_text')
    action = request.form.get('action')
    process_type = request.form.get("mode")
    text_rephraser_obj = TextRephraser()

    maintained_text = text_rephraser_obj.maintane_sentence(user_text, action, process_type)

    # if action == "rephrase":
    #     maintained_text = text_rephraser_obj.reprashe_sentence(user_text)
    #
    # if action == "summary":
    #     maintained_text = text_rephraser_obj.summary_sentence(user_text)

    return render_template("/rephrasegenius.html", maintained_text=maintained_text, user_text=user_text)

if __name__ == '__main__':
    app.run()
