from flask import Flask, render_template, request, send_file
from reportlab.pdfgen import canvas
from reportlab.lib import colors
from reportlab.lib.utils import ImageReader

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    name = request.form['name']
    email = request.form['email']
    mobile = request.form['mobile']
    about = request.form['about']
    skills = request.form['skills']
    education = request.form['education']
    experience = request.form['experience']

    filename = f"{name}_resume.pdf"
    c = canvas.Canvas(filename)

    # Background
    c.setFillColor(colors.whitesmoke)
    c.rect(0, 0, 600, 850, fill=1)

    # Better sidebar color (light beige)
    c.setFillColorRGB(0.90, 0.85, 0.82)
    c.rect(0, 0, 160, 850, fill=1)

    # Sidebar text
    c.setFillColor(colors.black)
    c.setFont("Helvetica-Bold", 16)
    c.drawString(20, 760, "CONTACT")
    c.setFont("Helvetica", 11)
    c.drawString(20, 730, mobile)
    c.drawString(20, 705, email)

    # Skills
    c.setFont("Helvetica-Bold", 16)
    c.drawString(20, 620, "SKILLS")
    text = c.beginText(20, 590)
    text.setFont("Helvetica", 11)
    for line in skills.split(','):
        text.textLine("• " + line.strip())
    c.drawText(text)

    # Education
    c.setFont("Helvetica-Bold", 16)
    c.drawString(20, 450, "EDUCATION")
    text = c.beginText(20, 420)
    text.setFont("Helvetica", 11)
    for line in education.split(','):
        text.textLine("• " + line.strip())
    c.drawText(text)

    # Right side
    c.setFillColor(colors.black)
    c.setFont("Helvetica-Bold", 28)
    c.drawString(190, 780, name)
    c.line(190, 760, 540, 760)

    # About
    c.setFont("Helvetica-Bold", 18)
    c.drawString(190, 710, "ABOUT")
    text = c.beginText(190, 680)
    text.setFont("Helvetica", 12)
    text.textLine(about)
    c.drawText(text)

    # Experience
    c.setFont("Helvetica-Bold", 18)
    c.drawString(190, 600, "EXPERIENCE")
    text = c.beginText(190, 570)
    text.setFont("Helvetica", 12)
    for line in experience.split(','):
        text.textLine("• " + line.strip())
    c.drawText(text)

    c.save()
    return send_file(filename, as_attachment=True)

import os

if __name__ == "_main_":
    # Render khud ek PORT allocate karta hai, agar wo na mile toh default 5000 use hoga
    port = int(os.environ.get("PORT", 5000))
    
    # host="0.0.0.0" likhna sabse zaroori hai taaki Render ise scan kar sake
    app.run(host="0.0.0.0", port=port)
    
    
    
