from flask import Flask, render_template, request, flash, redirect, url_for, json
import requests

#pip install recaptcha
#reCATPCHA V2

app = Flask(__name__)
app.config['SECRET_KEY'] = 'FLASK_SECRET_KEY'           #import os
                                                        #print(os.urandom(12).hex())

def is_human(captcha_response):
    secret = "YOUR_SITE_KEY "
    payload = {'response': captcha_response, 'secret': secret}
    response = requests.post("https://www.google.com/recaptcha/api/siteverify", payload)
    response_text = json.loads(response.text)

    return response_text['success']

@app.route("/", methods=["GET", "POST"])
def contact():
    sitekey = "YOUR_SECRET_KEY"

    if request.method == "POST":
        name = request.form['name']
        email = request.form['email']
        print(" name:", name)
        print(" email is :", email)
        captcha_response = request.form['g-recaptcha-response']
        if is_human(captcha_response):
            status = "Detail submitted successfully."
        else:
            status = "Sorry ! Please Check Im not a robot."
        flash(status)
        return redirect(url_for('contact'))
    return render_template("form.html", sitekey=sitekey)

if __name__ == '__main__':
    app.run(debug=True)





























