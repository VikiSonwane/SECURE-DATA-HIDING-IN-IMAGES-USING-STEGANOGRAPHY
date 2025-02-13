# SECURE-DATA-HIDING-IN-IMAGES-USING-STEGANOGRAPHY
This project integrates AES-128 encryption with Least Significant Bit (LSB) steganography to securely hide and retrieve encrypted messages within images. It ensures confidential communication while making the hidden data undetectable.


Secure Image Steganography with AES Encryption

Project Overview

This project combines AES encryption with LSB-based image steganography to securely hide and retrieve encrypted messages within images. 
The system ensures confidential communication while making the hidden message undetectable to casual observers.

Features

🔒 AES-128 Encryption to secure the message before embedding.

🖼️ Least Significant Bit (LSB) Steganography for hiding data in an image.

🔑 Automated AES Key Generation & Management.

📌 End Marker Detection for precise message retrieval.

🌍 Cross-Platform Support (Windows, Linux, macOS).

Technologies & Libraries Used

Python 3.x

cv2 (OpenCV) – For image processing

numpy – For handling image data

Crypto (PyCryptodome) – For AES encryption/decryption

base64 – For encoding messages

secrets – For generating secure AES keys

tkinter (optional) – For GUI integration

Installation & Setup

1. Clone the Repository

git clone https://github.com/yourusername/steganography-aes.git
cd steganography-aes

2. Install Required Dependencies

pip install opencv-python numpy pycryptodome


Usage

1. Hiding a Message

python app.py

Enter the secret message to hide.

The encrypted message will be embedded into encoded.jpg.

2. Extracting a Hidden Message

If prompted, select 'Y' to extract the hidden message.

The decrypted message will be displayed.

End Users

Cybersecurity professionals for secure communication.

Journalists & whistleblowers for discreet data sharing.

Law enforcement & forensic teams for evidence hiding.

Privacy-conscious individuals who want hidden communication.

Future Enhancements

✅ GUI Interface using Tkinter/PyQt for ease of use. 
✅ Support for PNG, BMP, and TIFF formats. 
✅ AES-256 & Hybrid Encryption (AES + RSA). 
✅ Cloud-based storage for secure sharing. 
✅ Mobile & Web Applications.

Contributing

Feel free to fork the repository and submit pull requests!

Report issues via the GitHub Issues section.

License

This project is licensed under the MIT License.

🔹 Author: Your Name
🔹 GitHub: YourUsername
🔹 Email: your.email@example.com

