from flask import Flask, request
import sqlite3
from vul import sanitize_input, fake_sanitize_input
app = Flask(__name__)

def vuln_function():
    username = request.args.get('username')  # Clear source
    
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    safe_input = fake_sanitize_input(username)
 
    # Vulnerable query construction
    query = "SELECT * FROM users WHERE username = '" + safe_input + "'"
    
    # Execution
    cursor.execute(query)  # Clear sink
    
    user = cursor.fetchone()
    conn.close()
    return str(user)

@app.route('/user')
def show_user():
    username = request.args.get('username')  # Clear source
    
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    safe_input = fake_sanitize_input(username)
 
    # Vulnerable query construction
    query = "SELECT * FROM users WHERE username = '" + safe_input + "'"
    
    # Execution
    cursor.execute(query)  # Clear sink
    
    user = cursor.fetchone()
    conn.close()
    return str(user)

@app.route('/user')
def show_user():
    username = request.args.get('username')  # Clear source
    
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    safe_input = sanitize_input(username)
 
    # Vulnerable query construction
    query = "SELECT * FROM users WHERE username = '" + safe_input + "'"
    
    # Execution
    cursor.execute(query)  # Clear sink
    
    user = cursor.fetchone()
    conn.close()
    return str(user)

@app.route('/user')
def how_user():
    username = request.args.get('username')  # Clear source
    
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    safe_input = sanitize_input(username)
 
    # Vulnerable query construction
    query = "SELECT * FROM users WHERE username = '" + username + "'"
    
    # Execution
    cursor.execute(query)  # Clear sink
    
    user = cursor.fetchone()
    conn.close()
    return str(user)

if __name__ == '__main__':
    app.run(debug=True)
