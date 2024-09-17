from django.db import models
from django.contrib.auth.models import User


ROLES = (
    ('T', 'Tank'),
    ('H', 'Healer'),
    ('D', 'DPS')
)

SERVERS = ( 
    ("01", "Adamantoise"),
    ("02", "Aegis"),
    ("03", "Alexander"),
    ("04", "Anima"),
    ("05", "Asura"),
    ("06", "Atomos"),
    ("07", "Bahamut"),
    ("08", "Balmung"),
    ("09", "Behemoth"),
    ("10", "Belias"),
    ("11", "Brynhildr"),
    ("12", "Cactuar"),
    ("13", "Carbuncle"),
    ("14", "Cerberus"),
    ("15", "Chocobo"),
    ("16", "Coeurl"),
    ("17", "Diabolos"),
    ("18", "Durandal"),
    ("19", "Excalibur"),
    ("20", "Exodus"),
    ("21", "Faerie"),
    ("22", "Famfrit"),
    ("23", "Fenrir"),
    ("24", "Garuda"),
    ("25", "Gilgamesh"),
    ("26", "Goblin"),
    ("27", "Gungnir"),
    ("28", "Hades"),
    ("29", "Hyperion"),
    ("30", "Ifrit"),
    ("31", "Ixion"),
    ("32", "Jenova"),
    ("33", "Kujata"),
    ("34", "Lamia"),
    ("35", "Leviathan"),
    ("36", "Lich"),
    ("37", "Louisoix"),
    ("38", "Malboro"),
    ("39", "Mandragora"),
    ("40", "Masamune"),
    ("41", "Mateus"),
    ("42", "Midgardsormr"),
    ("43", "Moogle"),
    ("44", "Odin"),
    ("45", "Omega"),
    ("46", "Pandaemonium"),
    ("47", "Phoenix"),
    ("48", "Ragnarok"),
    ("49", "Ramuh"),
    ("50", "Ridill"),
    ("51", "Sargatanas"),
    ("52", "Shinryu"),
    ("53", "Shiva"),
    ("54", "Siren"),
    ("55", "Tiamat"),
    ("56", "Titan"),
    ("57", "Tonberry"),
    ("58", "Typhon"),
    ("59", "Ultima"),
    ("60", "Ultros"),
    ("61", "Unicorn"),
    ("62", "Valefor"),
    ("63", "Yojimbo"),
    ("64", "Zalera"),
    ("65", "Zeromus"),
    ("66", "Zodiark"),
    ("67", "Spriggan"),
    ("68", "Twintania"),
    ("69", "Bismarck"),
    ("70", "Ravana"),
    ("71", "Sephirot"),
    ("72", "Sophia"),
    ("73", "Zurvan"),
    ("74", "Halicarnassus"),
    ("75", "Maduin"),
    ("76", "Marilith"),
    ("77", "Seraph"),
    ("78", "Alpha"),
    ("79", "Phantom"),
    ("80", "Raiden"),
    ("81", "Sagittarius")
)


class Player(models.Model):
    name = models.CharField(max_length=20)
    server = models.CharField(
        max_length=2,
        choices=SERVERS,
        default=SERVERS[0][0]
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    role = models.CharField(
        max_length=1,
        choices=ROLES,
        default=ROLES[0][0]
    )
    
    def __str__(self):
        return f"{self.name} is a {self.get_role_display()} on {self.get_server_display()}"