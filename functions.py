################################################################################################import bcrypt
import logging
from scapy.all import  IP, TCP, UDP, ICMP
################################################################################################

from src.ui_login import *
################################################################################################

################################################################################################

from Custom_Widgets import *



def setup_logging():
    """Configurer le système de journalisation."""
    logging.basicConfig(
        filename="app.log",  # Fichier de logs
        level=logging.INFO,  # Niveau de journalisation (INFO, WARNING, ERROR, etc.)
        format="%(asctime)s - %(levelname)s - %(message)s"  # Format des logs
    )

def log_login_attempt(username, success):
    """Journaliser une tentative de connexion."""
    if success:
        logging.info(f"Successful login attempt for user: {username}")
    else:
        logging.warning(f"Failed login attempt for user: {username}")


def packet_callback(self, packet):
    """Analyser chaque paquet capturé."""
    if not self.sniffing:
        return  # Arrêter l'analyse si le sniffing est désactivé

    logging.info(f"Paquet capturé : {packet.summary()}")

    # Ajouter le paquet à la liste des paquets capturés
    self.captured_packets.append(packet)

    # Afficher le paquet dans la page Capture
    self.display_packet(packet)

    # Détecter les paquets suspects
    if self.is_suspicious_packet(packet):
        logging.info("Paquet suspect détecté.")
        self.display_suspicious_packet(packet)  # Afficher dans la page Menace
        self.notify_suspicious_packet(packet)  # Notifier dans la page Alert

    # Détecter les ports non autorisés
    if self.is_unauthorized_port(packet):
        logging.info("Port non autorisé détecté.")
        self.display_unauthorized_port(packet)  # Afficher dans la page Menace
        self.notify_unauthorized_port(packet)  # Notifier dans la page Alert

    # Détecter les attaques courantes
    attack_type = self.detect_common_attacks(packet)
    if attack_type:
        logging.info(f"Attaque détectée : {attack_type}")
        self.display_attack_detected(packet, attack_type)  # Afficher dans la page Menace
        self.notify_attack_detected(packet, attack_type)  # Notifier dans la page Alert


def is_suspicious_packet(self, packet):
    """Identifier les paquets suspects."""
    if ICMP in packet:
        return True  # Les paquets ICMP sont considérés comme suspects
    if TCP in packet and packet[TCP].dport in [22, 80, 443]:  # Ports SSH, HTTP, HTTPS
        return False  # Les paquets sur ces ports ne sont pas suspects
    if UDP in packet and packet[UDP].dport in [53]:  # Port DNS
        return False  # Les paquets DNS ne sont pas suspects
    return True  # Tous les autres paquets sont considérés comme suspects


##############################################################ALERT #########################################################
def notify_suspicious_packet(self, packet):
    """Ajouter une notification pour un paquet suspect."""
    alert_message = f"Suspicious packet detected: {packet.summary()}"
    self.ui.alert_list.addItem(alert_message)  # Ajouter à la liste des alertes
    self.ui.alert_list.scrollToBottom()  # Faire défiler vers le bas pour voir la dernière alerte

def notify_unauthorized_port(self, packet):
    """Ajouter une notification pour un port non autorisé."""
    alert_message = f"Unauthorized port detected: {packet.summary()}"
    self.ui.alert_list.addItem(alert_message)
    self.ui.alert_list.scrollToBottom()

def notify_attack_detected(self, packet, attack_type):
    """Ajouter une notification pour une attaque détectée."""
    alert_message = f"{attack_type}: {packet.summary()}"
    self.ui.alert_list.addItem(alert_message)
    self.ui.alert_list.scrollToBottom() 


  


######################################################### MENACE #########################################################################################
def display_suspicious_packet(self, packet):
    """Afficher un paquet suspect dans la page Menace."""
    row_position = self.ui.menace_table.rowCount()
    self.ui.menace_table.insertRow(row_position)

    # Extraire les informations du paquet
    timestamp = packet.time
    source_ip = packet[IP].src if IP in packet else ""
    dest_ip = packet[IP].dst if IP in packet else ""
    protocol = packet.proto if IP in packet else ""
    length = len(packet)

    # Ajouter les informations dans les cellules du tableau
    self.ui.menace_table.setItem(row_position, 0, QTableWidgetItem(str(timestamp)))  # Timestamp
    self.ui.menace_table.setItem(row_position, 1, QTableWidgetItem(source_ip))  # Source IP
    self.ui.menace_table.setItem(row_position, 2, QTableWidgetItem(dest_ip))  # Destination IP
    self.ui.menace_table.setItem(row_position, 3, QTableWidgetItem(str(protocol)))  # Protocol
    self.ui.menace_table.setItem(row_position, 4, QTableWidgetItem(str(length)))  # Length
    self.ui.menace_table.setItem(row_position, 5, QTableWidgetItem("Suspicious Packet"))  # Type de menace

