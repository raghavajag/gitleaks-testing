from flask import Flask, request, render_template_string, Response
import sqlite3
import os
import subprocess # For command injection example

app = Flask(__name__)

# --- Configuration & Setup ---
DATABASE = 'users.db'
# VULNERABILITY: Hardcoded secret key (should be in config/env var)
API_SECRET = "sk_live_THIS_IS_A_VERY_BAD_SECRET_KEY"

def init_db():
    """Initializes the database if it doesn't exist."""
    if not os.path.exists(DATABASE):
        conn = sqlite3.connect(DATABASE)
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT UNIQUE NOT NULL,
                email TEXT NOT NULL,
                is_admin INTEGER DEFAULT 0
            )
        ''')
        cursor.execute("INSERT INTO users (username, email, is_admin) VALUES (?, ?, ?)",
                       ('admin', 'admin@example.com', 1))
        cursor.execute("INSERT INTO users (username, email) VALUES (?, ?)",
                       ('alice', 'alice@example.com'))
        conn.commit()
        conn.close()
        print(f"Database '{DATABASE}' initialized.")

# --- Vulnerable Routes ---

@app.route('/')
def home():
    return "Welcome to the Vulnerable App!"

@app.route('/user_info')
def get_user_info():
    """Fetches user info based on username from query param."""
    username = request.args.get('username')
    if not username:
        return "Please provide a 'username' parameter.", 400

    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()

    # VULNERABILITY: SQL Injection - user input directly formatted into query
    query = f"SELECT username, email FROM users WHERE username = '{username}'"
    print(f"Executing query: {query}") # Logging for demo

    try:
        cursor.execute(query)
        user = cursor.fetchone()
        conn.close()
        if user:
            # VULNERABILITY: Potential Reflected XSS (if username can contain HTML/JS)
            # Though render_template_string might escape by default depending on context,
            # explicitly show unsafe rendering pattern.
            template = f"<h1>User Info</h1><p>Username: {user[0]}</p><p>Email: {user[1]}</p>"
            return render_template_string(template)
        else:
            return f"User '{username}' not found.", 404
    except Exception as e:
        conn.close()
        return f"Database error: {str(e)}", 500

@app.route('/file_content')
def get_file_content():
    """Displays the content of a file specified by query param."""
    filename = request.args.get('filename')
    if not filename:
        return "Please provide a 'filename' parameter.", 400

    # VULNERABILITY: Command Injection - user input used in OS command
    # Using os.system is highly dangerous. subprocess with shell=True is also risky.
    command = f"cat {filename}"
    print(f"Executing command: {command}") # Logging for demo

    try:
        # Using os.system for clear vulnerability demonstration
        # result = os.system(command) # Very bad!
        # Alternative using subprocess (still vulnerable with shell=True or direct user input)
        result = subprocess.run(command, shell=True, capture_output=True, text=True, check=True)
        return Response(result.stdout, mimetype='text/plain')

    except subprocess.CalledProcessError as e:
        return f"Error executing command: {e.stderr}", 500
    except Exception as e:
        return f"An error occurred: {str(e)}", 500

# --- Dead Code Section ---

def generate_old_report(user_id):
    """
    An old, unused function with a potential vulnerability.
    THIS FUNCTION IS NEVER CALLED.
    """
    print(f"[DEAD CODE] Generating old report for {user_id}")
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    # VULNERABILITY (in dead code): SQL Injection via string formatting
    query = f"SELECT email FROM users WHERE id = {user_id}" # Assuming user_id might not be safe
    try:
        cursor.execute(query)
        # ... potentially process result ...
    except Exception as e:
        print(f"Error in dead code report: {e}")
    finally:
        conn.close()

# --- Main Execution ---
if __name__ == '__main__':
    init_db()
    # VULNERABILITY: Running Flask in debug mode in a production-like script
    app.run(debug=True, host='0.0.0.0', port=5000)

    # generate_old_report is never called from the main execution path or routes.


