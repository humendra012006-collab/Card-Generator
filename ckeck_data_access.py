import pandas as pd

students = pd.read_excel(r"C:\Users\humen\OneDrive\Desktop\Coding\ID Card Generator\Card data\Gurukul Institute.xlsx")

for _, student in students.iterrows():
    print(f"{student["Name"]} -- {student["Father"]} -- {student["Roll"]}")
