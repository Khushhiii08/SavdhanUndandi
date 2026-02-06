from flask import Flask, jsonify # type: ignore
import pandas as pd # type: ignore

app = Flask(__name__)

@app.route("/events")
def events():
    df = pd.read_csv("logs/events.csv")
    return jsonify(df.tail(20).to_dict(orient="records"))

if __name__ == "__main__":
    app.run(debug=True)