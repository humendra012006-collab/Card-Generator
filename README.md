# 🪪 ID Card Generator

A Python-based application that automatically generates student ID cards from an Excel spreadsheet. The program reads student information, places it onto an ID card template, inserts the student's photo, and saves the completed ID card as an image.

---

## ✨ Features

- Generate ID cards in bulk from an Excel file.
- Automatically inserts:
  - Student Name
  - Father's Name
  - Contact Number
  - Address
- Adds student photo based on Roll Number.
- Automatically resizes and crops photos to fit the template.
- Uses a default placeholder image if a student's photo is missing.
- Saves each generated ID card as a PNG image.

---

## 📂 Project Structure

```
ID Card Generator/
│
├── Card data/
│   └── Gurukul Institute.xlsx
│
├── Card template/
│   └── ID_Card02.png
│
├── Photos/
│   ├── 101.jpg
│   ├── 102.png
│   ├── 103.jpeg
│   └── Person.png          # Default image
│
├── Final_cards/
│
└── main.py
```

---

## 📋 Requirements

- Python 3.8+
- pandas
- Pillow
- openpyxl

Install the required libraries:

```bash
pip install pandas pillow openpyxl
```

---

## 📊 Excel File Format

The Excel file should contain the following columns:

| Column | Description |
|----------|-------------|
| Roll | Student Roll Number |
| Name | Student Name |
| Father | Father's Name |
| Contact | Contact Number |
| Address | Student Address |

Example:

| Roll | Name | Father | Contact | Address |
|------|------|---------|----------|----------|
| 101 | John Doe | Robert Doe | 9876543210 | New York |
| 102 | Jane Smith | David Smith | 9876543211 | California |

---

## 🖼️ Student Photos

Place all student photos inside the **Photos** folder.

The filename **must match the student's Roll Number**.

Example:

```
101.jpg
102.png
103.jpeg
```

Supported image formats:

- `.jpg`
- `.jpeg`
- `.png`

If no matching photo is found, the program automatically uses **Person.png** as the default image.

---

## 🚀 How It Works

1. Reads student information from the Excel file.
2. Opens the ID card template.
3. Writes student details onto the template.
4. Searches for the student's photo.
5. Resizes and crops the photo to fit the ID card.
6. Pastes the photo onto the template.
7. Saves the completed ID card in the **Final_cards** folder.

---

## ▶️ Usage

1. Update the file paths in `main.py` according to your system.
2. Place the Excel file in the **Card data** folder.
3. Place the ID card template in the **Card template** folder.
4. Add student photos to the **Photos** folder.
5. Run the script:

```bash
python main.py
```

When all cards have been generated, the terminal will display:

```
COMPLETED
```

---

## 📦 Output

Each generated ID card is saved as:

```
Final_cards/
│
├── 101.png
├── 102.png
├── 103.png
└── ...
```

---

## ⚙️ Technologies Used

- Python
- Pandas
- Pillow (PIL)
- OpenPyXL

---

## 🔮 Future Improvements

- Add a graphical user interface (GUI).
- Allow users to select files through a file picker.
- Support PDF output.
- Add QR code generation.
- Improve text wrapping and font customization.
- Support multiple ID card templates.
- Add logo and barcode support.

---

## 📄 License

This project is open source and available under the MIT License.

---

## 👤 Author

Developed using Python to simplify bulk ID card generation from Excel data.
