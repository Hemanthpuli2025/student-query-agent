from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
def home():
    return """
    <html>
        <head>
            <title>IIHMCA Student Query Agent</title>
            <style>
                body { 
                    font-family: Arial, sans-serif; 
                    background-color: #f5f5f5; 
                    display: flex; 
                    flex-direction: column; 
                    align-items: center; 
                    justify-content: center; 
                    height: 100vh; 
                    margin: 0; 
                }
                h1 {
                    color: #2c3e50;
                }
                p {
                    font-size: 20px;
                    color: #34495e;
                }
            </style>
        </head>
        <body>
            <h1>Welcome to IIHMCA Student Support Agent!</h1>
            <p>Ask any queries about Admissions, Courses, Fees, and Contact Information.</p>
            <p>We are here to help you!</p>
        </body>
    </html>
    """