import os
from flask import Flask, session, redirect, url_for

app = Flask(__name__)
# Generate a secure secret key
app.secret_key = os.urandom(24)  

# Route to the Account page
@app.route('/account')
def account():
    return 'This is the Account page'

# Route to sign out the user
@app.route('/signout')
def signout():
    
    # session.pop('authenticated', None)
    # Redirect the user to the Account page
    return redirect(url_for('account'))

if __name__ == '__main__':
    app.run()
