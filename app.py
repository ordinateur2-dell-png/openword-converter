import tkinter as tk
from tkinter import filedialog
import subprocess
import os
import time
import pygame 
import sys
import threading 
pygame.init()

a= 0
font = pygame.font.Font(None, 48)
info_screen = pygame.display.Info()
screen_width, screen_height = info_screen.current_w, info_screen.current_h
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption(".docx to .odt lite")
number_of_files = 0
number_of_files_read = 0 
def convertir_un_fichier():
    global a 
    global number_of_files
    global number_of_files_read
    a=1
    root = tk.Tk()
    root.withdraw()

    dossier = filedialog.askdirectory(
        title="Choisir un dossier"
    )
    root = tk.Tk()
    root.withdraw()
    dossier_sortie = filedialog.askdirectory(
        title="Choisir un dossier de sortie"
    )
    a= 2
    if dossier:
        os.makedirs(dossier_sortie, exist_ok=True)

        fichiers = [
            f for f in os.listdir(dossier)
            if f.lower().endswith(".docx")
        ]

        print(f"{len(fichiers)} fichiers trouvés.")
        number_of_files = len(fichiers)
        a= 3
        for fichier in fichiers:
            chemin = os.path.join(dossier, fichier)

            print(f"Conversion de : {fichier}")

            subprocess.run([
                r"C:\Program Files\LibreOffice\program\soffice.exe",
                "--headless",
                "--convert-to", "odt",
                "--outdir", dossier_sortie,
                chemin
            ])
            number_of_files_read+=1
            time.sleep(1)
        a=4
        print("Conversion terminée.")
clock = pygame.time.Clock()
surface_texte = font.render("choisissez votre dossier", True,((0,0,0)))
threading.Thread(target=convertir_un_fichier, daemon=True).start()
while True:
    rect = surface_texte.get_rect(center=screen.get_rect().center)
    screen.fill((255,255,255))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    if a == 1:
        surface_texte = font.render("choisissez votre dossier", True,((0,0,0)))
    if a == 2:
        surface_texte = font.render("comptage des documents", True,((0,0,0)))
    if a == 3:
        surface_texte = font.render("conversion des documents", True,((0,0,0)))
        surface_texte1 = font.render(f"{number_of_files_read}/{number_of_files}", True,((0,0,0)))
        rect1 = surface_texte1.get_rect(center=(screen.get_rect().centerx, screen_height//2+75))
        screen.blit(surface_texte1, rect1)
    if a == 4:
        surface_texte = font.render("terminé", True,((0,0,0)))
        rect = surface_texte.get_rect(center=screen.get_rect().center)
        screen.blit(surface_texte, rect)
        pygame.display.flip()
        time.sleep(1)
        pygame.quit()
        sys.exit()
    screen.blit(surface_texte, rect)

    pygame.display.flip()
    clock.tick(60)