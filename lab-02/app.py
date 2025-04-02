from flask import Flask, render_template, request, json
from cipher.caesar import CaesarCipher
from cipher.vigenere import VigenereCipher
from cipher.railfence import RailFenceCipher
from cipher.playfair import PlayFairCipher
import os
import subprocess
app = Flask(__name__)

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/caesar")
# def caesar():
    # return render_template('caesar.html')

def caesar():
    caesar_path = os.path.join('lab-03', 'caesar_cipher.py')
    subprocess.Popen(['python', caesar_path])  # Mở ứng dụng PyQt5
    return "Caesar Cipher application is opened!"

@app.route("/caesar/encrypt", methods=['POST'])
def caesar_encrypt():
    text = request.form['inputPlainText']
    key = int(request.form['inputKeyPlain'])
    Caesar = CaesarCipher()
    encrypted_text = Caesar.encrypt_text(text, key)
    return f"text: {text}<br/>key: {key}<br/>encrypted text: {encrypted_text}"

@app.route("/caesar/decrypt", methods = ['POST'])
def caesar_decrypt():
    text = request.form['inputCipherText']
    key = int(request.form['inputKeyCipher'])
    Caesar = CaesarCipher()
    decrypted_text = Caesar.decrypt_text(text, key)
    return f"text: {text}<br/>key: {key}<br/>decrypted text: {decrypted_text}"
#VIGENERE
@app.route("/vigenere")
def vigenere():
#     return render_template('vigenere.html')
    vigenere_path = os.path.join('lab-03', 'vigenere_cipher.py')
    subprocess.Popen(['python', vigenere_path])  # Mở ứng dụng PyQt5
    return "VVigenerear Cipher application is opened!"

@app.route("/vigenere/encrypt", methods=['POST'])
def vigenere_encrypt():
    text = request.form['inputPlainText']
    key = request.form['inputKeyPlain']
    Vigenere = VigenereCipher()
    encrypted_text = Vigenere.vigenere_encrypt(text, key)
    return f"text: {text}<br/>key: {key}<br/>encrypted text: {encrypted_text}"

@app.route("/vigenere/decrypt", methods = ['POST'])
def vigenere_decrypt():
    text = request.form['inputCipherText']
    key = request.form['inputKeyCipher']
    Vigenere = VigenereCipher()
    decrypted_text = Vigenere.vigenere_decrypt(text, key)
    return f"text: {text}<br/>key: {key}<br/>decrypted text: {decrypted_text}"

#PLAYFAIR
@app.route("/playfair")
def playfair():
    # return render_template('playfair.html')
    playfair_path = os.path.join('lab-03', 'playfair_cipher.py')
    subprocess.Popen(['python', playfair_path])  # Mở ứng dụng PyQt5
    return "Playfair Cipher application is opened!"

@app.route("/playfair/encrypt", methods=['POST'])
def playfair_encrypt():
    text = request.form['inputPlainText']
    key = request.form['inputKeyPlain']
    Playfair = PlayFairCipher()
    matrix = Playfair.create_playfair_matrix(key)
    encrypted_text = Playfair.playfair_encrypt(text, matrix)
    return f"text: {text}<br/>key: {key}<br/>encrypted text: {encrypted_text}"

@app.route("/playfair/decrypt", methods = ['POST'])
def playfair_decrypt():
    text = request.form['inputCipherText']
    key = request.form['inputKeyCipher']
    Playfair = PlayFairCipher()
    matrix = Playfair.create_playfair_matrix(key)
    decrypted_text = Playfair.playfair_decrypt(text, matrix)
    return f"text: {text}<br/>key: {key}<br/>decrypted text: {decrypted_text}"


#RAILFENCE
@app.route("/railfence")
def railfence():
    # return render_template('railfence.html')
    railfence_path = os.path.join('lab-03', 'railfence_cipher.py')
    subprocess.Popen(['python', railfence_path])  # Mở ứng dụng PyQt5
    return "Railfence Cipher application is opened!"

@app.route("/railfence/encrypt", methods=['POST'])
def railfence_encrypt():
    text = request.form['inputPlainText']
    key = int(request.form['inputKeyPlain'])
    RailFence = RailFenceCipher()
    encrypted_text = RailFence.rail_fence_encrypt(text, key)
    return f"text: {text}<br/>key: {key}<br/>encrypted text: {encrypted_text}"

@app.route("/railfence/decrypt", methods = ['POST'])
def railfence_decrypt():
    text = request.form['inputCipherText']
    key = int(request.form['inputKeyCipher'])
    RailFence = RailFenceCipher()
    decrypted_text = RailFence.rail_fence_decrypt(text, key)
    return f"text: {text}<br/>key: {key}<br/>decrypted text: {decrypted_text}"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5050, debug = True)