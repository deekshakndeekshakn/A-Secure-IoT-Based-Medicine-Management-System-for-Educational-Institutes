# A-Secure-IoT-Based-Medicine-Management-System-for-Educational-Institutes
This project is a Secure IoT-Based Medicine Management System built in Python on Raspberry Pi. It integrates keypad-based password authentication, barcode scanning for student identification, automated medicine dispensing using DC motors, Excel logging, and Adafruit IO for cloud monitoring. Designed for schools, colleges, and hostel medical centers

## 🔑 Key Features

Developed in Python for seamless hardware and cloud integration.

**Password-Protected Access –** Authentication via keypad ensures only authorized staff (doctors/nurses) can operate.

**Barcode Scanning –** Identifies students/patients using unique ID cards.

**Automated Dispensing –** DC motors release medicines when corresponding buttons are pressed.

**Excel Logging –** Saves student ID, timestamp, and medicine details into medicine.xlsx.

**Cloud Monitoring –** Data is uploaded to Adafruit IO feeds for real-time tracking.

**LCD Feedback –** Displays prompts, scanned IDs, and medicine counts in real time.

## 🛠️ Tech Stack & Components

**Programming Language:** Python

**Hardware:** Raspberry Pi, DC motors, USB Barcode Scanner, Push Buttons, Keypad, I2C LCD

**Libraries Used:**

RPi.GPIO → GPIO control for motors & switches

RPLCD → LCD display control

openpyxl → Excel file handling

Adafruit_IO → Cloud integration

Cloud Platform: Adafruit IO

Data Storage: Excel workbook (medicine.xlsx)

## ⚙️ Workflow

1. Authorized staff enters a password via keypad.
2. Student’s barcode ID is scanned.
3. Required medicines are dispensed via push buttons.
4. DC motors release the selected medicines.
5. Transaction details are saved in Excel.
6. Data is uploaded to Adafruit IO for real-time monitoring.
7. LCD provides feedback and status updates.

## 📊 Sample Excel Log
| S.No | Date & Time      | Student ID | a | s | d | f |
| ---- | ---------------- | ---------- | - | - | - | - |
| 1    | 2025-09-15 18:30 | 4NM21CS001 | 1 | 0 | 2 | 0 |


(a, s, d, f = medicine types dispensed)


## 🎥 Project Demo

We have prepared a complete hardware demonstration:
👉 Demo Video https://drive.google.com/file/d/1sWW4HSKs-a3PoucK_5NsvUZpjuOdx904/view?usp=sharing

## 📖 Research Paper

This project has been presented as a paper titled:

**“A Secure IoT-Based Medicine Management System for Educational Institutes”**

at the **7th International Conference on Communication and Computational Technologies (ICCCT 2025)**, organized in Hybrid Mode by:

National Forensic Sciences University, Goa Campus, India

Florida International University, Miami, FL, USA

📌 The paper is yet to be published in the conference proceedings.

## 👥 Authors

Deeksha K N

Aditya Raosab Magadum

Sneha R

Lohith J J

Ajay Kumar Dwivedi

## 🚀 Future Enhancements

1. Web-based monitoring dashboard
2. Biometric or Face Recognition authentication
3. SMS/Email alerts for guardians or doctors