def display_unauthorized_port(self, packet):
    """Afficher un port non autorisé dans la page Menace."""
    row_position = self.ui.menace_table.rowCount()
    self.ui.menace_table.insertRow(row_position)

    # Extraire les informations du paquet
    timestamp = packet.time
    source_ip = packet[IP].src if IP in packet else ""
    dest_ip = packet[IP].dst if IP in packet else ""
    protocol = packet.proto if IP in packet else ""
    length = len(packet)
    dest_port = packet[TCP].dport if TCP in packet else packet[UDP].dport if UDP in packet else ""

    # Ajouter les informations dans les cellules du tableau
    self.ui.menace_table.setItem(row_position, 0, QTableWidgetItem(str(timestamp)))  # Timestamp
    self.ui.menace_table.setItem(row_position, 1, QTableWidgetItem(source_ip))  # Source IP
    self.ui.menace_table.setItem(row_position, 2, QTableWidgetItem(dest_ip))  # Destination IP
    self.ui.menace_table.setItem(row_position, 3, QTableWidgetItem(str(protocol)))  # Protocol
    self.ui.menace_table.setItem(row_position, 4, QTableWidgetItem(str(length)))  # Length
    self.ui.menace_table.setItem(row_position, 5, QTableWidgetItem(f"Unauthorized Port: {dest_port}"))  # Type de menace

def display_attack_detected(self, packet, attack_type):
    """Afficher une attaque détectée dans la page Menace."""
    row_position = self.ui.menace_table.rowCount()
    self.ui.menace_table.insertRow(row_position)

    # Extraire les informations du paquet
    timestamp = packet.time
    source_ip = packet[IP].src if IP in packet else ""
    dest_ip = packet[IP].dst if IP in packet else ""
    protocol = packet.proto if IP in packet else ""
    length = len(packet)

    # Ajouter les informations dans les cellules du tableau
    self.ui.menace_table.setItem(row_position, 0, QTableWidgetItem(str(timestamp)))  # Timestamp
    self.ui.menace_table.setItem(row_position, 1, QTableWidgetItem(source_ip))  # Source IP
    self.ui.menace_table.setItem(row_position, 2, QTableWidgetItem(dest_ip))  # Destination IP
    self.ui.menace_table.setItem(row_position, 3, QTableWidgetItem(str(protocol)))  # Protocol
    self.ui.menace_table.setItem(row_position, 4, QTableWidgetItem(str(length)))  # Length
    self.ui.menace_table.setItem(row_position, 5, QTableWidgetItem(attack_type))  # Type de menace

def is_unauthorized_port(self, packet):
    """Vérifier si un paquet utilise un port non autorisé."""
    # Liste des ports autorisés (exemple : SSH, HTTP, HTTPS, DNS)
    authorized_ports = [22, 80, 443, 53]

    if TCP in packet:
        return packet[TCP].dport not in authorized_ports
    if UDP in packet:
        return packet[UDP].dport not in authorized_ports
    return False  # Si ce n'est ni TCP ni UDP, on considère que le port est autorisé
  
def detect_common_attacks(self, packet):
        """Détecter des attaques courantes."""
        src_ip = packet[IP].src if IP in packet else None

        # Détection d'ICMP Flood
        if ICMP in packet:
            self.icmp_count[src_ip] += 1
            if self.icmp_count[src_ip] > self.icmp_flood_threshold:
                return "ICMP Flood"

        # Détection de SYN Flood
        if TCP in packet and packet[TCP].flags == "S":  # SYN flag
            self.syn_count[src_ip] += 1
            if self.syn_count[src_ip] > self.syn_flood_threshold:
                return "SYN Flood"

        # Détection de port scanning (exemple simplifié)
        if TCP in packet or UDP in packet:
            dst_port = packet[TCP].dport if TCP in packet else packet[UDP].dport
            self.syn_count[(src_ip, dst_port)] += 1
            if self.syn_count[(src_ip, dst_port)] > 5:  # Seuil arbitraire
                return "Port Scanning"

        return None  # Aucune attaque détectée


############################################################################"blocage ip ################################################################################
"""def block_ip(self, ip_address):
    Bloquer une IP suspecte en utilisant iptables.
    try:
        # Ajouter une règle iptables pour bloquer l'IP
        subprocess.run(["iptables", "-A", "INPUT", "-s", ip_address, "-j", "DROP"], check=True)
        self.show_message("Success", f"IP {ip_address} blocked successfully.")
        logging.info(f"Blocked IP: {ip_address}")
    except subprocess.CalledProcessError as e:
        self.show_message("Error", f"Failed to block IP {ip_address}: {str(e)}")
        logging.error(f"Failed to block IP {ip_address}: {str(e)}")"""
        
        
        
        
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
    """Afficher un paquet dans le tableau de la page Filtre."""
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
            self.ui.tableWidget_2.item(row_position, col).setBackground(Qt.yellow)  # Marquer en jaune
  
def clear_filters(self):
    """Efface les filtres et réinitialise le tableau."""
    self.ui.ip_src.clear()
    self.ui.ip_dest.clear()
    self.ui.port_src.clear()
    self.ui.port_dest.clear()
    self.ui.protocol.setCurrentIndex(0)  # Réinitialiser à "Sélectionner Protocole"
    self.filter_packets()  # Réappliquer le filtrage (vide)
    # Afficher un message de confirmation
    self.show_message("Success", "Les données de Filtrage ont été réinitialisées.")
