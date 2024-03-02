import sqlite3

from flask import Flask,render_template



app = Flask(__name__)


@app.route('/')
def index():
   return render_template('index.html')

@app.route('/information')
def information():
    conn = sqlite3.connect('LFB_data.db')
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()
    cur.execute("SELECT * FROM incident")
    rows = cur.fetchall()
    conn.close()
    return render_template('information.html',rows=rows)

@app.route('/property')
def property():
    conn = sqlite3.connect('LFB_data.db')
    conn.row_factory =  sqlite3.Row
    cur = conn.cursor()
    cur.execute("SELECT * FROM property_type")
    rows = cur.fetchall()
    conn.close()
    return render_template('property.html',rows=rows)

@app.route('/information_with_type')
def information_with_type():
    conn = sqlite3.connect('LFB_data.db')
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()
    cur.execute("SELECT * FROM incident i INNER JOIN property_type p ON i.property_id = p.property_id")
    rows = cur.fetchall()
    conn.close()
    return render_template('information_with_type.html', rows=rows)


@app.route('/details/<string:id>')
def details(id):
    conn = sqlite3.connect('LFB_data.db')
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()
    cur.execute("SELECT *  FROM incident i INNER JOIN property_type p ON i.property_id = p.property_id WHERE incident_id = ? ", (id,))
    rows = cur.fetchall()
    conn.close()
    return render_template('details.html', rows=rows)


if __name__ == '__main__':
    app.run()
