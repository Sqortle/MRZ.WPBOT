
# 📱 WhatsApp Online Status Notifier with Email Alerts

This Python script uses **Selenium WebDriver** and the **SMTP** protocol to monitor a specific contact's online/offline status on **WhatsApp Web** and sends email notifications when the status changes.

---

## 🚀 Features

- Track a contact’s online/offline status on WhatsApp Web
- Receive instant email notifications when the contact goes online or offline
- Calculate and notify how long the contact stayed online
- Automate browser interaction and click buttons via XPath

---

## 🛠 Requirements

- Python 3.8 or later
- Firefox browser
- [GeckoDriver](https://github.com/mozilla/geckodriver/releases)
- Gmail account with SMTP access (App Password recommended)

---

## ⚙️ Installation

1. Install required packages:
    ```bash
    pip install selenium
    ```

2. Download GeckoDriver and update the script with its path:
    ```python
    path = '/your/gecko/driver/path'
    ```

3. Replace the placeholders in the script:
    - `<YOUR EMAIL>` → The email address where notifications will be sent
    - `<WPBOT EMAIL>` → The sender Gmail address
    - `<<PASSWORD KEY>>` → Your Gmail app password
    - `'Target Button'` → XPath of the WhatsApp contact chat
    - `'Your Online Button'` → XPath of the "online" label when contact is online

---

## ▶️ Usage

1. Run the script:
    ```bash
    python main.py
    ```

2. Scan the QR code on WhatsApp Web when prompted.

3. Make sure the XPath targets the desired contact and online status element.

4. The script will send an email when the contact comes online and another when they go offline, including how long they were online.

---

## 📨 SMTP Email Notification

- Gmail SMTP server: `smtp.gmail.com`, port: `587`
- Secure connection via `starttls()`
- Sender and receiver email addresses can be the same

---

## ⚠️ Warnings

- WhatsApp Web UI and XPath structure may change over time. Make sure to update XPath selectors accordingly.
- Running the script for long periods may trigger security checks by WhatsApp or Gmail.
- This script is intended for personal and educational use only. Monitoring others without consent may be illegal in your jurisdiction.

---

**⚠️ Note:** This script is intended for educational and automation practice purposes only. Please comply with WhatsApp’s Terms of Service and local laws.
