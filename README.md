# Digital CV | Pranjal Sharma

This repository contains the code for a digital CV created using Streamlit for Pranjal Sharma, a Software Engineer with experience in problem-solving and supporting data-driven decision-making in Cloud and AI.

## Table of Contents

- [Demo](#demo)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Content](#content)
- [License](#license)

## Demo

You can check out the live demo of the Digital CV [here](https://digital-cv-dspb.onrender.com/).

## Features

- Professional CV layout
- Downloadable PDF resume
- Social media links
- Detailed experience and qualifications
- Display of hard skills
- Work history section
- Certificates and accomplishments

## Installation

To run this application locally, follow these steps:

1. Clone the repository:
    ```bash
    git clone https://github.com/pranjalsharmaa/digital-cv.git
    cd digital-cv
    ```

2. Create a virtual environment and activate it:
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

3. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. Make sure you have the assets and styles in the appropriate directories:
    ```
    digital-cv/
    ├── assets/
    │   ├── pranjal_sharma_resume.pdf
    │   └── profile-pic (1).png
    └── styles/
        └── main.css
    ```

2. Run the Streamlit app:
    ```bash
    streamlit run app.py
    ```

3. Open your web browser and go to the provided local URL (usually `http://localhost:8501`).

## Content

### PATH SETTINGS

- **current_dir**: Sets the current directory for the app.
- **css_file**: Path to the CSS file for custom styles.
- **resume_file**: Path to the PDF resume file.
- **profile_pic**: Path to the profile picture.

### GENERAL SETTINGS

- **PAGE_TITLE**: Title of the web page.
- **PAGE_ICON**: Icon for the web page.
- **NAME**: Name of the individual.
- **DESCRIPTION**: Short description or bio.
- **EMAIL**: Contact email.
- **SOCIAL_MEDIA**: Dictionary containing social media platforms and their links.
- **PROJECTS**: Dictionary containing projects and accomplishments with their links.

### HERO SECTION

Displays the profile picture, name, description, and download button for the resume.

### SOCIAL LINKS

Displays social media links in a row.

### EXPERIENCE & QUALIFICATIONS

Lists experience and qualifications.

### SKILLS

Lists hard skills including technologies, platforms, and databases.

### WORK HISTORY

Lists work history with job titles, companies, and descriptions of responsibilities and achievements.

### PROJECTS & ACCOMPLISHMENTS

Lists certificates and accomplishments with links.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
