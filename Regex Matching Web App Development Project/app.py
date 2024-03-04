from flask import Flask, request, render_template, redirect
import re

app = Flask(__name__)
####################################

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/results', methods=['POST'])
def results():
    regex = request.form.get('regex')
    test_string = request.form.get('test_string')
    func = request.form.get('func')

    result = ''

    if func == "findall":
        result = re.findall(regex, test_string)
    elif func == "search":
        x = re.search(regex, test_string)
        if x is not None:
            result = 'The text is located in position: {}'.format(x.start())
        else:
            result = 'No Match found, please try again'
    elif func == "split":
        result = re.split(regex, test_string)
    elif func == "sub":
        result = re.sub(regex, test_string)
    if result == []:
        result = 'No Match found, please try again'
    if type(result) != list:
        result = [result]
    return render_template('result.html', result=result, regex = regex, test_string = test_string, func = func)

@app.route('/validate_email', methods=['POST'])
def validate():
    regex = '^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,3}$'
    email = request.form.get('email')
    check = re.match(regex, email)
    if check:
        return render_template('home.html', email=email, email_address="Valid email address", condition=True)
    else:
        return render_template('home.html',email=email, email_address="Invalid email address")

####################################

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')