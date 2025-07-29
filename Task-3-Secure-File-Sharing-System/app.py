import os
import io
from flask import Flask, request, render_template, send_file, flash, redirect, url_for
from werkzeug.utils import secure_filename
from encryption import derive_key, encrypt_file, decrypt_file

UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'zip', 'docx'}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.secret_key = 'CHANGE_THIS_SECRET'
app.config['MAX_CONTENT_LENGTH'] = 10 * 1024 * 1024  # 10 MB file size limit

PASSWORD = os.environ.get('ENCRYPTION_PASSWORD', 'defaultpass')  # Set via env for real security!

os.makedirs(UPLOAD_FOLDER, exist_ok=True)

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/', methods=['GET', 'POST'])
def index():
    files = [f for f in os.listdir(UPLOAD_FOLDER) if f.endswith('.enc')]
    files.sort()
    return render_template('index.html', files=files)

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        flash('No file part found.', 'warning')
        return redirect(url_for('index'))
    file = request.files['file']
    if not file or file.filename == '':
        flash('No file selected.', 'warning')
        return redirect(url_for('index'))
    if not allowed_file(file.filename):
        flash('Invalid file type! Allowed: txt, pdf, png, jpg, zip, docx', 'danger')
        return redirect(url_for('index'))

    filename = secure_filename(file.filename)
    try:
        data = file.read()
        key, salt = derive_key(PASSWORD)
        encrypted = encrypt_file(data, key)
        enc_path = os.path.join(UPLOAD_FOLDER, filename + '.enc')
        with open(enc_path, 'wb') as f:
            f.write(salt + encrypted)
        flash(f'"{filename}" uploaded and encrypted successfully!', 'success')
    except Exception as e:
        flash('File encryption/upload failed. Error: {}'.format(str(e)), 'danger')
    return redirect(url_for('index'))

@app.route('/download/<filename>')
def download_file(filename):
    enc_path = os.path.join(UPLOAD_FOLDER, filename)
    if not os.path.exists(enc_path):
        flash('File not found!', 'warning')
        return redirect(url_for('index'))
    try:
        with open(enc_path, 'rb') as f:
            blob = f.read()
        salt = blob[:16]
        encrypted = blob[16:]
        key, _ = derive_key(PASSWORD, salt)
        decrypted = decrypt_file(encrypted, key)
        original_name = filename.replace('.enc', '')
        return send_file(
            io.BytesIO(decrypted),
            as_attachment=True,
            download_name=original_name,
        )
    except Exception as e:
        flash(f'Decryption failed: {str(e)}', 'danger')
        print("Decryption error:", str(e))  # Important: prints exact error in console
        return redirect(url_for('index'))



if __name__ == "__main__":
    app.run(debug=True)
