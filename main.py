################################################################################################
import sys
import sqlite3
import re
import threading
from functools import partial
import bcrypt
import logging
from scapy.all  import *
from scapy.all import IP, ICMP
import time  
################################################################################################

from src.ui_login import *
################################################################################################
from PySide6.QtWidgets import QApplication, QInputDialog, QWidget, QFileDialog
import csv
import platform
import subprocess
import os
################################################################################################

from Custom_Widgets import *

from Custom_Widgets.QAppSettings import QAppSettings

from PySide6.QtWidgets import QMessageBox
from PySide6.QtWidgets import QPushButton, QHBoxLayout, QWidget
from PySide6.QtWidgets import QMenu
################################################################################################



################################################################################################
## main window class 
################################################################################################


#DATA BASE Configuration 
def create_user_table():
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL,
            role TEXT NOT NULL DEFAULT 'blue_team'  -- Ajout d'une colonne pour le rôle
        )
    """)
    conn.commit()
    conn.close()
  
def hash_password(password):
    """Hacher le mot de passe avec bcrypt."""
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password.encode(), salt)
    return hashed_password

def verify_password(hashed_password, input_password):
    """Vérifier si le mot de passe saisi correspond au mot de passe haché."""
    return bcrypt.checkpw(input_password.encode(), hashed_password)



class MainWindow(QMainWindow):
  packet_filtered = Signal(str)  
  def __init__(self):
    QMainWindow.__init__(self)
    self.ui = Ui_MainWindow() #appel lohin.py
    self.ui.setupUi(self) 

    # Initialisation de la base de données
    create_user_table()
    # Initialisation des variables pour la détection d'attaques
    self.suspected_ips = set()  # Initialisation de la variable suspected_ips
    self.MAX_PING_SIZE = 1024  # Définir une taille maximale pour les paquets ICMP

    ################################################################################################
    # apply json stylesheet
    ################################################################################################
    loadJsonStyle(self, self.ui, jsonFiles = { "json-style/login_style.json"})

    ################################################################################################
    
    #apply theme style, generate icons ...
    QAppSettings.updateAppSettings(self)

    ################################################################################################
    self.show()
    
    #navigation button 
    self.ui.siginBtn.clicked.connect(self.handle_login)
    self.ui.signupBtn.clicked.connect(self.handle_signup)
    self.ui.restbtn.clicked.connect(self.reset_password)
    #nav bar
    self.ui.to_packet.clicked.connect(partial(self.navigate_to_page_bar, "packet"))
    self.ui.to_packet_2.clicked.connect(partial(self.navigate_to_page_bar, "packet"))
    self.ui.to_menace.clicked.connect(partial(self.navigate_to_page_bar, "menace"))
    self.ui.to_menace_2.clicked.connect(partial(self.navigate_to_page_bar, "menace"))
    self.ui.to_alert.clicked.connect(partial(self.navigate_to_page_bar, "alert"))
    self.ui.to_alert_2.clicked.connect(partial(self.navigate_to_page_bar, "alert"))
    self.ui.to_profil.clicked.connect(partial(self.navigate_to_page_bar, "profil"))
    self.ui.to_profil_2.clicked.connect(partial(self.navigate_to_page_bar, "profil"))
    self.ui.to_visual.clicked.connect(partial(self.navigate_to_page_bar, "visual"))
    self.ui.to_visual_2.clicked.connect(partial(self.navigate_to_page_bar, "visual"))
    
    #sniffingg buttons
    self.ui.to_capture.clicked.connect(partial(self.nav_packet_page,"capture"))
    self.ui.to_filtrer.clicked.connect(partial(self.nav_packet_page, "filtrer"))
    self.captured_packets = []
    self.sniffing = False
    
    self.ui.start.clicked.connect(self.start_sniffing)
    self.ui.stop.clicked.connect(self.stop_sniffing)
    self.ui.clear_sniffing.clicked.connect(self.clear_sniffing_data)
    self.ui.save_file.clicked.connect(self.save_packets)
    
    #flitre button 
    # Bouton pour appliquer les filtres
    self.ui.start_filter.clicked.connect(self.filter_packets)
    # Bouton pour effacer les filtres
    self.ui.clear_filter_button.clicked.connect(self.clear_filters)
    #self.ui.save_file.clicked.connect()
    #profil buttons
    self.ui.editbtn.clicked.connect(partial(self.nav_profil_page,"edit_form"))
    self.ui.deletbtn.clicked.connect(partial(self.nav_profil_page,"delate"))
    self.ui.logout.clicked.connect(self.logout)
    self.ui.logout_2.clicked.connect(self.logout)

    self.ui.menace_table.setContextMenuPolicy(Qt.CustomContextMenu)
    self.ui.menace_table.customContextMenuRequested.connect(self.show_context_menu)
    
    
    #menace button 
    self.ui.black_list.clicked.connect(partial(self.nav_menace_page,"black"))
    self.ui.white_list.clicked.connect(partial(self.nav_menace_page,"white"))
    self.ui.dns_list.clicked.connect(partial(self.nav_menace_page,"dns"))  
  #Function to display notification
  def showNotif(self, msg):
    self.ui.notificationTxt.setText(msg)
    self.ui.notificationSlide.expandMenu()
      
  # function to switch theme 
  def changeTheme(self):
    #######################################################################
    # CHECK THE CURRENT THEME SETTINGS
    #######################################################################
    settings = QSettings()
    # CURRENT ICONS 
    # CURRENT THEME NAME
    print("Current theme", settings.value("THEME"))
    print("Current Icons color", settings.value("ICONS-COLOR"))
    
    if settings.value("THEME") == "Modern Teal Slate":
      # CHANGE THE THEME NAME IN SETTINGS
      # Use one of the app themes from your JSON file
      settings.setValue("THEME", "Midnight Teal Slate")
      style="#stackedWiget *{color: $COLOR_BACKGROUND_1; background-color: transparent;}"
    else:
      settings.setValue("THEME", "Modern Teal Slate")
      
      # RE APPLY THE NEW SETINGS
      # CompileStyleSheet might also work
      # CompileStyleSheet.applyCompiledSass(self)
      QAppSettings.updateAppSettings(self)
      
      self.ui.stackedWidget.setStyleSheet(style)
      self.ui.frame_4.setStyleSheet(style)
      self.ui.frame_8.setStyleSheet(style)
    
     
  #login function 
  def handle_login(self):
    username = self.ui.usernameInput.text().strip()
    password = self.ui.passwordInput.text().strip()

    # Validation de base
    if not username or not password:
        self.show_message("Error", "Username and password cannot be empty.")
        return

    try:
        conn = sqlite3.connect("users.db")
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users WHERE username = ?", (username,))
        user = cursor.fetchone()
        conn.close()

        # Vérification des résultats
        if user:
            stored_password = user[2]  # Le mot de passe haché est stocké dans la 3ème colonne
            if verify_password(stored_password, password):
                if user[3] == "blue_team":  # Vérifier le rôle de l'utilisateur
                    self.show_message("Success", f"Welcome, {username}!")
                    self.navigate_to_acceuil()  # Naviguer vers la page d'accueil

                    # Journalisation de la tentative de connexion réussie
                    logging.info(f"Successful login attempt for user: {username}")
                else:
                    self.show_message("Error", "You are not authorized to access this system.")
                    # Journalisation de la tentative de connexion échouée (rôle incorrect)
                    logging.warning(f"Failed login attempt for user {username}: Incorrect role.")
            else:
                self.show_message("Error", "Invalid username or password.")
                # Journalisation de la tentative de connexion échouée (mot de passe incorrect)
                logging.warning(f"Failed login attempt for user {username}: Incorrect password.")
        else:
            self.show_message("Error", "Invalid username or password.")
            # Journalisation de la tentative de connexion échouée (utilisateur non trouvé)
            logging.warning(f"Failed login attempt for user {username}: User not found.")
    except sqlite3.Error as e:
        self.show_message("Error", f"Database error: {str(e)}")
        # Journalisation de l'erreur de base de données
        logging.error(f"Database error during login attempt for user {username}: {str(e)}")

  #SignUp Function 
  def handle_signup(self):
    username = self.ui.usernameInput_2.text().strip()
    password = self.ui.passwordInput_2.text().strip()
    confirmPassword = self.ui.confirmInput.text().strip()

    # Validation de base
    if not username or not password:
        self.show_message("Error", "Username and password cannot be empty.")
        return

    # Vérification des mots de passe cohérents
    if confirmPassword != password:
        self.show_message("Error", "Passwords do not match!")
        return

    # Validation de la force du mot de passe
    if len(password) < 8 or not re.search(r"[A-Z]", password) or not re.search(r"\d", password):
        self.show_message("Error", "Password must be at least 8 characters long, contain one uppercase letter and one digit.")
        return

    # Inscription
    try:
        hashed_password = hash_password(password)
        conn = sqlite3.connect("users.db")
        cursor = conn.cursor()
        cursor.execute("INSERT INTO users (username, password, role) VALUES (?, ?, ?)", (username, hashed_password, "blue_team"))
        conn.commit()
        conn.close()
        self.show_message("Success", "Signup successful! You can now log in.")
    except sqlite3.IntegrityError:
        self.show_message("Error", "Username already exists.")
    except Exception as e:
        self.show_message("Error", f"An error occurred: {str(e)}")
  
  def show_message(self, title, message):
    QMessageBox.information(self, title, message)
 
 
 
 
 ################################################################################################### NAVIGATION  beetwen page ####################################################################################################
 
  def navigate_to_acceuil(self):
      """Naviguer vers la page d'accueil."""
      try:
          # Récupérer le QdgetStackedWi
          self.globale_screen = self.ui.globale_screen  # Utilisez le bon nom ici

          # Vérifier si le widget existe
          if not self.globale_screen:
              print("Erreur : Le QStackedWidget 'globale_screen' est introuvable.")
              return

          # Récupérer la page d'accueil
          self.acceuil_page = self.findChild(QWidget, "acceuil")  # Nom de la page dans Qt Designer
          if not self.acceuil_page:
              print("Erreur : La page 'acceuil' est introuvable.")
              return

          # Naviguer vers la page d'accueil
          self.globale_screen.setCurrentWidget(self.acceuil_page)
          print("Navigation vers la page d'accueil réussie.")
      except Exception as e:
          print(f"Une erreur est survenue : {e}")

    # Méthode navigate_to_page corrigée
  def navigate_to_page_bar(self, page_name: str):
    """
    Naviguer vers une page spécifique à l'intérieur du QStackedWidget imbriqué.
    :param page_name: Nom de l'objet QWidget correspondant à la page dans Qt Designer.
    """
    print(f"Appel de navigate_to_page avec page_name = {page_name}")  # Message de déboga
    try:
        # Accéder au QStackedWidget principal (globale_screen)
        globale_screen = self.ui.globale_screen
        if not globale_screen:
            print("Erreur : Le QStackedWidget 'globale_screen' est introuvable.")
            return

        # Accéder à la page d'accueil (acceuil)
        acceuil_page = globale_screen.findChild(QWidget, "acceuil")
        if not acceuil_page:
            print("Erreur : La page 'acceuil' est introuvable.")
            return

        # Accéder au QFrame "screen" de la page "acceuil"
        screen_frame = acceuil_page.findChild(QFrame, "screen")
        if not screen_frame:
            print("Erreur : Le QFrame 'screen' est introuvable.")
            return

        # Accéder au QWidget "main_screen" de la page "acceuil"
        main_screen = screen_frame.findChild(QWidget, "main_screen")
        if not main_screen:
            print("Erreur : Le QWidget 'main_screen' est introuvable.")
            return

        # Accéder au QStackedWidget des pages ("pages_screen")
        pages_screen = main_screen.findChild(QStackedWidget, "pages_screen")
        if not pages_screen:
            print("Erreur : Le QStackedWidget 'pages_screen' est introuvable.")
            return

        # Récupérer la page cible
        target_page = pages_screen.findChild(QWidget, page_name)
        if not target_page:
            print(f"Erreur : La page '{page_name}' est introuvable dans 'pages_screen'.")
            return

        # Naviguer vers la page cible
        pages_screen.setCurrentWidget(target_page)
        print(f"Navigation vers la page '{page_name}' réussie.")
    except Exception as e:
        print(f"Une erreur est survenue lors de la navigation : {e}")
  def nav_packet_page(self, page_name: str):
    """
    Naviguer vers une page spécifique à l'intérieur du QStackedWidget imbriqué "packets".
    :param page_name: Nom de l'objet QWidget correspondant à la page dans Qt Designer.
    """
    print(f"Appel de nav_packet_page avec page_name = {page_name}")  # Message de débogage
    try:
        # Accéder au QStackedWidget principal (globale_screen)
        globale_screen = self.ui.globale_screen
        if not globale_screen:
            print("Erreur : Le QStackedWidget 'globale_screen' est introuvable.")
            return

        # Accéder à la page d'accueil (acceuil)
        acceuil_page = globale_screen.findChild(QWidget, "acceuil")
        if not acceuil_page:
            print("Erreur : La page 'acceuil' est introuvable.")
            return

        # Accéder au QFrame "screen" de la page "acceuil"
        screen_frame = acceuil_page.findChild(QFrame, "screen")
        if not screen_frame:
            print("Erreur : Le QFrame 'screen' est introuvable.")
            return

        # Accéder au QWidget "main_screen" de la page "acceuil"
        main_screen = screen_frame.findChild(QWidget, "main_screen")
        if not main_screen:
            print("Erreur : Le QWidget 'main_screen' est introuvable.")
            return

        # Accéder au QStackedWidget des pages ("pages_screen")
        pages_screen = main_screen.findChild(QStackedWidget, "pages_screen")
        if not pages_screen:
            print("Erreur : Le QStackedWidget 'pages_screen' est introuvable.")
            return

        # Accéder à la page "packet"
        packet = pages_screen.findChild(QWidget, "packet")
        if not packet:
            print("Erreur : Le QWidget 'packet' est introuvable.")
            return

        # Accéder au QWidget "frame_16" de la page "packet"
        frame_16 = packet.findChild(QWidget, "frame_16")
        if not frame_16:
            print("Erreur : Le QWidget 'frame_16' est introuvable.")
            return

        # Accéder au QStackedWidget des pages ("packets")
        packets = frame_16.findChild(QStackedWidget, "packets")
        if not packets:
            print("Erreur : Le QStackedWidget 'packets' est introuvable.")
            return

        # Récupérer la page cible
        target_page = packets.findChild(QWidget, page_name)  # Utilise packets ici
        if not target_page:
            print(f"Erreur : La page '{page_name}' est introuvable dans 'packets'.")
            return

        # Naviguer vers la page cible
        packets.setCurrentWidget(target_page)  # Utilise packets ici
        print(f"Navigation vers la page '{page_name}' réussie.")
    except Exception as e:
        print(f"Une erreur est survenue lors de la navigation : {e}")
  def nav_menace_page(self, page_name: str):
    """
    Naviguer vers une page spécifique à l'intérieur du QStackedWidget imbriqué "packets".
    :param page_name: Nom de l'objet QWidget correspondant à la page dans Qt Designer.
    """
    print(f"Appel de nav_packet_page avec page_name = {page_name}")  # Message de débogage
    try:
        # Accéder au QStackedWidget principal (globale_screen)
        globale_screen = self.ui.globale_screen
        if not globale_screen:
            print("Erreur : Le QStackedWidget 'globale_screen' est introuvable.")
            return

        # Accéder à la page d'accueil (acceuil)
        acceuil_page = globale_screen.findChild(QWidget, "acceuil")
        if not acceuil_page:
            print("Erreur : La page 'acceuil' est introuvable.")
            return

        # Accéder au QFrame "screen" de la page "acceuil"
        screen_frame = acceuil_page.findChild(QFrame, "screen")
        if not screen_frame:
            print("Erreur : Le QFrame 'screen' est introuvable.")
            return

        # Accéder au QWidget "main_screen" de la page "acceuil"
        main_screen = screen_frame.findChild(QWidget, "main_screen")
        if not main_screen:
            print("Erreur : Le QWidget 'main_screen' est introuvable.")
            return

        # Accéder au QStackedWidget des pages ("pages_screen")
        pages_screen = main_screen.findChild(QStackedWidget, "pages_screen")
        if not pages_screen:
            print("Erreur : Le QStackedWidget 'pages_screen' est introuvable.")
            return

        # Accéder à la page "packet"
        visual = pages_screen.findChild(QWidget, "visual")
        if not visual:
            print("Erreur : Le QWidget 'visual' est introuvable.")
            return

        # Accéder au QWidget "frame_16" de la page "packet"
        frame_32 = visual.findChild(QWidget, "frame_32")
        if not frame_32:
            print("Erreur : Le QWidget 'frame_32' est introuvable.")
            return

        # Accéder au QStackedWidget des pages ("packets")
        listes = frame_32.findChild(QStackedWidget, "listes")
        if not listes:
            print("Erreur : Le QStackedWidget 'listes' est introuvable.")
            return

        # Récupérer la page cible
        target_page = listes.findChild(QWidget, page_name)  # Utilise packets ici
        if not target_page:
            print(f"Erreur : La page '{page_name}' est introuvable dans 'packets'.")
            return

        # Naviguer vers la page cible
        listes.setCurrentWidget(target_page)  # Utilise packets ici
        print(f"Navigation vers la page '{page_name}' réussie.")
    except Exception as e:
        print(f"Une erreur est survenue lors de la navigation : {e}") 
  def nav_profil_page(self, page_name: str):
    """
    Naviguer vers une page spécifique à l'intérieur du QStackedWidget imbriqué "packets".
    :param page_name: Nom de l'objet QWidget correspondant à la page dans Qt Designer.
    """
    print(f"Appel de nav_packet_page avec page_name = {page_name}")  # Message de débogage
    try:
        # Accéder au QStackedWidget principal (globale_screen)
        globale_screen = self.ui.globale_screen
        if not globale_screen:
            print("Erreur : Le QStackedWidget 'globale_screen' est introuvable.")
            return

        # Accéder à la page d'accueil (acceuil)
        acceuil_page = globale_screen.findChild(QWidget, "acceuil")
        if not acceuil_page:
            print("Erreur : La page 'acceuil' est introuvable.")
            return

        # Accéder au QFrame "screen" de la page "acceuil"
        screen_frame = acceuil_page.findChild(QFrame, "screen")
        if not screen_frame:
            print("Erreur : Le QFrame 'screen' est introuvable.")
            return

        # Accéder au QWidget "main_screen" de la page "acceuil"
        main_screen = screen_frame.findChild(QWidget, "main_screen")
        if not main_screen:
            print("Erreur : Le QWidget 'main_screen' est introuvable.")
            return

        # Accéder au QStackedWidget des pages ("pages_screen")
        pages_screen = main_screen.findChild(QStackedWidget, "pages_screen")
        if not pages_screen:
            print("Erreur : Le QStackedWidget 'pages_screen' est introuvable.")
            return

        # Accéder à la page "packet"
        profil = pages_screen.findChild(QWidget, "profil")
        if not profil:
            print("Erreur : Le QWidget 'packet' est introuvable.")
            return

        # Accéder au QWidget "frame_23" de la page "packet"
        frame_23 = profil.findChild(QWidget, "frame_23")
        if not frame_23:
            print("Erreur : Le QWidget 'frame_16' est introuvable.")
            return

        # Accéder au QStackedWidget des pages ("packets")
        profil_edit = frame_23.findChild(QStackedWidget, "profil_edit")
        if not profil_edit:
            print("Erreur : Le QStackedWidget 'profil_edit' est introuvable.")
            return

        # Récupérer la page cible
        target_page = profil_edit.findChild(QWidget, page_name)  # Utilise packets ici
        if not target_page:
            print(f"Erreur : La page '{page_name}' est introuvable dans 'packets'.")
            return

        # Naviguer vers la page cible
        profil_edit.setCurrentWidget(target_page)  #
        print(f"Navigation vers la page '{page_name}' réussie.")

    except Exception as e:
        print(f"Une erreur est survenue lors de la navigation : {e}")        
  
  def reset_password(self):
    username = self.ui.usernameInput_3.text().strip()
    new_password = self.ui.passwordInput_3.text().strip()
    confirm_password = self.ui.confirmInput_2.text().strip()

    if not username or not new_password or not confirm_password:
        self.show_message("Error", "All fields are required.")
        return
    
        # Validation de la force du mot de passe
    if len(new_password) < 8 or not re.search(r"[A-Z]", new_password) or not re.search(r"\d", new_password):
        self.show_message("Error", "Password must be at least 8 characters long, contain one uppercase letter and one digit.")
        return
    if new_password != confirm_password:
        self.show_message("Error", "Passwords do not match.")
        return

    try:
        conn = sqlite3.connect("users.db")
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users WHERE username = ?", (username,))
        user = cursor.fetchone()

        if user:
            hashed_password = hash_password(new_password)
            cursor.execute("UPDATE users SET password = ? WHERE username = ?", (hashed_password, username))
            conn.commit()
            conn.close()
            self.show_message("Success", "Password reset successful! You can now log in.")
            # Rediriger vers la page de connexion
            self.navigate_to_login_pg()
        else:
            self.show_message("Error", "Username not found.")
    except Exception as e:
        self.show_message("Error", f"An error occurred: {str(e)}")
  def logout(self):
    """
    Déconnecte l'utilisateur et redirige vers la page de connexion.
    """
    # Réinitialiser l'état de l'application (si nécessaire)
    # Par exemple, effacer les informations de l'utilisateur connecté
    self.current_user = None  # Si tu stockes l'utilisateur connecté dans une variable

    # Rediriger vers la page de connexion
    self.navigate_to_login()

    # Afficher un message de confirmation
    self.show_message("Success", "You have been logged out successfully.")
  def navigate_to_login_pg(self):
    """
    Naviguer vers la page de connexion (login_pg).
    """
    try:
        # Accéder au QStackedWidget principal (globale_screen)
        globale_screen = self.ui.globale_screen
        if not globale_screen:
            print("Erreur : Le QStackedWidget 'globale_screen' est introuvable.")
            return

        # Récupérer la page de connexion (login)
        login_page = globale_screen.findChild(QWidget, "login")  # Assurez-vous que le nom est correct
        if not login_page:
            print("Erreur : La page 'login' est introuvable.")
            return

        # Récupérer le main_body dans la page de connexion
        main_body = login_page.findChild(QWidget, "main_body")
        if not main_body:
            print("Erreur : Le widget 'main_body' est introuvable.")
            return

        # Récupérer le form_stack dans le main_body
        form_stack = main_body.findChild(QStackedWidget, "form_stack")
        if not form_stack:
            print("Erreur : Le QStackedWidget 'form_stack' est introuvable.")
            return

        # Récupérer la page de connexion (login_pg) dans le form_stack
        login_pg = form_stack.findChild(QWidget, "login_pg")
        if not login_pg:
            print("Erreur : La page 'login_pg' est introuvable.")
            return

        # Naviguer vers la page de connexion (login_pg)
        form_stack.setCurrentWidget(login_pg)  # Utiliser form_stack pour naviguer
        print("Navigation vers la page de connexion réussie.")
    except Exception as e:
        print(f"Une erreur est survenue lors de la navigation : {e}")
 
  def navigate_to_login(self):
    """
    Naviguer vers la page de connexion.
    """
    try:
        # Accéder au QStackedWidget principal (globale_screen)
        globale_screen = self.ui.globale_screen
        if not globale_screen:
            print("Erreur : Le QStackedWidget 'globale_screen' est introuvable.")
            return

        # Récupérer la page de connexion
        login_page = globale_screen.findChild(QWidget, "login")  # Remplace "login" par le nom réel de ta page de connexion
        if not login_page:
            print("Erreur : La page 'login' est introuvable.")
            return

        # Naviguer vers la page de connexion
        globale_screen.setCurrentWidget(login_page)
        print("Navigation vers la page de connexion réussie.")
    except Exception as e:
        print(f"Une erreur est survenue lors de la navigation : {e}")
  
  ############################################################################### SNIFFING #########################################################################################
  def start_sniffing(self):
        """Démarrer le sniffing des paquets"""
        self.sniffing = True
        self.ui.start.setDisabled(True)  # Désactiver le bouton Start Sniffing une fois cliqué
        self.ui.stop.setEnabled(True)  # Activer le bouton Stop Sniffing
        self.sniff_thread = threading.Thread(target=self.sniff_packets)
        self.sniff_thread.start()

  def sniff_packets(self):
        """Capturer les paquets et les ajouter dans le tableau"""
        def packet_callback(packet):
            if not self.sniffing:
                return  # Arrêter le sniffing si self.sniffing est False
            self.Ajout_menace(packet)
            self.process_packet_auto_block(packet)
            self.captured_packets.append(packet)
            self.display_packet(packet)

        # Démarrer le sniffing
        sniff(prn=packet_callback, store=False)

  def stop_sniffing(self):
        """Arrêter le sniffing des paquets"""
        self.sniffing = False
        self.ui.start.setEnabled(True)  # Réactiver le bouton Start Sniffing
        self.ui.stop.setDisabled(True)  # Désactiver le bouton Stop Sniffing

  def display_packet(self, packet):
        """Affichage d'un paquet dans le tableau"""
        row_position = self.ui.tableWidget.rowCount()
        self.ui.tableWidget.insertRow(row_position)

        # Timestamp, MAC, IP, Length (affichage générique)
        timestamp = packet.time
        source_mac = packet.src if Ether in packet else ""
        dest_mac = packet.dst if Ether in packet else ""
        source_ip = packet[IP].src if IP in packet else ""
        dest_ip = packet[IP].dst if IP in packet else ""
        protocol = packet.proto if IP in packet else ""
        length = len(packet)

        # Déterminer le type du paquet et les ports si présents
        packet_type = ""
        source_port = ""
        dest_port = ""

        # Vérifier les protocoles dans l'ordre
        if TCP in packet:
            packet_type = "TCP"
            source_port = packet[TCP].sport
            dest_port = packet[TCP].dport
        elif UDP in packet:
            packet_type = "UDP"
            source_port = packet[UDP].sport
            dest_port = packet[UDP].dport
        elif ICMP in packet:
            packet_type = "ICMP"
        elif ARP in packet:
            packet_type = "ARP"
        elif DNS in packet:
            packet_type = "DNS"
        elif DHCP in packet:
            packet_type = "DHCP"
        elif IPv6 in packet:
            packet_type = "IPv6"
        elif IP in packet:
            packet_type = "IP"

        # Ajouter les informations dans les cellules du tableau
        self.ui.tableWidget.setItem(row_position, 0, QTableWidgetItem(str(timestamp)))  # Timestamp
        self.ui.tableWidget.setItem(row_position, 1, QTableWidgetItem(source_mac))  # Source MAC
        self.ui.tableWidget.setItem(row_position, 2, QTableWidgetItem(dest_mac))  # Destination MAC
        self.ui.tableWidget.setItem(row_position, 3, QTableWidgetItem(source_ip))  # Source IP
        self.ui.tableWidget.setItem(row_position, 4, QTableWidgetItem(dest_ip))  # Destination IP
        self.ui.tableWidget.setItem(row_position, 5, QTableWidgetItem(str(protocol)))  # Protocol
        self.ui.tableWidget.setItem(row_position, 6, QTableWidgetItem(str(length)))  # Length
        self.ui.tableWidget.setItem(row_position, 7, QTableWidgetItem(str(source_port)))  # Source Port
        self.ui.tableWidget.setItem(row_position, 8, QTableWidgetItem(str(dest_port)))  # Destination Port
        self.ui.tableWidget.setItem(row_position, 9, QTableWidgetItem(packet_type))  # Packet Type

  def clear_sniffing_data(self):
    """Réinitialiser les données de capture de paquets."""
    try:
        # Effacer la liste des paquets capturés
        self.captured_packets.clear()

        # Réinitialiser le tableau d'affichage
        self.ui.tableWidget.setRowCount(0)

        # Afficher un message de confirmation
        self.show_message("Success", "Les données de capture ont été réinitialisées.")
    except Exception as e:
        print(f"Erreur lors de la réinitialisation des données de capture : {e}")
        self.show_message("Error", f"Erreur lors de la réinitialisation des données de capture : {str(e)}")
 
  def save_packets(self):
    """Sauvegarder les paquets capturés au format PCAP ou CSV."""
    if not self.captured_packets:
        self.show_message("Error", "No packets to save!")
        return

    # Demander à l'utilisateur de choisir le format
    format_choice, ok = QInputDialog.getItem(
        self, "Save Packets", "Choose format:", ["PCAP", "CSV"], 0, False
        )
    if not ok:
        return  # L'utilisateur a annulé

    # Demander à l'utilisateur de choisir l'emplacement du fichier
    file_path, _ = QFileDialog.getSaveFileName(
        self, "Save Packets", "", f"{format_choice} Files (*.{format_choice.lower()})"
        )
    if not file_path:
        return  # L'utilisateur a annulé

    try:
        if format_choice == "PCAP":
            self.save_packets_as_pcap(file_path)
        elif format_choice == "CSV":
            self.save_packets_as_csv(file_path)
        self.show_message("Success", f"Packets saved successfully to {file_path}!")
    except Exception as e:
        self.show_message("Error", f"Failed to save packets: {str(e)}")
 
 
  def save_packets_as_pcap(self, file_path):
    """Sauvegarder les paquets au format PCAP."""
    wrpcap(file_path, self.captured_packets)

  def save_packets_as_csv(self, file_path):
    """Sauvegarder les paquets au format CSV."""
    with open(file_path, mode="w", newline="") as csv_file:
        writer = csv.writer(csv_file)
        # En-tête du CSV
        writer.writerow([
            "Timestamp", "Source MAC", "Destination MAC", "Source IP", "Destination IP",
            "Protocol", "Length", "Source Port", "Destination Port", "Packet Type"
            ])
            # Données des paquets
        for packet in self.captured_packets:
            row = self.extract_packet_info(packet)
            writer.writerow(row)
 
  def extract_packet_info(self, packet):
    """Extraire les informations d'un paquet pour le CSV."""
    timestamp = packet.time
    source_mac = packet.src if Ether in packet else ""
    dest_mac = packet.dst if Ether in packet else ""
    source_ip = packet[IP].src if IP in packet else ""
    dest_ip = packet[IP].dst if IP in packet else ""
    protocol = packet.proto if IP in packet else ""
    length = len(packet)
    packet_type = ""
    source_port = ""
    dest_port = ""

    if TCP in packet:
        packet_type = "TCP"
        source_port = packet[TCP].sport
        dest_port = packet[TCP].dport
    elif UDP in packet:
        packet_type = "UDP"
        source_port = packet[UDP].sport
        dest_port = packet[UDP].dport
    elif ICMP in packet:
        packet_type = "ICMP"
    elif ARP in packet:
        packet_type = "ARP"
    elif DNS in packet:
        packet_type = "DNS"
    elif DHCP in packet:
        packet_type = "DHCP"
    elif IPv6 in packet:
        packet_type = "IPv6"
    elif IP in packet:
        packet_type = "IP"

    return [
        timestamp, source_mac, dest_mac, source_ip, dest_ip,
        protocol, length, source_port, dest_port, packet_type
        ]      
 
 ########################################################################## FILTER #############################################################################################################
  
  
  def filter_packets(self):
    """Filtrer les paquets capturés en fonction des critères spécifiés."""
    try:
        # Récupérer les critères de filtrage depuis l'interface
        src_ip = self.ui.ip_src.text().strip()  # Adresse IP source
        dst_ip = self.ui.ip_dest.text().strip()  # Adresse IP de destination
        src_port = self.ui.port_src.text().strip()  # Port source
        dst_port = self.ui.port_dest.text().strip()  # Port destination
        protocol = self.ui.protocol.currentText().strip()  # Protocole (TCP, UDP, etc.)

        # Effacer le tableau avant d'afficher les résultats filtrés
        self.ui.tableWidget_2.setRowCount(0)

        # Parcourir les paquets capturés
        for packet in self.captured_packets:
            # Extraire les informations du paquet
            packet_src_ip = packet[IP].src if IP in packet else ""
            packet_dst_ip = packet[IP].dst if IP in packet else ""
            packet_src_port = ""
            packet_dst_port = ""
            packet_protocol = ""

            if TCP in packet:
                packet_protocol = "TCP"
                packet_src_port = str(packet[TCP].sport)
                packet_dst_port = str(packet[TCP].dport)
            elif UDP in packet:
                packet_protocol = "UDP"
                packet_src_port = str(packet[UDP].sport)
                packet_dst_port = str(packet[UDP].dport)
            elif ICMP in packet:
                packet_protocol = "ICMP"
            elif ARP in packet:
                packet_protocol = "ARP"
            elif DNS in packet:
                packet_protocol = "DNS"
            elif DHCP in packet:
                packet_protocol = "DHCP"
            elif IPv6 in packet:
                packet_protocol = "IPv6"
            elif IP in packet:
                packet_protocol = "IP"

            # Vérifier si le paquet correspond aux critères de filtrage
            matches = True

            # Filtrage par adresse IP
            if src_ip and packet_src_ip != src_ip:
                matches = False
            if dst_ip and packet_dst_ip != dst_ip:
                matches = False

            # Filtrage par port (uniquement pour TCP et UDP)
            if protocol in ["TCP", "UDP"]:
                if src_port and packet_src_port != src_port:
                    matches = False
                if dst_port and packet_dst_port != dst_port:
                    matches = False

            # Filtrage par protocole
            if protocol and packet_protocol != protocol:
                matches = False

            # Afficher le paquet s'il correspond aux critères
            if matches:
                self.display_packet_filter(packet)
    except Exception as e:
        print(f"Erreur lors du filtrage des paquets : {e}")
        self.show_message("Error", f"Erreur lors du filtrage des paquets : {str(e)}")

  def display_packet_filter(self, packet): 
      row_position = self.ui.tableWidget_2.rowCount()
      self.ui.tableWidget_2.insertRow(row_position)

      # Extraire les informations du paquet
      timestamp = packet.time
      source_mac = packet.src if Ether in packet else ""
      dest_mac = packet.dst if Ether in packet else ""
      source_ip = packet[IP].src if IP in packet else ""
      dest_ip = packet[IP].dst if IP in packet else ""
      protocol = packet.proto if IP in packet else ""
      length = len(packet)

      # Déterminer le type du paquet et les ports si présents
      packet_type = ""
      source_port = ""
      dest_port = ""

      if TCP in packet:
          
          packet_type = "TCP"
          source_port = packet[TCP].sport
          dest_port = packet[TCP].dport
      elif UDP in packet:
          packet_type = "UDP"
          source_port = packet[UDP].sport
          dest_port = packet[UDP].dport
      elif ICMP in packet:
          packet_type = "ICMP"
      elif ARP in packet:
          packet_type = "ARP"
      elif DNS in packet:
          packet_type = "DNS"
      elif DHCP in packet:
          packet_type = "DHCP"
      elif IPv6 in packet:
          packet_type = "IPv6"
      elif IP in packet:
          packet_type = "IP"

      # Ajouter les informations dans les cellules du tableau
      self.ui.tableWidget_2.setItem(row_position, 0, QTableWidgetItem(str(timestamp)))  # Timestamp
      self.ui.tableWidget_2.setItem(row_position, 1, QTableWidgetItem(source_mac))  # Source MAC
      self.ui.tableWidget_2.setItem(row_position, 2, QTableWidgetItem(dest_mac))  # Destination MAC
      self.ui.tableWidget_2.setItem(row_position, 3, QTableWidgetItem(source_ip))  # Source IP
      self.ui.tableWidget_2.setItem(row_position, 4, QTableWidgetItem(dest_ip))  # Destination IP
      self.ui.tableWidget_2.setItem(row_position, 5, QTableWidgetItem(str(protocol)))  # Protocol
      self.ui.tableWidget_2.setItem(row_position, 6, QTableWidgetItem(str(length)))  # Length
      self.ui.tableWidget_2.setItem(row_position, 7, QTableWidgetItem(str(source_port)))  # Source Port
      self.ui.tableWidget_2.setItem(row_position, 8, QTableWidgetItem(str(dest_port)))  # Destination Port
      self.ui.tableWidget_2.setItem(row_position, 9, QTableWidgetItem(packet_type))  # Packet Type

      # Marquer les paquets suspects
      if self.is_suspicious_packet(packet):
          for col in range(self.ui.tableWidget_2.columnCount()):
              self.ui.tableWidget_2.item(row_position, col).setBackground(Qt.green) #  # Marquer en jaune

  def clear_filters(self):
    """Effacer les filtres et réinitialiser le tableau."""
    self.ui.ip_src.clear()
    self.ui.ip_dest.clear()
    self.ui.port_src.clear()
    self.ui.port_dest.clear()
    self.ui.protocol.setCurrentIndex(0)  # Réinitialiser à "Sélectionner Protocole"
    self.filter_packets()  # Réappliquer le filtrage (vide)
    # Afficher un message de confirmation
    self.show_message("Success", "Les données de Filtrage ont été réinitialisées.")

  def is_suspicious_packet(self, packet):
    """Déterminer si un paquet est suspect."""
    # Exemple de détection de paquets suspects
    if IP in packet:
        source_ip = packet[IP].src
        dest_ip = packet[IP].dst
        # Marquer les paquets provenant d'adresses IP suspectes
        if source_ip.startswith("192.168.1.100") or dest_ip.startswith("192.168.1.100"):
            return True
    return False

