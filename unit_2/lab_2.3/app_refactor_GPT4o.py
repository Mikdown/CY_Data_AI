import os
from flask import Flask, request, g, jsonify
import sqlite3

app = Flask(__name__)
app.config['DATABASE'] = 'users.db'


def get_db():
    """
    Opens a new database connection if there is none yet for the current application context.
    """
    if 'db' not in g:
        g.db = sqlite3.connect(app.config['DATABASE'])
        g.db.row_factory = sqlite3.Row  # Enable dictionary-like access to rows
    return g.db


@app.teardown_appcontext
def close_db(exception):
    """
    Closes the database connection at the end of the request.
    """
    db = g.pop('db', None)
    if db is not None:
        db.close()


@app.route('/user')
def get_user_profile():
    """
    Fetches a user profile from the database based on the user_id provided as a query parameter.
    Returns the user data in JSON format.
    """
    user_id = request.args.get('id')

    # Validate user_id
    if not user_id or not user_id.isdigit():
        return jsonify({"error": "Invalid user ID"}), 400

    db = get_db()
    try:
        # Use parameterized query to prevent SQL injection
        cursor = db.execute("SELECT * FROM users WHERE user_id = ?", (user_id,))
        user_data = cursor.fetchone()

        if user_data is None:
            return jsonify({"error": "User not found"}), 404

        # Assuming process_data and format_response are defined elsewhere
        temp = process_data(dict(user_data))  # Convert row to dictionary
        res = format_response(temp)

        return jsonify(res), 200

    except sqlite3.Error as e:
        return jsonify({"error": "Database error", "details": str(e)}), 500


if __name__ == "__main__":
    app.run(debug=True)