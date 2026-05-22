\# Python SMTP Email Automation



A Python-based email automation tool that sends personalized emails using SMTP and Gmail App Passwords. It reads recipient data from an Excel file and sends customized email messages with randomized templates and safe delays.



\## Features



\- Send emails using Gmail SMTP

\- Read recipients from Excel file

\- Personalized email templates

\- Random subject and body rotation

\- Email validation

\- Retry failed emails

\- Random delay between emails

\- Simple Python script structure



\## Tech Stack



\- Python

\- Pandas

\- OpenPyXL

\- SMTP

\- Gmail App Password



\## Folder Structure



```text

python-smtp-email-automation/

│

├── mailer.py

├── README.md

├── .gitignore

└── emails.xlsx





Excel File Format



Your emails.xlsx file should contain these columns:



Email	Name	State

example@gmail.com	John	TX

Installation

pip install pandas openpyxl

How to Run

python mailer.py

Security Note



Do not upload your Gmail App Password publicly. Keep passwords in environment variables or a .env file.



Author



Muhammad Afzal Kalwar

GitHub: @mafzalkalwardev

