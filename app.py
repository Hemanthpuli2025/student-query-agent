from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
def home():
    return """
    <html>
        <head>
            <title>IIHMCA Student Support Agent</title>
        </head>
        <body style="text-align:center; margin-top:50px;">
            <h1>Welcome to IIHMCA Student Support Agent!</h1>
            <p>Ask any queries about Admissions, Courses, Fees, and Contact Information.</p>
            <a href="/admissions">Admissions Info</a> |
            <a href="/courses">Courses Offered</a> |
            <a href="/contact">Contact Us</a>
        </body>
    </html>
    """

@app.get("/admissions", response_class=HTMLResponse)
def admissions():
    return """
    <html>
        <head><title>Admissions</title></head>
        <body style="text-align:center; margin-top:50px;">
            <h1>Admissions Information</h1>
            <p>Admissions are open for 2025. Apply Now!</p>
            <p><a href="/">Back to Home</a></p>
        </body>
    </html>
    """

@app.get("/courses", response_class=HTMLResponse)
def courses():
    return """
    <html>
        <head><title>Courses</title></head>
        <body style="text-align:center; margin-top:50px;">
            <h1>Courses Offered</h1>
            <p>- BCT&CA: Catering Technology & Culinary Arts</p>
            <p>- BHM&CT: Hotel Management and Catering Technology</p>
            <p>- 1½ Year Certificate in Culinary Arts</p>
            <p>- 1 Year International Diploma in Patisserie</p>
            <p>- 1 Year Diploma in Culinary Arts</p>
            <p><a href="/">Back to Home</a></p>
        </body>
    </html>
    """

@app.get("/contact", response_class=HTMLResponse)
def contact():
    return """
    <html>
        <head><title>Contact Us</title></head>
        <body style="text-align:center; margin-top:50px;">
            <h1>Contact Us</h1>
            <p>Phone: +91-1234567890</p>
            <p>Email: director.iihmca@gmail.com</p>
            <p>Address: Hyderabad, Telangana, India</p>
            <p><a href="/">Back to Home</a></p>
        </body>
    </html>
    """