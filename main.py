################################################################################################
import sys
import sqlite3
import re
import threading
from functools import partial
import bcrypt
import logging
from scapy.all import sniff, Ether, IP, TCP, UDP, ICMP, ARP, DNS, DHCP, IPv6
################################################################################################

from src.ui_login import *
################################################################################################


################################################################################################

from Custom_Widgets import *

from Custom_Widgets.QAppSettings import QAppSettings

from PySide6.QtWidgets import QMessageBox
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
    self.ui = Ui_MainWindow()
    self.ui.setupUi(self) 

    # Initialisation de la base de données
    create_user_table()

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
    self.ui.to_capture.clicked.connect(partial(self.nav_packet_page,"capture"))
    self.ui.to_filtrer.clicked.connect(partial(self.nav_packet_page, "filtrer"))
    self.ui.editbtn.clicked.connect(partial(self.nav_profil_page,"edit_form"))
    self.ui.deletbtn.clicked.connect(partial(self.nav_profil_page,"delate"))
    self.ui.logout.clicked.connect(self.logout)
    self.ui.logout_2.clicked.connect(self.logout)
    
    #sniffing button 
    self.captured_packets = []
    self.sniffing = False
    
    self.ui.start.clicked.connect(self.start_sniffing)
    self.ui.stop.clicked.connect(self.stop_sniffing)
    self.ui.clear_sniffing.clicked.connect(self.clear_sniffing_data)
    
    #flitre button 
    # Bouton pour appliquer les filtres
    self.ui.start_filter.clicked.connect(self.filter_packets)

    # Bouton pour effacer les filtres
    self.ui.clear_filter_button.clicked.connect(self.clear_filters)
  
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

################################################################################################
## Execute App
################################################################################################
if __name__ == "__main__":
  app=QApplication(sys.argv)
  window = MainWindow()
  sys.exit(app.exec_())
################################################################################################
## end ==>
################################################################################################