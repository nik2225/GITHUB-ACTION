from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('register.html')

@app.route('/register', methods=['POST'])
def register():
    name = request.form['name']
    email = request.form['email']
    return f"Registered {name} with email {email}"

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')  # Important for Docker!
