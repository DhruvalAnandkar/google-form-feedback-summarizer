import openai
import gspread
from openai import OpenAI
from oauth2client.service_account import ServiceAccountCredentials
import requests


client  = OpenAI(api_key ="YOURAPIKEY")

SLACK_WEBHOOK_URL = "YOUR_SLACK_WEBHOOK_URL"

scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name("Your_service_account_key.json", scope)
gs_client = gspread.authorize(creds)

sheet = gs_client.open("Summerizer").sheet1
data = sheet.get_all_records()
last_response = data[-1] if data else {}
name = last_response.get("Name", "Unknown")
email = last_response.get("Email", "Not provided")
message = last_response.get("Message", "")
priority = last_response.get("Priority", "Medium")
def summarize_and_categorize(text):
    prompt = f"""
    You are a helpful assistant. Please summarize the following message and categorize it as one of: Urgent, General, or Follow-up.

    Message:
    {text}

    Format the output like this:
    Summary: <short summary>
    Category: <Urgent/General/Follow-up>
    """
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You summarize feedback and categorize it."},
            {"role": "user", "content": prompt.strip()}
        ],
        temperature=0.5,
        max_tokens=200
    )
    return response.choices[0].message.content.strip()
def send_to_slack(message):
    payload = {"text": message}
    response = requests.post(SLACK_WEBHOOK_URL, json=payload)
    if response.status_code != 200:
        print("Slack notification failed:", response.text)
    else:
        print("Sent to Slack successfully.")
if message:
    summary_block = summarize_and_categorize(message)

    slack_message = f"""
*New Feedback Submission!*
*Name:* {name}
*Email:* {email}
*Message:* {message}
*Priority (by user):* {priority}

{summary_block}
    """
    send_to_slack(slack_message)
else:
    print("No message found in the last response.")

print("Done!")