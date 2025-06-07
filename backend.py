from flask import Flask, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        data = request.form.to_dict()
        return f"✅ POST received: {data}"
    return "✅ Backend is up and responding!"

app.run(port=3000)

