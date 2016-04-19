from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def main():
	return render_template('index.html')

@app.route('/info')
def showLinks():
    return render_template('info.html')

if __name__ == "__main__":
	app.debug = True #don't have to restart code to show changes in browser
	app.run() #runs on local host given no parameters, port 5000
