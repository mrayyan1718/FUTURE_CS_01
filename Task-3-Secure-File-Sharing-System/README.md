# 🔐 Task 3 – Secure File Sharing System

As part of the **Future Interns Cyber Security Internship**, this project demonstrates a secure file upload and download system using **Python Flask** and **AES encryption** to protect files both at rest and in transit.

---

## 🚀 Overview

This secure portal allows users to upload files, which are then encrypted using AES (GCM mode) and stored safely on the server. Files can be downloaded later with automatic decryption. Security, usability, and clean UI were prioritized.

---

## 💡 Key Features

- 🔐 AES Encryption (GCM) for confidentiality and integrity  
- 📁 File upload and download via a simple web interface  
- 🧠 Key derivation using PBKDF2 with salt  
- 🛡️ Secure encrypted storage using a `.enc` file format  
- 🎨 Responsive Bootstrap 5 UI for ease of use  
- 📋 Flash messages for user feedback on actions  
- ✅ Upload validation with file size and extension restrictions  

---

## 🧱 Tech Stack

- **Backend:** Python Flask  
- **Encryption:** PyCryptodome (AES, PBKDF2)  
- **Frontend:** HTML, Bootstrap 5, Bootstrap Icons  
- **Utilities:** Werkzeug for secure filenames, Python `os` and `io` modules  
- **Version Control:** Git & GitHub  

---

## 📁 Project Structure
undefined
Task3/
├── app.py # Main Flask application (backend logic)
├── encryption.py # AES encryption and key derivation helper functions
├── requirements.txt # Python dependencies list (Flask, PyCryptodome)
├── uploads/ # Folder to store encrypted files (.enc)
├── templates/ # Folder containing HTML template files
│ └── index.html # Main UI template (Bootstrap-based web page)
├── screenshots/ # (Optional) folder storing project screenshots
│ ├── HomePage.png
│ ├── FileSelection.png
│ ├── Upload.png
│ ├── FileListWithDownload.png
│ ├── FileDownloaded.png
│ ├── Uploads.png
│ ├── TerminalRunning.png
│ └── ErrorMessage.png
└── pycache/ # Python bytecode cache (auto-generated, can be ignored)
undefined
---

## 🧪 How It Works

1. User selects and uploads a file via the web UI.  
2. Uploaded file gets encrypted using AES-GCM with a key derived from a password via PBKDF2 with random salt.  
3. The encrypted file is saved on the server with a `.enc` extension.  
4. When downloading, the server decrypts the file on-the-fly and serves the original content securely.  
5. All actions display success or error messages on the UI using Bootstrap flash alerts.  
6. Server logs upload/download events in the terminal for audit and debugging.

---

## ⚙️ Setup Instructions

1. Clone your repo and navigate to the Task 3 folder
git clone https://github.com/mrayyan1718/FUTURE_CS_01.git
cd FUTURE_CS_01/Task-3-Secure-File-Sharing-System


2. Create and activate a Python virtual environment
python -m venv venv

Windows:
venv\Scripts\activate

macOS/Linux:
source venv/bin/activate

3. Install dependencies
pip install -r requirements.txt

4. (Optional) Set encryption password environment variable (recommended for security)
Windows:
set ENCRYPTION_PASSWORD=YourStrongPassword

macOS/Linux:
export ENCRYPTION_PASSWORD=YourStrongPassword

5. Run the Flask app
python app.py


Open [http://127.0.0.1:5000](http://127.0.0.1:5000) in your web browser to use the application.

---

## 🔒 Security Notes

- Uses AES-GCM for authenticated encryption to ensure confidentiality and integrity.  
- Encryption key is derived securely with PBKDF2 and a unique salt per file.  
- Uploaded files are limited to 10 MB.  
- Only allows specific file extensions: `txt`, `pdf`, `png`, `jpg`, `zip`, `docx`.  
- Password is configurable via environment variable; never hardcoded for production.  
- Files are never stored unencrypted on server disk.  

---

## 📸 Screenshots

| UI Section                  | Screenshot Filename           |
|----------------------------|------------------------------|
| Home Page                  | HomePage.png                 |
| File Selection Dialog      | FileSelection.png            |
| Upload Confirmation        | Upload.png                   |
| Uploaded Files List        | FileListWithDownload.png     |
| File Download Process      | FileDownloaded.png           |
| Encrypted Files in `uploads/` Folder | Uploads.png          |
| Flask Terminal Running     | TerminalRunning.png          |
| Error Message Example      | ErrorMessage.png             |

_All screenshots are located in the `/screenshots` directory._

---

## 📜 License

This project is part of the **Future Interns Cyber Security Internship** and meant for educational purposes.

---

## 🙌 Acknowledgments

Thanks to Future Interns for the opportunity to gain practical hands-on experience in cybersecurity development.

---

If you want me to help prepare a combined README for all internship tasks or any additional documentation, just let me know!
