from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

def create_database():
    conn = sqlite3.connect('catalogue.db')
    c = conn.cursor()
    c.execute('CREATE TABLE IF NOT EXISTS items (id INTEGER PRIMARY KEY, item TEXT)')
    conn.commit()
    conn.close()

    @app.route('/')
    def index():
        conn = sqlite3.connect('catalogue.db')
        c = conn.cursor()
        c.execute('SELECT * FROM items')
        items = c.fetchall()
        conn.close()
        return render_template('index.html', items=items)

@app.route('/add', methods=['POST'])
def add_item():
    item = request.form['item']
    conn = sqlite3.connect('catalogue.db')
    c = conn.cursor()
    c.execute('INSERT INTO items (item) VALUES (?)', (item,)) 
    conn.commit()
    conn.close()
    return redirect(url_for('index'))

@app.route('/delete/<int:item_id>')
def delete_item(item_id):
    conn = sqlite3.connect('catalogue.db')
    c = conn.cursor()
    c.execute('DELETE FROM items WHERE id = ?', (item_id,))
    conn.commit()
    conn.close()
    return redirect(url_for('index'))

if __name__ == '__main__':
    create_database()
    app.run(debug=True)
    
         

