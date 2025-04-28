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
        <head><title>Admissions - IIHMCA</title></head>
        <body style="font-family: Arial, sans-serif; margin: 40px;">
            <h1 style="text-align:center;">Admissions Information</h1>
            
            <h2>Admission Process:</h2>
            <ol>
                <li>Complete the online application form on <a href="https://www.iihmca.org" target="_blank">www.iihmca.org</a> providing personal information, contact details, and academic history. Submit transcripts from the most recent school/college attended.</li>
                <li>Pay the non-refundable application fee of Rs.500/- which can be done online.</li>
            </ol>

            <h2>Admission & Selection Process:</h2>
            <h3>Step 1: Academic Evaluation</h3>
            <p>All applicants undergo a thorough academic evaluation. This includes a review of their transcripts, GPA/test scores, and any advanced coursework or classes taken.</p>
            
            <h3>Step 2: Common Entrance Exam (CEE)</h3>
            <p>Students have to qualify in the Common Entrance Exam, which may include assessments in General Knowledge, General English, Test of Reasoning, and Numerical Ability conducted at the campus or Online.</p>
            
            <h3>Step 3: Interview</h3>
            <p>Shortlisted candidates are invited for a one-on-one interview with the Interview Panel. The interview assesses the student's interpersonal skills, interests, and alignment with the course requirements.</p>
            
            <h3>Step 4: Final Review and Selection</h3>
            <p>The admissions committee conducts a final review of all application materials, considering academic performance, test scores, interview results, and essays. Offers of Admission are based on this holistic evaluation.</p>
            
            <br><p style="text-align:center;"><a href="/">Back to Home</a></p>
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