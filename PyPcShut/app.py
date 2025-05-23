from flask import Flask, render_template
import os
import platform
import time

app = Flask(__name__)

def close_all_programs():
    current_os = platform.system()

    if current_os == "Windows":
        os.system("shutdown /s /f /t 60")  # Initiates shutdown with a delay of 60 seconds
    elif current_os == "Linux":
        os.system("shutdown -h +1")  # Initiates shutdown with a delay of 1 minute
    else:
        print("Unsupported operating system")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/shutdown')
def shutdown():
    close_all_programs()
    return "Shutting down..."

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)
