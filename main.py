from flask import Flask, request, render_template, redirect

app = Flask(__name__)

warehouses_map = {
    'СкладWMS (Паперня MAIN)': "/warehouses/172",
    'СкладWMS (Паперня QARANTINE)': "/warehouses/173",
    'СкладWMS (Паперня BRAK)': "/warehouses/174",
    'СкладWMS (Паперня LOST)': "/warehouses/175",
    'СкладWMS (Паперня EXPORT)': "/warehouses/176"
}

path = ""


@app.route('/')
def index():
    return render_template("/pages/homePage.html")


@app.route('/table', methods=['POST'])
def find_table():
    params = request.get_json(force=True, silent=True)
    warehouse = params['warehouse']
    warehouse_path = warehouses_map[warehouse] + "/"
    date = params['date'].replace("-", "")
    global path
    path = warehouse_path + date + ".html"
    return redirect('/table')


@app.route('/table')
def show_table():
    try:
        return render_template(path)
    except:
        return "Остатков нет или данные не сохранились"


@app.route('/cabinet')
def cabinet():
    return render_template("/pages/cabinet.html")


if __name__ == '__main__':
    app.run(debug=True)
