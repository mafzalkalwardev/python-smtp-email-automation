<div align="center">

# 🚀 Python SMTP Email Automation

**A Python SMTP email automation tool that sends personalized emails from Excel data using Gmail App Passwords, randomized templates, retries, and safe delays.**

Documented · MIT licensed · Maintained

[![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge)](LICENSE)
[![PRs](https://img.shields.io/badge/PRs-welcome-brightgreen?style=for-the-badge)](CONTRIBUTING.md)

</div>

---

## 🐍 Contribution graph

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/mafzalkalwardev/python-smtp-email-automation/output/snake-dark.svg" />
  <source media="(prefers-color-scheme: light)" srcset="https://raw.githubusercontent.com/mafzalkalwardev/python-smtp-email-automation/output/snake.svg" />
  <img alt="Contribution snake" src="https://raw.githubusercontent.com/mafzalkalwardev/python-smtp-email-automation/output/snake.svg" />
</picture>

---

\# Python SMTP Email Automation

A Python-based email automation tool that sends personalized emails using SMTP and Gmail App Passwords. It reads recipient data from an Excel file and sends customized email messages with randomized templates and safe delays.

\## Screenshots

## Features

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
