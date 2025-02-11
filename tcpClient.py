from flask import Flask
import os
import sys

app = Flask(__name__)

@app.route('/')
def shutdown_computer():
    try:
        # For Windows OS
        if sys.platform == "win32":
            os.system("shutdown /s /t 000")
        else:
            return "This shutdown script only works on Windows."
        
        return "Shutdown command executed successfully."
    except Exception as e:
        return f"An error occurred: {str(e)}"

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=5000)
