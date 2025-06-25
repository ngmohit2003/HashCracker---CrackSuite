from flask import Flask, request, render_template_string
from modules.cracker import crack_hash

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    if request.method == "POST":
        hash_input = request.form["hash"]
        wordlist = "wordlists/rockyou.txt"
        result = crack_hash(hash_input, wordlist)
    return render_template_string('''
        <!DOCTYPE html>
        <html>
        <head>
            <title>CrackSuite GUI</title>
        </head>
        <body style="font-family:sans-serif">
            <h1>🔐 CrackSuite Web</h1>
            <form method="post">
                <label>Enter Hash:</label>
                <input name="hash" type="text" required>
                <button type="submit">Crack</button>
            </form>
            {% if result is not none %}
                <h2>{{ '✅ Cracked: ' + result if result else '❌ Not Found' }}</h2>
            {% endif %}
        </body>
        </html>
    ''', result=result)

if __name__ == "__main__":
    app.run(debug=True)
