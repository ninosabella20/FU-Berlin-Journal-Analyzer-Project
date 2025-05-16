from flask import Flask, render_template, request
import app
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    daily = request.form.get('daily')
    print(f"Output which you entered: {daily}")
    emotions = app.analyze_journal(daily)
    print(emotions)
    return render_template('result.html', name=daily)

if __name__ == '__main__':
    app.run(debug=True)