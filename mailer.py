import pandas as pd
import smtplib
import time
import random
from email.message import EmailMessage
from typing import Optional

# ===== Configuration =====
EXCEL_FILE = "emails.xlsx"
SENDER_EMAIL = "jack.adam.12120@gmail.com"
SENDER_PASSWORD = "mdnd exgi tgch csvi"  # Use app password for Gmail
EMAIL_SENDER_NAME = "Jack Adam"
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 465
MIN_DELAY = 3   # minimum seconds between emails
MAX_DELAY = 10  # maximum seconds between emails
MAX_RETRIES = 2

# ===== Email Templates =====
SUBJECT_TEMPLATES = [
    "Keep Your Trucks Moving – {state} Local & OTR Freight Available",
    "Idle Trucks? Let's Fill Them With {state} Freight",
    "{state} Local & OTR Freight – Ready When You Are",
    "Keep Your Trucks Loaded – {state} Freight Available Now",
    "{state} Freight Available – Local & OTR Loads Moving Today"
]

EMAIL_BODIES = [
    """Hi {Name},
Hope you're doing well.
We've got both local and OTR loads ready now in {state} — including backhauls — to keep your trucks busy and your revenue strong.
If you have any equipment sitting idle, just share your ZIP code and MC#, and I'll match you with the best-paying loads right away.
Let's keep your fleet rolling!
Best regards,
{EMAIL_SENDER_NAME}
{SENDER_EMAIL}""",

    """Hi {Name},
Hope things are running smoothly on your end.
We're matching carriers with high-paying local and OTR freight in {state}, plus backhauls, to help you maximize your earnings.
If you've got trucks parked, send me your ZIP code and MC# and I'll connect you to the top loads in your area.
Let's get those wheels turning!
Best,
{EMAIL_SENDER_NAME}
{SENDER_EMAIL}""",

    """Hi {Name},
Hope your week's going great.
We have freight ready to move in {state} — local runs, OTR lanes, and backhauls — to keep your wheels turning and your cash flow steady.
Reply with your ZIP code and MC#, and I'll start locking in the best loads for you today.
Talk soon,
{EMAIL_SENDER_NAME}
{SENDER_EMAIL}""",

    """Hi {Name},
Hope everything's going well with you.
We have local, OTR, and backhaul loads available right now in {state} to keep your trucks loaded and profitable.
If your equipment's ready, send me your ZIP code and MC# so I can secure the best-paying loads for you ASAP.
Let's make it happen,
{EMAIL_SENDER_NAME}
{SENDER_EMAIL}""",

    """Hi {Name},
Hope business is running strong.
We have immediate freight opportunities in {state} — local, OTR, and backhauls — so your trucks never sit idle.
Just send me your ZIP code and MC#, and I'll get to work finding the most profitable loads for your lanes.
Looking forward to working with you,
{EMAIL_SENDER_NAME}
{SENDER_EMAIL}"""
]

# Shuffle templates once per run
EMAIL_TEMPLATES = list(zip(SUBJECT_TEMPLATES, EMAIL_BODIES))
random.shuffle(EMAIL_TEMPLATES)
current_template_idx = 0

# ===== Helpers =====
def validate_email(email: str) -> bool:
    """Simple email format check: must contain '@' and at least one '.' after '@'"""
    if not isinstance(email, str):
        return False
    email = email.strip()
    if "@" not in email:
        return False
    local, _, domain = email.partition("@")
    if not local or "." not in domain:
        return False
    return True

def get_next_template() -> tuple:
    """Cycle through shuffled templates"""
    global current_template_idx
    template = EMAIL_TEMPLATES[current_template_idx]
    current_template_idx = (current_template_idx + 1) % len(EMAIL_TEMPLATES)
    return template

def get_state(row: pd.Series) -> str:
    """Safely extract state"""
    state = str(row['State']).strip().upper() if pd.notna(row['State']) else "N/A"
    return state if state else "N/A"

# ===== Main Execution =====
try:
    df = pd.read_excel(EXCEL_FILE, engine='openpyxl')
    print(f"📂 Loaded {len(df)} recipients from {EXCEL_FILE}")
except Exception as e:
    print(f"🚨 Excel Error: {e}")
    exit()

# Check required columns
if not {'Email', 'Name', 'State'}.issubset(df.columns):
    print("🚨 Missing required columns: must include Email, Name, and State")
    exit()

# Connect to SMTP server
try:
    server = smtplib.SMTP_SSL(SMTP_SERVER, SMTP_PORT, timeout=10)
    server.login(SENDER_EMAIL, SENDER_PASSWORD)
    print("✅ Logged into SMTP server")
except Exception as e:
    print(f"🚨 SMTP Error: {e}")
    exit()

success_count = 0
for index, row in df.iterrows():
    recipient_email = str(row['Email']).strip()
    
    if not validate_email(recipient_email):
        print(f"⏭️ Skipping invalid email: {recipient_email}")
        continue

    state = get_state(row)
    if state == "N/A":
        print(f"⏭️ Missing state for {recipient_email}")
        continue

    subject_template, body_template = get_next_template()

    for attempt in range(MAX_RETRIES):
        try:
            msg = EmailMessage()
            msg["From"] = f"{EMAIL_SENDER_NAME} <{SENDER_EMAIL}>"
            msg["To"] = recipient_email
            msg["Subject"] = subject_template.format(state=state)
            
            msg.set_content(body_template.format(
                Name=row['Name'],
                state=state,
                EMAIL_SENDER_NAME=EMAIL_SENDER_NAME,
                SENDER_EMAIL=SENDER_EMAIL
            ))
            
            server.send_message(msg)
            success_count += 1
            print(f"✅ Sent to {recipient_email} (Subject: {msg['Subject']})")
            break

        except Exception as e:
            if attempt == MAX_RETRIES - 1:
                print(f"🚨 Failed {recipient_email} after {MAX_RETRIES} attempts: {e}")
            else:
                print(f"⚠️ Error sending to {recipient_email}, retrying...")
                time.sleep(5)

    # Delay before next email
    delay = random.uniform(MIN_DELAY, MAX_DELAY)
    print(f"⏳ Waiting {delay:.1f}s before next email...")
    time.sleep(delay)

server.quit()
print(f"\n📬 Finished: Sent {success_count}/{len(df)} emails successfully")