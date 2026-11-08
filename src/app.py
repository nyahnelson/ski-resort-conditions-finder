from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <h1>Idaho Ski Resort Conditions Finder</h1>
    <p>Find the best skiing conditions in Idaho!</p>

    <form action="/conditions" method="POST">
        <label>Select a ski resort:</label>

        <select name="resort">
            <option>Bogus Basin</option>
            <option>Brundage Mountain</option>
            <option>Tamarack Resort</option>
            <option>Sun Valley Resort</option>
        </select>

        <button type="submit">View Conditions</button>
    </form>
    """

@app.route("/conditions", methods=["POST"])
def conditions():
    resort = request.form.get("resort", "")
    return f"<h2>You selected: {resort}</h2>"