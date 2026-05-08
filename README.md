Lab: Securing APIs using OAuth 2.0

Miraflores, Marl Aj 
May 8, 2026

 Project Overview

This project demonstrates the implementation of **OAuth 2.0** to secure a web application. Using **Flask** and the **Authlib** library, the application integrates with **GitHub** as the Identity Provider (IdP) to authenticate users and protect sensitive user data.

Features

- **OAuth Handshake:** Securely redirects users to GitHub for authorization.
- **Protected Routes:** The `/profile` route is only accessible after a successful login.
- **Session Management:** Uses Flask sessions to store user identity temporarily.
- **Secure Logout:** Implements session clearing to revoke access.
- **Dynamic UI:** Displays GitHub profile data (avatar, followers, following) in a centered dashboard.

 How I Built It (Step-by-Step)

1. Provider Registration

I registered a new **OAuth Application** on GitHub Developer Settings.

- **Homepage URL:** `http://localhost:5000`
- **Authorization Callback URL:** `http://127.0.0.1:5000/callback`
- I generated a **Client ID** and **Client Secret** to allow my app to communicate with GitHub's API.

 2. Environment Setup

I initialized a Python environment and installed the necessary dependencies:

- `Flask`: For the web server logic.
- `Authlib`: To handle the OAuth 2.0 protocol and token exchange.
- `Requests`: To fetch data from the GitHub User API.

 3. Implementing the OAuth Flow

- **Login Route:** Redirects the user to GitHub's authorization page.
- **Callback Route:** Receives the authorization code from GitHub, trades it for an access token, and fetches the user's profile information.
- **Authorization Check:** Added logic to the `/profile` route to check if a `user` exists in the `session`. If not, it returns a `401 Unauthorized` status.



4. Revoking Access

I implemented a `/logout` route that uses `session.clear()` to ensure that once a user logs out, they can no longer access the protected `/profile` data without re-authenticating.

How to Run

1. Ensure Python is installed.
2. Install requirements: `pip install -r requirements.txt`
3. Run the application: `python app.py`
4. Access the app at `http://127.0.0.1:5000/`
