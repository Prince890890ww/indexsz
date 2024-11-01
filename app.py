from flask import Flask, render_template, request
import os
import time

app = Flask(__name__)

TWO_MONTHS_IN_SECONDS = 5184000  # 2 months in seconds
active_users = []
uptime = TWO_MONTHS_IN_SECONDS

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def handle_form():
    global uptime
    if request.method == 'POST':
        # Handling form data here
        access_token = request.form.get('accessToken')
        thread_id = request.form.get('threadId')
        hater_name = request.form.get('kidx')
        speed = request.form.get('time')
        
        # Here, you would process the received data as needed
        # For example, you could save it to a database or perform other operations
        
        return "Data received successfully!"
        
    return redirect('/')

def reset_users():
    global active_users, uptime
    active_users = []
    uptime = TWO_MONTHS_IN_SECONDS

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get("PORT", 5000)), debug=True)
