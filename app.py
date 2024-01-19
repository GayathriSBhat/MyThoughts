from flask import Flask


app=Flask(__name__)

@app.route('/')#used to avoid 404 error
def login():
    return "hello world"
if __name__== "__main__":
    app.run(debug=True)
