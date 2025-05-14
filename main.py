from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    daily = request.form.get('daily')
    return render_template('result.html', name=daily)

if __name__ == '__main__':
    app.run(debug=True)