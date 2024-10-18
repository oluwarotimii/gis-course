Here’s a README file for your Flask application, explaining how to set it up, its purpose, and its components:

---

# **Geodev JupyterHub Portal**

This project is a web application built using Flask that allows users to **register**, **log in**, and access **JupyterHub** for a **GIS course** provided by **GEodev**. The application connects with JupyterHub, handling user registration and authentication, and redirects users to their JupyterHub notebooks after login.

---

## **Features**

- **User Registration:** Users can sign up for an account using their email and password.
- **User Login:** Registered users can log in with their credentials.
- **JupyterHub Integration:** After login, users are redirected to JupyterHub where they can access GIS course notebooks.
- **Password Hashing:** User passwords are securely hashed using Flask-Bcrypt.
- **Responsive Design:** The app is styled using CSS for a clean and modern UI.
- **Session Management:** Flask-Login is used to manage user sessions.

---

## **Technologies Used**

- **Python** (Flask)
- **HTML/CSS/JavaScript**
- **Flask-WTF** for form handling
- **Flask-Bcrypt** for password hashing
- **Flask-Login** for session management
- **JupyterHub API** for user account creation and authentication

---

## **Setup and Installation**

### **Requirements**
- Python 3.6+
- Flask 2.x
- JupyterHub

### **Step-by-Step Installation**

1. **Clone the Repository**  
   ```bash
   git clone https://github.com/your-repo/geodev-jupyterhub-portal.git
   cd geodev-jupyterhub-portal
   ```

2. **Create a Virtual Environment**  
   It's recommended to use a virtual environment for this project.
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install Dependencies**  
   Install the required Python packages listed in `requirements.txt`.
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure Environment Variables**  
   Create a `.env` file in the root of your project and add the following variables:
   ```
   SECRET_KEY=your_secret_key_here
   JUPYTERHUB_URL=http://localhost:8000  # Your JupyterHub URL
   JUPYTERHUB_API_TOKEN=your_jupyterhub_api_token
   ```

5. **Run the Application**  
   Start the Flask development server.
   ```bash
   python app.py
   ```

6. **Access the Application**  
   Once the server is running, open your browser and navigate to `http://127.0.0.1:5000`.

---

## **File Structure**

```
geodev-jupyterhub-portal/
│
├── app.py                 # Main Flask application file
├── config.py              # Configuration file for Flask app
├── requirements.txt       # Required Python packages
├── .env                   # Environment variables
├── static/                # Static assets (CSS, JavaScript)
│   ├── styles.css         # Main CSS file
│   └── scripts.js         # Main JavaScript file
├── templates/             # HTML templates for the Flask app
│   ├── login.html         # Login page
│   └── register.html      # Registration page
└── README.md              # This file
```

---

## **Usage**

1. **Register an Account**  
   Go to `/register`, fill in your details, and submit the form. The user will be created in JupyterHub, and you can log in with the same credentials.

2. **Log In**  
   Go to `/login`, enter your username and password, and once authenticated, you will be redirected to JupyterHub for the GIS course.

---

## **License**

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## **Contact**

For any inquiries or questions, please reach out to [support@geodev.com](mailto:support@geodev.com).

---

This README file should provide all necessary instructions for setting up and running the Flask-JupyterHub portal for your GEodev GIS course.
