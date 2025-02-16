from flask import Flask, request, jsonify
import sqlite3
import bcrypt

app = Flask(__name__)

def init_db():
    with sqlite3.connect('users.db') as conn:
        conn.execute('''CREATE TABLE IF NOT EXISTS users (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        email TEXT UNIQUE NOT NULL,
                        password TEXT NOT NULL)''')

@app.route('/register', methods=['POST'])
def register():
    data = request.json
    hashed_pw = bcrypt.hashpw(data['password'].encode(), bcrypt.gensalt())
    try:
        with sqlite3.connect('users.db') as conn:
            conn.execute('INSERT INTO users (email, password) VALUES (?, ?)', (data['email'], hashed_pw))
        return jsonify({'message': 'User registered'}), 201
    except sqlite3.IntegrityError:
        return jsonify({'error': 'User already exists'}), 400

@app.route('/login', methods=['POST'])
def login():
    data = request.json
    with sqlite3.connect('users.db') as conn:
        cur = conn.cursor()
        cur.execute('SELECT password FROM users WHERE email = ?', (data['email'],))
        user = cur.fetchone()
    if user and bcrypt.checkpw(data['password'].encode(), user[0]):
        return jsonify({'message': 'Login successful'})
    return jsonify({'error': 'Invalid credentials'}), 400

if __name__ == '__main__':
    init_db()
    app.run(debug=True)

import tkinter as tk
from tkinter import messagebox
import requests

def login():
    email = email_entry.get()
    password = password_entry.get()
    response = requests.post('http://127.0.0.1:5000/login', json={'email': email, 'password': password})
    messagebox.showinfo('Login', response.json().get('message', response.json().get('error')))

def register():
    email = email_entry.get()
    password = password_entry.get()
    response = requests.post('http://127.0.0.1:5000/register', json={'email': email, 'password': password})
    messagebox.showinfo('Register', response.json().get('message', response.json().get('error')))

root = tk.Tk()
root.title('Login')

tk.Label(root, text='Email').pack()
email_entry = tk.Entry(root)
email_entry.pack()

tk.Label(root, text='Password').pack()
password_entry = tk.Entry(root, show='*')
password_entry.pack()

tk.Button(root, text='Login', command=login).pack()
tk.Button(root, text='Register', command=register).pack()

root.mainloop()
