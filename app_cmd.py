import tkinter as tk
from tkinter import filedialog
import subprocess
import os
import sys

number_of_files = 0
number_of_files_read = 0 
print("Welcome to .word to .odt ultralight app")
task_finished=False
resolue_1=False
def convertir_un_fichier(a):
    global task_finished
    global number_of_files
    global number_of_files_read
    root = tk.Tk()
    root.withdraw()

    dossier = filedialog.askdirectory(
        title="choose a file"
    )
    root = tk.Tk()
    root.withdraw()
    dossier_sortie = filedialog.askdirectory(
        title="choose exit file"
    )
    if dossier:
        os.makedirs(dossier_sortie, exist_ok=True)
        if a == 1:

            fichiers = [
                f for f in os.listdir(dossier)
                if f.lower().endswith(".docx")
            ]

        elif a == 2:
            fichiers = [
                f for f in os.listdir(dossier)
                if f.lower().endswith(".odt")
            ]
        elif a == 3:
            fichiers = [
                f for f in os.listdir(dossier)
                if f.lower().endswith(".xlsx")
            ]
        elif a == 4:
            fichiers = [
                f for f in os.listdir(dossier)
                if f.lower().endswith(".ods")
            ]
        elif a == 5:
            fichiers = [
                f for f in os.listdir(dossier)
                if f.lower().endswith(".pptx")
            ]
        elif a == 6:
            fichiers = [
                f for f in os.listdir(dossier)
                if f.lower().endswith(".odp")
            ]
        print(f"{len(fichiers)} fichiers trouvés.")
        number_of_files = len(fichiers)
        for fichier in fichiers:
            chemin = os.path.join(dossier, fichier)

            print(f"Conversion of : {fichier}")
            if a == 1:

                subprocess.run([
                    r"C:\Program Files\LibreOffice\program\soffice.exe",
                    "--headless",
                    "--convert-to", "odt",
                    "--outdir", dossier_sortie,
                    chemin
                ])
            elif a == 2:
                subprocess.run([
                    r"C:\Program Files\LibreOffice\program\soffice.exe",
                    "--headless",
                    "--convert-to", "docx",
                    "--outdir", dossier_sortie,
                    chemin
                ])
            elif a == 3:
                subprocess.run([
                    r"C:\Program Files\LibreOffice\program\soffice.exe",
                    "--headless",
                    "--convert-to", "ods",
                    "--outdir", dossier_sortie,
                    chemin
                ])
            elif a == 4:
                subprocess.run([
                    r"C:\Program Files\LibreOffice\program\soffice.exe",
                    "--headless",
                    "--convert-to", "xlsx",
                    "--outdir", dossier_sortie,
                    chemin
                ])
            elif a == 5:
                subprocess.run([
                    r"C:\Program Files\LibreOffice\program\soffice.exe",
                    "--headless",
                    "--convert-to", "odp",
                    "--outdir", dossier_sortie,
                    chemin
                ])
            elif a == 6:
                subprocess.run([
                    r"C:\Program Files\LibreOffice\program\soffice.exe",
                    "--headless",
                    "--convert-to", "pptx",
                    "--outdir", dossier_sortie,
                    chemin
                ])
            number_of_files_read+=1
            print(f"{number_of_files_read}/{number_of_files}")
        print("Conversion terminée.")
        task_finished = True
while True:
    print("tap 1 to start a text file conversion process (.docx to .odt)")
    print("tap 2 to start a text file conversion process (.odt to .docx)")
    print("tap 3 to start a tableur file conversion process (.xlsx to .ods)")
    print("tap 4 to start a tableur file conversion process (.ods to .xlsx)")
    print("tap 5 to start a presentation file conversion process (.pptx to .odp)")
    print("tap 6 to start a presentation file conversion process (.odp to .pptx)")
    print("tap 7 to exit program")

    input_value = input(">")

    if input_value == "1":
        number_of_files_read=0
        convertir_un_fichier(1)

    elif input_value == "2":
        number_of_files_read=0
        convertir_un_fichier(2)
    elif input_value == "3":
        number_of_files_read=0
        convertir_un_fichier(3)
    elif input_value == "4":
        number_of_files_read=0
        convertir_un_fichier(4)
    elif input_value == "5":
        number_of_files_read=0
        convertir_un_fichier(5)
    elif input_value == "6":
        number_of_files_read=0
        convertir_un_fichier(6)
    elif input_value == "7":
        sys.exit()
    
    
