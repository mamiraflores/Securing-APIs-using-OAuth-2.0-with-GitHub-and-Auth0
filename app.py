from flask import Flask, redirect, url_for, session, jsonify
from authlib.integrations.flask_client import OAuth

app = Flask(__name__)
app.secret_key = "a944659596f55a04fef46c90e330de3b43035eec"  # Replace with a real secret key [cite: 49]


oauth = OAuth(app)


github = oauth.register(
    name='github',
    client_id='Ov23linHCRHFGYB8huWJ',       
    client_secret='a944659596f55a04fef46c90e330de3b43035eec', # Replace with your Client Secret [cite: 57]
    access_token_url='https://github.com/login/oauth/access_token',
    authorize_url='https://github.com/login/oauth/authorize',
    api_base_url='https://api.github.com/',
    client_kwargs={'scope': 'user:email'},
)

@app.route('/')
def index():
    return '''
        <h1>Welcome to the OAuth Lab</h1>
        <p>Your application is running successfully!</p>
        <a href="/login"><button>Login with GitHub</button></a>
    '''

@app.route('/login')
def login():
    redirect_uri = url_for('callback', _external=True)
    return github.authorize_redirect(redirect_uri)


@app.route('/callback')
def callback():
    token = github.authorize_access_token()
    resp = github.get('user')
    user = resp.json()
    session['user'] = user  
    return redirect('/profile')

# Protected Profile Route 
@app.route('/profile')
def profile():
    user = session.get('user')
    if not user:
        return "Unauthorized", 401
    
    # Extracting the specific fields you requested
    username = user.get('login')
    avatar_url = user.get('avatar_url')
    followers = user.get('followers')
    following = user.get('following')
    github_link = user.get('html_url')

    return f'''
        <h1>Profile Page</h1>
        <img src="{avatar_url}" width="150" style="border-radius: 50%; border: 2px solid #333;">
        
        <h2>User: {username}</h2>
        <ul>
            <li><strong>Followers:</strong> {followers}</li>
            <li><strong>Following:</strong> {following}</li>
            <li><strong>GitHub Profile:</strong> <a href="{github_link}" target="_blank">View Profile</a></li>
        </ul>
        
        <br>
        <a href="/logout"><button>Logout</button></a>
    '''

# Logout Route 
@app.route('/logout')
def logout():
    session.pop('user', None) 
    return redirect('/sign-out') 

# Bonus Challenge:
@app.route('/api/secure-data')
def secure_data():
    if 'user' not in session:
        return jsonify({"error": "Access Denied"}), 403
    return jsonify({"message": "This is highly sensitive data!", "status": "Secure"})

@app.route('/sign-out')
def sign_out():
    session.clear() 
    return "<h1>Logged Out</h1><p>You have been signed out. <a href='/login'>Login again</a></p>"

if __name__ == '__main__':
    app.run(debug=True) 