from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
def home():
    return """
    <html>
        <head>
            <title>IIHMCA Student Support Agent</title>
            <style>
                body { font-family: Arial, sans-serif; text-align: center; margin-top: 50px; }
                h1 { color: #2c3e50; }
                p { font-size: 20px; color: #34495e; }
                a { display: block; margin: 10px; font-size: 18px; color: #3498db; text-decoration: none; }
            </style>
        </head>
        <body>
            <h1>Welcome to IIHMCA Student Support Agent!</h1>
            <p>Ask any queries about Admissions, Courses, Fees, and Contact Information.</p>
            <a href="/admissions">Admissions Info</a>
            <a href="/courses">Courses Offered</a>
            <a href="/contact">Contact Us</a>
        </body>
    </html>
    """

@app.get("/admissions", response_class=HTMLResponse)
def admissions():
    return """
    <html>
        <head>
            <title>Admissions - IIHMCA</title>
            <style> body { font-family: Arial, sans-serif; text-align: center; margin-top: 50px; } </style>
        </head>
        <body>
            <h1>Admissions Information</h1>
            <p>Admissions are open for 2025. Apply Now!</p>
            <p>Contact our Admissions Office for details.</p>
            <a href="/">Go Back Home</a>
        </body>
    </html>
    """

@app.get("/courses", response_class=HTMLResponse)
def courses():
    return """
    <html>
        <head>
            <title>Courses - IIHMCA</title>
            <style> body { font-family: Arial, sans-serif; text-align: center; margin-top: 50px; } </style>
        </head>
        <body>
            <h1>Courses Offered</h1>
            <p>- BCT&CA: Bachelors in Catering Technology and Culinary Arts</p>
            <p>- BHM&CT: Bachelors in Hotel Management and Catering Technology</p>
            <p>- 1½ Year Certificate in Culinary Arts</p>
            <p>- 1 Year International Diploma in Patisserie</p>
            <p>- 1 Year Diploma in Culinary Arts</p>
            <a href="/">Go Back Home</a>
        </body>
    </html>
    """

@app.get("/contact", response_class=HTMLResponse)
def contact():
    return """
    <html>
        <head>
            <title>Contact - IIHMCA</title>
            <style> body { font-family: Arial, sans-serif; text-align: center; margin-top: 50px; } </style>
        </head>
        <body>
            <h1>Contact Us</h1>
            <p>Phone: +91-1234567890</p>
            <p>Email: director.iihmca@gmail.com</p>
            <p>Address: Hyderabad, Telangana, India</p>
            <a href="/">Go Back Home</a>
        </body>
    </html>
    """