##################################################################" MENACE ###############################################################################################################"
  def is_suspicious_packet(self, packet):
    """
    Vérifie si un paquet est suspect en utilisant des critères génériques.
    :param packet: Le paquet à analyser.
    :return: True si le paquet est suspect, False sinon.
    """
    try:
        # 1. Vérifier la taille du paquet
        packet_length = len(packet)
        if packet_length > 1500:  # Taille maximale typique pour un paquet Ethernet
            return True  # Paquet trop grand, potentiellement suspect

        # 2. Vérifier les paquets avec des adresses MAC invalides
        if Ether in packet:
            source_mac = packet[Ether].src
            dest_mac = packet[Ether].dst
            if source_mac == "00:00:00:00:00:00" or dest_mac == "00:00:00:00:00:00":
                return True  # Adresse MAC invalide

        # 3. Vérifier les paquets avec des adresses IP invalides
        if IP in packet:
            source_ip = packet[IP].src
            dest_ip = packet[IP].dst
            if source_ip == "0.0.0.0" or dest_ip == "0.0.0.0":
                return True  # Adresse IP invalide

        # 4. Vérifier les paquets ICMP (ping flood, etc.)
        if ICMP in packet:
            if packet_length > 1000:  # Paquets ICMP volumineux
                return True

        # 5. Vérifier les paquets ARP (ARP spoofing)
        if ARP in packet:
            if packet[ARP].op not in [1, 2]:  # Opérations ARP normales : 1 (requête), 2 (réponse)
                return True  # Opération ARP inhabituelle

        # 6. Vérifier les paquets DNS (requêtes suspectes)
        if DNS in packet:
            if hasattr(packet[DNS], "qd") and packet[DNS].qd:
                domain = packet[DNS].qd.qname.decode("utf-8").rstrip(".")
                if len(domain) > 50:  # Nom de domaine trop long
                    return True

        # 7. Vérifier les paquets avec des flags TCP inhabituels
        if TCP in packet:
            flags = packet[TCP].flags
            if flags not in ["S", "SA", "A", "PA", "FA", "R"]:  # Flags TCP normaux
                return True  # Flags TCP inhabituels

        # 8. Vérifier les paquets UDP avec une charge utile inhabituelle
        if UDP in packet:
            if packet_length > 512:  # Paquets UDP volumineux
                return True

        # 9. Vérifier les paquets IPv6 (tunneling suspect)
        if IPv6 in packet:
            if packet_length > 1500:  # Paquets IPv6 volumineux
                return True

        # Si aucun critère suspect n'est détecté, le paquet est considéré comme normal
        return False

    except Exception as e:
        # En cas d'erreur lors de l'analyse, considérer le paquet comme suspect par précaution
        logging.error(f"Erreur lors de l'analyse du paquet : {e}")
        return True

  def Ajout_menace(self, packet):
    """
    Ajoute un paquet suspect dans le tableau menace_table.
    :param packet: Le paquet à ajouter.
    """
    try:
        # Vérifier si le paquet est suspect
        if self.is_suspicious_packet(packet):
            # Ajouter le paquet dans le tableau menace_table
            row_position = self.ui.menace_table.rowCount()
            self.ui.menace_table.insertRow(row_position)

            # Extraire les informations du paquet
            timestamp = packet.time
            source_mac = packet.src if Ether in packet else ""
            dest_mac = packet.dst if Ether in packet else ""
            source_ip = packet[IP].src if IP in packet else ""
            dest_ip = packet[IP].dst if IP in packet else ""
            protocol = packet.proto if IP in packet else ""
            length = len(packet)

            # Déterminer le type du paquet et les ports si présents
            packet_type = ""
            source_port = ""
            dest_port = ""

            if TCP in packet:
                packet_type = "TCP"
                source_port = packet[TCP].sport
                dest_port = packet[TCP].dport
            elif UDP in packet:
                packet_type = "UDP"
                source_port = packet[UDP].sport
                dest_port = packet[UDP].dport
            elif ICMP in packet:
                packet_type = "ICMP"
            elif ARP in packet:
                packet_type = "ARP"
            elif DNS in packet:
                packet_type = "DNS"
            elif DHCP in packet:
                packet_type = "DHCP"
            elif IPv6 in packet:
                packet_type = "IPv6"
            elif IP in packet:
                packet_type = "IP"

            # Ajouter les informations dans les cellules du tableau
            self.ui.menace_table.setItem(row_position, 0, QTableWidgetItem(str(timestamp)))  # Timestamp
            self.ui.menace_table.setItem(row_position, 1, QTableWidgetItem(source_mac))  # Source MAC
            self.ui.menace_table.setItem(row_position, 2, QTableWidgetItem(dest_mac))  # Destination MAC
            self.ui.menace_table.setItem(row_position, 3, QTableWidgetItem(source_ip))  # Source IP
            self.ui.menace_table.setItem(row_position, 4, QTableWidgetItem(dest_ip))  # Destination IP
            self.ui.menace_table.setItem(row_position, 5, QTableWidgetItem(str(protocol)))  # Protocol
            self.ui.menace_table.setItem(row_position, 6, QTableWidgetItem(str(length)))  # Length
            self.ui.menace_table.setItem(row_position, 7, QTableWidgetItem(str(source_port)))  # Source Port
            self.ui.menace_table.setItem(row_position, 8, QTableWidgetItem(str(dest_port)))  # Destination Port
            self.ui.menace_table.setItem(row_position, 9, QTableWidgetItem(packet_type))  # Packet Type

            # Marquer la ligne en rouge pour indiquer une menace
            for col in range(self.ui.menace_table.columnCount() - 1):  # Ne pas colorer la colonne Action
                self.ui.menace_table.item(row_position, col).setBackground(Qt.red)

            # Ajouter les boutons dans la colonne "Action"
            #self.add_action_buttons(row_position)

    except Exception as e:
        logging.error(f"Erreur lors de l'ajout du paquet dans menace_table : {e}")

  def show_context_menu(self, position):
    """
    Affiche un menu contextuel au clic droit sur une ligne du tableau menace_table.
    """
    # Récupérer la ligne sélectionnée
    selected_row = self.ui.menace_table.rowAt(position.y())
    if selected_row == -1:  # Aucune ligne sélectionnée
        return

    # Créer un menu contextuel
    context_menu = QMenu(self)

    # Ajouter les actions au menu
    action_blacklist = context_menu.addAction("Ajouter à la blackliste")
    action_whitelist = context_menu.addAction("Ajouter à la whiteliste")
    action_dns_list = context_menu.addAction("Ajouter à la DNS liste")

    # Connecter les actions aux fonctions correspondantes
    action_blacklist.triggered.connect(lambda: self.add_to_blacklist(selected_row))
    
    action_whitelist.triggered.connect(lambda: self.add_to_whitelist(selected_row))
    action_dns_list.triggered.connect(lambda: self.add_to_dns_list(selected_row))
    

    # Afficher le menu contextuel à la position du clic
    context_menu.exec_(self.ui.menace_table.viewport().mapToGlobal(position))
  
  def add_to_blacklist(self, row):
    """
    Ajoute l'adresse IP de la ligne sélectionnée à la blackliste et la bloque sur le système.
    """
    ip_address = self.ui.menace_table.item(row, 3).text()  # Récupérer l'adresse IP

    # Naviguer vers la page "black" dans le stackedWidget "listes"
    self.ui.listes.setCurrentWidget(self.ui.black)

    # Ajouter l'adresse IP dans black_table
    self.add_to_table(self.ui.black_table, ip_address)

    # Bloquer l'adresse IP sur le système
    if self.block_ip(ip_address):
        self.show_message("Blackliste", f"Adresse IP {ip_address} ajoutée à la blackliste et bloquée.")
    else:
        self.show_message("Erreur", f"Impossible de bloquer l'adresse IP {ip_address}.")

  def add_to_whitelist(self, row):
    """
    Ajoute l'adresse IP de la ligne sélectionnée à la whiteliste.
    """
    ip_address = self.ui.menace_table.item(row, 3).text()  # Récupérer l'adresse IP

    # Naviguer vers la page "white" dans le stackedWidget "listes"
    self.ui.listes.setCurrentWidget(self.ui.white)

    # Ajouter l'adresse IP dans white_table
    self.add_to_table(self.ui.white_table, ip_address)

    # Afficher un message de confirmation
    self.show_message("Whiteliste", f"Adresse IP {ip_address} ajoutée à la whiteliste.")

  def add_to_dns_list(self, row):
    """
    Ajoute le domaine de la ligne sélectionnée à la DNS liste.
    """
    domain = self.ui.menace_table.item(row, 3).text()  # Récupérer le domaine

    # Naviguer vers la page "dns" dans le stackedWidget "listes"
    self.ui.listes.setCurrentWidget(self.ui.dns)

    # Ajouter le domaine dans dns_table
    self.add_to_table(self.ui.dns_table, domain)

    # Afficher un message de confirmation
    self.show_message("DNS Liste", f"Domaine {domain} ajouté à la DNS liste.")

  def add_to_table(self, table, entry):
    """
    Ajoute une entrée (adresse IP ou domaine) dans un tableau spécifique.
    :param table: Le tableau cible (black_table, white_table, dns_table).
    :param entry: L'entrée à ajouter (adresse IP ou domaine).
    """
    # Vérifier si l'entrée existe déjà dans le tableau
    for row in range(table.rowCount()):
        if table.item(row, 0).text() == entry:
            return  # L'entrée existe déjà, ne rien faire

    # Ajouter une nouvelle ligne dans le tableau
    row_position = table.rowCount()
    table.insertRow(row_position)
    table.setItem(row_position, 0, QTableWidgetItem(entry))  # Ajouter l'entrée dans la première colonne

  def block_ip(self, ip_address):
    """
    Bloque une adresse IP sur le système (Windows ou Linux).
    :param ip_address: L'adresse IP à bloquer.
    :return: True si le blocage a réussi, False sinon.
    """
    try:
        system_os = platform.system()  # Détecter le système d'exploitation

        if system_os == "Windows":
            # Commande pour bloquer une adresse IP sous Windows
            command = f"netsh advfirewall firewall add rule name=\"Block {ip_address}\" dir=in action=block remoteip={ip_address}"
        elif system_os == "Linux":
            # Commande pour bloquer une adresse IP sous Linux
            command = f"iptables -A INPUT -s {ip_address} -j DROP"
        else:
            self.show_message("Erreur", "Système d'exploitation non pris en charge.")
            return False

        # Exécuter la commande système
        subprocess.run(command, shell=True, check=True)
        return True

    except subprocess.CalledProcessError as e:
        logging.error(f"Erreur lors du blocage de l'adresse IP {ip_address} : {e}")
        return False
    except Exception as e:
        logging.error(f"Erreur inattendue lors du blocage de l'adresse IP {ip_address} : {e}")
        return False
