# 🧠 Google Form Feedback Summarizer

This automation project captures responses from a Google Form, summarizes the feedback using OpenAI's GPT-3.5, and posts the summary with category to a designated Slack channel. Built as part of a technical showcase for Zschool’s AI/ML Automation Internship.

---

## 🚀 Project Overview

- **Goal:** Automate the process of gathering, understanding, and sharing user feedback efficiently.
- **Tools Used:**
  - Python
  - Google Sheets API (via `gspread`)
  - OpenAI GPT-3.5 API
  - Slack Webhook Integration
- **Outcome:** Automatically posts summaries of Google Form responses into Slack, including categorization (e.g., Urgent, General, Follow-up).

---

## 🛠️ How to Set Up & Run

### 1. Clone this repository
Click the green `Code` button > `Download ZIP` or use:

git clone https://github.com/DhruvalAnandkar/google-form-feedback-summarizer/tree/main.git

pip install openai gspread oauth2client requests

### 2. Install dependencies

Make sure you have Python installed. 
Then run:
pip install openai gspread oauth2client requests

### 3. Set up Google Sheets API
Go to Google Cloud Console.

Create a project and enable Google Sheets API + Google Drive API.

Create a Service Account and download the JSON key file (name it service_account_key.json).

Share your Google Sheet with the service account email (with edit access).

### 4. Update your config in the script
Open your Python script (summarizer.py) and update:

openai.api_key = "YOUR_OPENAI_API_KEY"
SLACK_WEBHOOK_URL = "YOUR_SLACK_WEBHOOK_URL"
SHEET_NAME = "Your Google Sheet Name"

### 5. Run the script
Make sure your Google Sheet contains responses from the form. 
Then:
python summarizer.py

💡 Example Output on Slack:

📬 New Feedback Submission!
👤 Name: Dhruval Anandkar  
📧 Email: dhruval@gmail.com
📝 Message: I had a great experience using your platform, but the dashboard loads slowly when I access it from my phone.  
⚡ Priority: High
Summary: Positive feedback on platform experience, with a request to improve mobile performance.  
Category: Follow-up
