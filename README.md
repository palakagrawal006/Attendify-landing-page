# Attendify: Landing Page
 
Responsive marketing page for **[Attendify](https://github.com/palakagrawal006/Attendify-AI-Attendance)**, an AI-powered attendance system with face and voice recognition.
 
**[Live site](https://attendify-ai-attendance.vercel.app/)** · **[Launch the app](https://attendify-ai-attendance.streamlit.app/)**
 
![Landing page](static/img/demo/teacher2.png)
 
## What's on the page
 
- Hero section with a product screenshot
- Features overview
- **How it works** with separate Teacher and Student journeys 
- Tech stack
- Call to action and footer
## Tech stack
 
Flask, HTML and CSS. Deployed on Vercel.
 
## Project structure
 
```
app.py              # Flask app (serves templates/index.html)
templates/
  index.html
static/
  css/style.css
  img/              # icon and demo screenshots
requirements.txt
vercel.json
```
 
## Run locally
 
```bash
git clone https://github.com/YOUR-USERNAME/YOUR-LANDING-REPO.git
cd Attendify-landing-page
python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
pip install -r requirements.txt
python app.py
```
 
Open http://localhost:5002.
 
## Deploy
 
Import the repo on [Vercel](https://vercel.com). No build settings are needed; `vercel.json` handles the Flask setup. Update the app link in `templates/index.html` if your Streamlit URL changes.
 
## Customise
 
- Colours are CSS variables at the top of `static/css/style.css`.
- To change screenshots, replace the files in `static/img/demo/` and keep the same names.
## Related
 
- App repository: [https://github.com/palakagrawal006/Attendify-AI-Attendance](https://github.com/palakagrawal006/Attendify-AI-Attendance)
- Live app: [https://attendify-ai-attendance.streamlit.app/](https://attendify-ai-attendance.streamlit.app/)
## Author
 
Built by Palak Agrawal.
