from flask import Flask, redirect, url_for, request, render_template

app = Flask(__name__)


@app.route('/login', methods=['POST', 'GET'])
def ar_keliamieji_metai():
    zinute = "Iveskite metus!!"
    metai = ''
    if request.method == "POST":
        try:
            metai = int(request.form["metai"])
            if (metai % 400 == 0) or (metai % 100 != 0 and metai % 4 == 0):
                zinute = f'Metai {metai} yra keliamieji!'
            else:
                zinute = f'Metai {metai} nėra keliamieji!'
            renderis = render_template("sablonas.html", metai=metai, zinute=zinute)
        except ValueError:

            renderis = render_template("sablonas.html", metai=metai, zinute=zinute)
    else:
        renderis = render_template("sablonas.html", zinute=zinute)
    return renderis


if __name__ == '__main__':
    app.run(debug=True)
