import calendar
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/keliamieji")
def user():
    kel_metai = []
    for x in range(1900, 2100):
        if calendar.isleap(x) is True:
            kel_metai.append(x)
    return render_template("d.html", metai=kel_metai)


app.run()
