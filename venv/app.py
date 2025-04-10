from flask import Flask, render_template, render_template, request

# app
app = Flask(__name__)

# routes
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/recommendation')
def recommendation():
    return render_template('recommendation.html')

# python main
if __name__ == '__main__':
    app.run(debug=True)