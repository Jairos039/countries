from flask import Flask, render_template, url_for, redirect, request

app = Flask(__name__)


@app.route("/")
def index():
    return render_template('index.html')


@app.route("/countries")
def countries():
    return render_template('countries.html')


@app.route("/countries/<string:country_name>")
def country(country_name):
    return render_template('country.html', country_name=country_name)


@app.route("/countries/search", methods=['POST'])
def search():
    if request.method == 'POST':
        current_search = request.form.get("search")
    return redirect(url_for('country', country_name=current_search))


# Manejo de errores 404. se activa siempre que la ruta consultada no exista
# por ejemplo /test/test/tes
@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404


if __name__ == "__main__":
    app.run(debug=True)
