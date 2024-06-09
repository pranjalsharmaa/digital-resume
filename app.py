from pathlib import Path

import streamlit as st
from PIL import Image 


# ---- PATH SETTINGS ----

current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "assets" / "pranjal_sharma_resume.pdf"
profile_pic = current_dir / "assets" / "profile-pic (1).png"


# --- GENERAL SETTINGS ---
PAGE_TITLE = "Digital CV | Pranjal Sharma"
PAGE_ICON = ":wave:"
NAME = "Pranjal Sharma"
DESCRIPTION = """
Software Engineer, assisting in problem solving and supporting data-driven decision-making in Cloud and AI.
"""
EMAIL = "pranjals.dev@gmail.com"
SOCIAL_MEDIA = {
    "YouTube": "https://youtube.com/c/PranjalGuitarist",
    "LinkedIn": "https://linkedin.com/in/pranjalsharmaa/",
    "GitHub": "https://github.com/pranjalsharmaa",
    "Twitter": "https://x.com/itsprnjl",
}
PROJECTS = {
    "🏆 Google Cloud Certified - Professional Machine Learning Engineer": "https://www.credential.net/fc4739e1-a34e-4a7b-a1cc-549ba8309ff1?key=822e89fd3176ca48d647471d466ace21a1fa4fbd1a6763798a44f64f004e63dc",
    "🏆 The joy of Computing using Python - NPTEL, IIT Madras": "https://drive.google.com/file/d/1euYLqjliuh7n8KShBpDbbfyzCMAaR2ng/view?usp=sharing",
    "🏆 Served as a Student Coordinator for the Institute Innovation Cell, LNCT Bhopal": "https://drive.google.com/file/d/1WShCzQElnHdIclhUPF2JqfPgCYoBNPPw/view?usp=sharing",
    "🏆 Awarded by MIC Organization, Indore (M.P.) for educating young minds of the nation during the lockdown.": " ",
    "🏆 More than 100K Views on my YouTube Channel, following my passion for making videos about Guitar & Music.": "https://youtube.com/c/PranjalGuitarist"
}


st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)


# --- LOAD CSS, PDF & PROFIL PIC ---
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
profile_pic = Image.open(profile_pic)


# --- HERO SECTION ---
col1, col2 = st.columns(2, gap="small")
with col1:
    st.image(profile_pic, width=230)

with col2:
    st.title(NAME)
    st.write(DESCRIPTION)
    st.write("Bachelors of Technology (with Hons.)")
    st.write("Madhya Pradesh, India")
    st.download_button(
        label=" 📄 Download CV",
        data=PDFbyte,
        file_name=resume_file.name,
        mime="application/octet-stream",
    )
    st.write("📫", EMAIL)


# --- SOCIAL LINKS ---
st.write('\n')
cols = st.columns(len(SOCIAL_MEDIA))
for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
    cols[index].write(f"[{platform}]({link})")


# --- EXPERIENCE & QUALIFICATIONS ---
st.write('\n')
st.subheader("Experience & Qualifications")
st.write(
    """
- ✔️ 2 Years expereince in Information and Technology.
- ✔️ Strong hands on experience and knowledge in Python and GCP/AWS Cloud.
- ✔️ Good understanding of statistical principles and their respective applications
- ✔️ Excellent team-player and displaying strong sense of initiative on tasks
"""
)


# --- SKILLS ---
st.write('\n')
st.subheader("Hard Skills")
st.write(
    """
- 👩‍💻 Technologies & Platforms: Python (Fine-tuning, Scikit-learn, Pandas, Numpy, Deep Learning), Core Java, SQL, Object Oriented Programming, AWS Platform, Event-Driven Architecture, Layers,
Google Cloud, AutoML, Deep Learning, HTML5, MySQL, Vertex AI, VS Code and GitHub. 
- 🗄️ Databases: Postgres, MongoDB, MySQL
"""
)


# --- WORK HISTORY ---
st.write('\n')
st.subheader("Work History")
st.write("---")

# --- JOB 1
st.write("🚧", "**Software Engineer | Global Technology Solutions Inc.**")
st.write("11/2023 - Present")
st.write(
    """
- ► Deployed Intelligent Document Processing on AWS using CloudFormation, CloudFront, Lambda, S3, Cognito & IAM roles; developed a merging algorithm with AWS Textract and PyMuPDF.
- ► Automated conversation analysis and export in CCAI Insights using Google Cloud Functions and Scheduler.
- ► Built and deployed a Streamlit AI Agent for RAG tasks, interacting with AWS Bedrock and Lex on EC2.
"""
)

# --- JOB 2
st.write('\n')
st.write("🚧", "**Software Engineer | Quantiphi Inc.**")
st.write("08/2018 - 05/2023")
st.write(
    """
- ► Led successful projects and POCs in an R&D environment, collaborating with cross-functional teams and presenting video demos to stakeholders.
- ► Tackled complex optimization challenges on GCP, followed Agile methodology with ASANA, and maintained comprehensive documentation.
- ► Completed a 6-week deep learning and GCP training, achieved a score of 4.2/5, and developed reusable assets for the company's IP repository.
"""
)

# --- JOB 3
st.write('\n')
st.write("🚧", "**Software Engineer Intern | Persistent Systems**")
st.write("12/2022 - 07/2023")
st.write(
    """
- ► GEMS participant, mastering Software Development Fundamentals, OOP, SDLC, and Agile Methodology, and engaging in team activities.
- ► Developed a Project Management Tool with OutSystems for the IBA Business Unit, demonstrating expertise in JavaScript and HTML5.
- ► Collaborated with a cross-functional team using Agile and GitHub, contributing to the success of the Enterprise Payroll Application with high-quality frontend solutions.
"""
)


# --- Projects & Accomplishments ---
st.write('\n')
st.subheader("Certificates & Accomplishments")
st.write("---")
for project, link in PROJECTS.items():
    st.write(f"[{project}]({link})")