################################################################### ALERT #############################
  def process_packet_auto_block(self, packet):
    """
    Détecter les paquets graves et bloquer automatiquement l'adresse IP.
    :param packet: Le paquet capturé.
    """
    if packet.haslayer(IP) and packet.haslayer(ICMP):  # Utilisez IP et ICMP directement
        ip_src = packet[IP].src
        icmp_len = len(packet)

        # Détecter les paquets ICMP trop volumineux
        if icmp_len > self.MAX_PING_SIZE:
            print(f"Paquet ICMP trop grand détecté depuis {ip_src}, taille : {icmp_len} octets.")
            if ip_src not in self.suspected_ips:
                self.suspected_ips.add(ip_src)
                self.block_ip_auto(ip_src, "ICMP Grave")
  def block_ip_auto(self, ip_address, attack_type):
    """
    Bloquer automatiquement une adresse IP en cas de détection d'une activité grave.
    :param ip_address: L'adresse IP à bloquer.
    :param attack_type: Le type d'attaque détectée.
    """
    system = platform.system()
    print(f"Attaque grave {attack_type} détectée ! Blocage automatique de l'adresse IP : {ip_address}")

    # Bloquer l'adresse IP selon le système d'exploitation
    if system == "Linux":
        os.system(f"sudo iptables -A INPUT -s {ip_address} -j DROP")
    elif system == "Windows":
        os.system(f"netsh advfirewall firewall add rule name=\"Block {ip_address}\" dir=in action=block remoteip={ip_address}")
    else:
        print(f"Système non pris en charge : {system}")
        return

    # Ajouter l'alerte dans le tableau
    self.add_alert(ip_address, attack_type)

  def detect_brute_force_auto_block(self):
    """
    Détecter les attaques de brute force et bloquer automatiquement les adresses IP suspectes.
    """
    system = platform.system()
    if system == "Windows":
        brute_force_ips = self.detect_brute_force_windows()
    elif system == "Linux":
        brute_force_ips = self.detect_brute_force_linux()
        ssh_brute_force_ips = self.detect_ssh_brute_force()
    else:
        print("Système non pris en charge.")
        return

    # Bloquer automatiquement les adresses IP suspectes
    if brute_force_ips:
        print("Activité de brute force suspecte détectée depuis les adresses IP suivantes :")
        for ip, attempts in brute_force_ips.items():
            print(f"IP: {ip} - {attempts} tentatives échouées")
            self.block_ip_auto(ip, "Brute Force")

    if 'ssh_brute_force_ips' in locals() and ssh_brute_force_ips:
        print("Activité de brute force SSH suspecte détectée depuis les adresses IP suivantes :")
        for ip, attempts in ssh_brute_force_ips.items():
            print(f"IP: {ip} - {attempts} tentatives échouées")
            self.block_ip_auto(ip, "SSH Brute Force")


  def add_alert(self, ip_address, attack_type):
    """
    Ajouter une alerte dans le tableau alert_table.
    :param ip_address: L'adresse IP suspecte.
    :param attack_type: Le type d'attaque détectée.
    """
    # Vérifier si le tableau alert_table existe
    if not hasattr(self.ui, 'alert_table'):
        print("Erreur : Le tableau alert_table n'existe pas dans l'interface utilisateur.")
        return

    # Ajouter une nouvelle ligne dans le tableau
    row_position = self.ui.alert_table.rowCount()
    self.ui.alert_table.insertRow(row_position)

    # Ajouter les informations dans les cellules du tableau
    self.ui.alert_table.setItem(row_position, 0, QTableWidgetItem(time.strftime("%Y-%m-%d %H:%M:%S")))  # Timestamp
    self.ui.alert_table.setItem(row_position, 1, QTableWidgetItem(attack_type))  # Type d'attaque
    self.ui.alert_table.setItem(row_position, 2, QTableWidgetItem(ip_address))  # Adresse IP
    self.ui.alert_table.setItem(row_position, 3, QTableWidgetItem("Bloqué"))  # Action

    # Optionnel : Colorer la ligne en rouge pour indiquer une alerte grave
    for col in range(self.ui.alert_table.columnCount()):
        self.ui.alert_table.item(row_position, col).setBackground(Qt.red)

    print(f"Alerte ajoutée : {attack_type} depuis {ip_address}")


 ########################################" Profil " #################################"""
  








## Execute App
################################################################################################
if __name__ == "__main__":
  app=QApplication(sys.argv)
  window = MainWindow()
  sys.exit(app.exec_())
################################################################################################
## end ==>
################################################################################################