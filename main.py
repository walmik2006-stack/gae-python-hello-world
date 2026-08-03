from flask import Flask
app = Flask(__name__)
@app.route("/")
def hello():
return """
<html>
<head>
<title>My First GAE Application</title>
</head>
<body style="text-align:center; font-family:Arial; margin-top:100px;">
<h1>Hello World!</h1>
<h2>My First Python Application</h2>
<p>This application is running on Google App Engine.</p>
</body>
</html>
"""
if __name__ == "__main__":
app.run(host="0.0.0.0", port=8080)
