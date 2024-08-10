from flask import Flask, request, render_template, send_file
from encryption import process_image

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        encrypted_file = request.files['encrypted_image']
        key_file = request.files['key']
        if encrypted_file and key_file:
            encrypted_file.save('encrypted_image.png')
            key_file.save('key.npy')
            process_image('encrypted_image.png', 'key.npy', encrypt=False)
            return render_template('result.html', image='decrypted_image.png', action='decrypt')
    return render_template('decrypt.html')

@app.route('/download/<filename>')
def download_file(filename):
    return send_file(filename, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
