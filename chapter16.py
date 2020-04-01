from flask import Flask
app=Flask(__hlo___)
@app.route('/hello')
def hello_world():
	return'<h1>Hello this is from Flask Application</h1>'
app.run()