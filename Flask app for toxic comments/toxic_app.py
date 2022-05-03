
from flask import Flask, render_template, request
from detoxify import Detoxify

app = Flask(__name__)

# Render the HTML file for the home page
@app.route("/")
def home():
    return render_template('index_toxic.html')

@app.route("/predict", methods=['POST'])
def predict():
    
    # Take a string input from user
    user_input = request.form['text']
    data = [user_input]

    results = Detoxify('original').predict(data)

    print(results)

    pred_tox = results['toxicity']

    pred_sev = results['severe_toxicity']

    pred_obs = results['obscene']

    pred_thr = results['threat']

    pred_ins = results['insult']

    pred_ide = results['identity_attack']

    out_tox = round(pred_tox[0], 2)
    if(out_tox<0.5):
           text_tox =""
    else:
        text_tox ="Toxic"
    out_sev = round(pred_sev[0], 2)

    if(out_sev<0.5):
           text_sev =""
    else:
        text_sev ="Severly toxic"

    out_obs = round(pred_obs[0], 2)
    if(out_obs<0.5):
           text_obs =""
    else:
        text_obs ="Obscene"

    out_ins = round(pred_ins[0], 2)
    if(out_ins<0.5):
           text_ins =""
    else:
        text_ins ="Insult"

    out_thr = round(pred_thr[0], 2)
    if(out_thr<0.5):
           text_thr =""
    else:
        text_thr ="Threat"

    out_ide = round(pred_ide[0], 2)
    if(out_ide<0.5):
           text_ide =""
    elif(out_ide<0.5 and out_tox<0.5 and out_obs<0.5 and out_sev<0.5 and out_thr<0.5 and out_ins<0.5):
        text_ide ="Good"
    else:
        text_ide ="Identity hate"

    print(out_tox)  

    return render_template('index_toxic.html', 
                            pred_tox =text_tox,
                            pred_sev = text_sev,
                            pred_obs = text_obs,
                            pred_ins = text_ins,
                            pred_thr = text_thr,
                            pred_ide = text_ide                       
                            )

# Server reloads itself if code changes so no need to keep restarting:
app.run(debug=True)

