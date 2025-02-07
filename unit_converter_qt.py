from PyQt6.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout, 
                            QHBoxLayout, QLabel, QLineEdit, QComboBox, QPushButton, 
                            QListWidget, QFrame, QListWidgetItem)
from PyQt6.QtCore import Qt, pyqtSlot
from PyQt6.QtGui import QFont, QIcon
import sys
import os

class UnitConverterQt(QMainWindow):
    def __init__(self):
        super().__init__()
        
        # İkon yolunu al
        icon_path = os.path.join(os.path.dirname(__file__), "ikon.png")
        
        # Pencere ikonu ayarla
        self.setWindowIcon(QIcon(icon_path))
        
        # Önce sözlükleri tanımla
        self.conversions = {
            "Length": {
                "meter": 1,
                "kilometer": 0.001,
                "centimeter": 100,
                "millimeter": 1000,
                "mile": 0.000621371,
                "yard": 1.09361,
                "foot": 3.28084,
                "inch": 39.3701,
                "nautical mile": 0.000539957,
                "parsec": 3.24078e-17,
                "angstrom": 10000000000,
                "micron": 1000000,
            },
            "Weight": {
                "kilogram": 1,
                "gram": 1000,
                "milligram": 1000000,
                "metric ton": 0.001,
                "pound": 2.20462,
                "ounce": 35.274,
                "carat": 5000,
                "grain": 15432.4,
                "stone": 0.157473,
                "long ton": 0.000984207,
                "short ton": 0.00110231,
                "atomic mass unit": 6.02214e+26,
            },
            "Volume": {
                "liter": 1,
                "milliliter": 1000,
                "cubic meter": 0.001,
                "cubic centimeter": 1000,
                "gallon (US)": 3.78541,      # 1 US gallon = 3.78541 L
                "gallon (UK)": 4.54609,      # 1 UK gallon = 4.54609 L
                "barrel": 158.987,           # 1 oil barrel = 158.987 L
                "cup": 0.236588,             # 1 US cup = 236.588 mL
                "tablespoon": 0.0147868,     # 1 US tbsp = 14.7868 mL
                "teaspoon": 0.00492892,      # 1 US tsp = 4.92892 mL
                "fluid ounce": 0.0295735,    # 1 US fl oz = 29.5735 mL
                "cubic foot": 28.3168,       # 1 ft³ = 28.3168 L
                "cubic inch": 0.0163871,     # 1 in³ = 16.3871 mL
                "pint (US)": 0.473176,       # 1 US pt = 473.176 mL
                "pint (UK)": 0.568261,       # 1 UK pt = 568.261 mL
                "quart": 0.946353,           # 1 US qt = 946.353 mL
            },
            "Area": {
                "square meter": 1,
                "square kilometer": 0.000001,
                "hectare": 0.0001,
                "are": 0.01,
                "acre": 0.000247105,
                "square foot": 10.7639,
                "square yard": 1.19599,
                "square mile": 3.861e-7,
                "square inch": 1550,
                "square centimeter": 10000,
                "square millimeter": 1000000,
            },
            "Data Storage (Binary)": {
                "byte": 1,
                "kibibyte": 1/1024,          # 2^10 bytes
                "mebibyte": 1/1024**2,       # 2^20 bytes
                "gibibyte": 1/1024**3,       # 2^30 bytes
                "tebibyte": 1/1024**4,       # 2^40 bytes
                "pebibyte": 1/1024**5,       # 2^50 bytes
                "bit": 8,                    # 8 bits = 1 byte
            },
            "Data Storage (Decimal)": {
                "byte": 1,
                "kilobyte": 1/1000,          # 10^3 bytes
                "megabyte": 1/1000**2,       # 10^6 bytes
                "gigabyte": 1/1000**3,       # 10^9 bytes
                "terabyte": 1/1000**4,       # 10^12 bytes
                "petabyte": 1/1000**5,       # 10^15 bytes
                "bit": 8,                    # 8 bits = 1 byte
                "kilobit": 8/1000,           # 10^3 bits
                "megabit": 8/1000**2,        # 10^6 bits
                "gigabit": 8/1000**3,        # 10^9 bits
            },
            "Speed": {
                "meter/second": 1,
                "kilometer/hour": 3.6,
                "mile/hour": 2.23694,
                "knot": 1.94384,
                "foot/second": 3.28084,
                "mach": 0.00293858,
                "light speed": 3.33564e-9,
                "kilometer/second": 0.001,
            },
            "Time": {
                "second": 1,
                "minute": 0.0166667,
                "hour": 0.000277778,
                "day": 1.15741e-5,
                "week": 1.65344e-6,
                "month": 3.80517e-7,
                "year": 3.171e-8,
                "decade": 3.171e-9,
                "century": 3.171e-10,
                "millennium": 3.171e-11,
                "microsecond": 1000000,
                "millisecond": 1000,
                "nanosecond": 1000000000,
            },
            "Temperature": {
                "Celsius": "C",
                "Fahrenheit": "F",
                "Kelvin": "K"
            },
            "Pressure": {
                "pascal": 1,
                "bar": 0.00001,
                "atmosphere": 9.86923e-6,
                "psi": 0.000145038,
                "mmHg": 0.00750062,
                "inHg": 0.000295301,
                "kilopascal": 0.001,
                "megapascal": 0.000001,
                "torr": 0.00750062,
                "pound/square foot": 0.0208854,
            },
            "Energy": {
                "joule": 1,
                "calorie": 0.239006,
                "kilocalorie": 0.000239006,
                "watt-hour": 0.000277778,
                "kilowatt-hour": 2.77778e-7,
                "electron volt": 6.242e+18,
                "BTU": 0.000947817,
                "therm": 9.4804e-9,
                "foot-pound": 0.737562,
                "erg": 10000000,
            },
            "Power": {
                "watt": 1,
                "kilowatt": 0.001,
                "megawatt": 0.000001,
                "horsepower": 0.00134102,
                "BTU/hour": 3.41214,
                "foot-pound/minute": 44.2537,
                "calorie/second": 0.239006,
            },
            "Angle": {
                "degree": 1,
                "radian": 0.0174533,
                "gradian": 1.11111,
                "arcminute": 60,
                "arcsecond": 3600,
                "revolution": 0.00277778,
            },
            "Digital Resolution": {
                "pixels": 1,
                "480p": 307200,            # 640x480
                "720p": 921600,            # 1280x720
                "1080p": 2073600,          # 1920x1080
                "1440p": 3686400,          # 2560x1440
                "2K": 2764800,             # 2560x1080
                "4K": 8294400,             # 3840x2160
                "8K": 33177600,            # 7680x4320
            },
            "Typography": {
                "point": 1,                  # Base unit (1/72 inch)
                "pica": 1/12,                # 1 pica = 12 points
                "inch": 1/72,                # 1 inch = 72 points
                "millimeter": 2.835,         # 1 mm = 2.835 points
                "Q": 0.709,                  # 1 Q = 0.25 mm = 0.709 points
                "didot": 0.937795,           # 1 didot = 0.375 mm
                "cicero": 11.2535,           # 1 cicero = 12 didot
            },
            "Astronomical": {
                "astronomical unit": 1,       # Base unit
                "light year": 1/63241.077,    # 1 AU ≈ 1/63,241.077 ly
                "parsec": 1/206264.806,       # 1 AU ≈ 1/206,264.806 pc
                "light second": 499.005,      # 1 AU ≈ 499.005 ls
                "light minute": 8.31675,      # 1 AU ≈ 8.31675 lm
                "light hour": 0.138613,       # 1 AU ≈ 0.138613 lh
                "light day": 0.00577554,      # 1 AU ≈ 0.00577554 ld
                "kiloparsec": 1/206264806,    # 1 AU ≈ 1/(1000*206,264.806) kpc
                "megaparsec": 1/206264806000, # 1 AU ≈ 1/(1000000*206,264.806) Mpc
            },
            "Radioactivity": {
                "becquerel": 1,
                "curie": 2.70270e-11,        # 1 Ci = 3.7×10¹⁰ Bq
                "millicurie": 2.70270e-8,    # 1 mCi = 3.7×10⁷ Bq
                "microcurie": 2.70270e-5,    # 1 µCi = 3.7×10⁴ Bq
                "nanocurie": 0.0270270,      # 1 nCi = 37 Bq
                "picocurie": 27.0270,        # 1 pCi = 0.037 Bq
                "rutherford": 1e-6,          # 1 Rd = 10⁶ Bq
                "disintegrations per second": 1,
            },
            "Prefixes": {
                "base": 1,
                "deca": 10,           # 10^1
                "hecto": 100,         # 10^2
                "kilo": 1000,         # 10^3
                "mega": 1e6,          # 10^6
                "giga": 1e9,          # 10^9
                "tera": 1e12,         # 10^12
                "peta": 1e15,         # 10^15
                "exa": 1e18,          # 10^18
                "zetta": 1e21,        # 10^21
                "yotta": 1e24,        # 10^24
                "deci": 0.1,          # 10^-1
                "centi": 0.01,        # 10^-2
                "milli": 0.001,       # 10^-3
                "micro": 1e-6,        # 10^-6
                "nano": 1e-9,         # 10^-9
                "pico": 1e-12,        # 10^-12
                "femto": 1e-15,       # 10^-15
                "atto": 1e-18,        # 10^-18
                "zepto": 1e-21,       # 10^-21
                "yocto": 1e-24,       # 10^-24
            },
            "Textile": {
                "denier": 1,
                "tex": 0.111111,
                "dtex": 1.11111,
                "micron": 10.1787,
                "decitex": 1.11111,
                "millitex": 111.111,
                "kilotex": 0.000111111,
                "gram/kilometer": 1.11111,
            },
            "Reddit Karma": {
                "post karma": 1,
                "comment karma": 2,
                "award karma": 5,
                "downvotes": -1,
                "reposts": 0.5,
                "cake day bonus": 10,
                "viral post": 50,
                "controversial": 0.1,
                "mod approval": 20,
            },
            "Meme Fame": {
                "viral tweet": 1,
                "reddit front page": 2,
                "tiktok trend": 3,
                "instagram repost": 0.5,
                "facebook mom share": 0.1,
                "youtube reaction": 1.5,
                "know your meme entry": 5,
                "buzzfeed article": 0.3,
                "celebrity retweet": 4,
            },
            "Cat Lives": {
                "standard cat life": 9,
                "indoor cat": 12,
                "outdoor cat": 6,
                "meme cat": 999,
                "grumpy cat": 1000,
                "keyboard cat": 88,
                "nyan cat": float('inf'),
                "schrodinger cat": 0.5,
                "garfield": 100,
            },
            "Dad Jokes": {
                "eye roll": 1,
                "audible groan": 2,
                "face palm": 3,
                "silent treatment": 5,
                "mom laugh": -1,
                "kid embarrassment": 4,
                "pun intensity": 2.5,
                "dad pride": 10,
                "comedy gold": 0.01,
            },
            "Gaming Skill": {
                "noob": 1,
                "casual": 5,
                "tryhard": 10,
                "pro gamer": 50,
                "rage quit": -5,
                "camping": 0.5,
                "360 no scope": 100,
                "keyboard warrior": 2,
                "esports ready": 1000,
                "git gud": 9000,
            },
            "Voltage": {
                "volt": 1,
                "millivolt": 1000,
                "microvolt": 1000000,
                "kilovolt": 0.001,
                "megavolt": 0.000001,
            },
            "Current": {
                "ampere": 1,
                "milliampere": 1000,
                "microampere": 1000000,
                "kiloampere": 0.001,
            },
            "Resistance": {
                "ohm": 1,
                "milliohm": 1000,
                "kiloohm": 0.001,
                "megaohm": 0.000001,
            },
            "Absorbed Dose": {
                "gray": 1,
                "rad": 100,
                "milligray": 1000,
                "kilogray": 0.001,
            },
            "Equivalent Dose": {
                "sievert": 1,
                "rem": 100,
                "millisievert": 1000,
                "microsievert": 1000000,
            },
            "Frequency": {
                "hertz": 1,
                "kilohertz": 0.001,
                "megahertz": 1e-6,
                "gigahertz": 1e-9,
                "terahertz": 1e-12,
                "revolution/minute": 60,    # RPM to Hz
                "beat/minute": 60,         # BPM to Hz
                "frame/second": 1,         # FPS = Hz
            },
            "Magnetic Field": {
                "tesla": 1,
                "gauss": 10000,
                "milligauss": 1e7,
                "microtesla": 1e6,
                "nanotesla": 1e9,
                "gamma": 1e9,           # 1 gamma = 1 nT
                "weber/square meter": 1,
                "maxwell/square centimeter": 10000,
            },
            "Sound Level": {
                "_type": "logarithmic",
                "decibel": 1,
                "bel": 10,
                "neper": 8.686,
            },
            "Fuel Economy": {
                "_type": "inverse",           # Özel dönüşüm gerektirir
                "miles/gallon": 1,            # Base unit (MPG)
                "kilometers/liter": 0.425144,  # 1 km/L ≈ 2.352 MPG
                "miles/liter": 0.264172,      # 1 mi/L ≈ 3.785 MPG
                "kilometers/gallon": 1.609344, # 1 km/gal ≈ 0.621 MPG
                "liters/100km": "inverse",    # L/100km = 235.215/MPG
            },
            "Viscosity": {
                "pascal second": 1,           # Pa·s
                "poise": 10,                  # P
                "centipoise": 1000,           # cP
                "millipascal second": 1000,   # mPa·s
                "square meter/second": 0.001,  # Kinematic viscosity
                "square foot/second": 0.0929,
                "stokes": 10000,              # St
                "centistokes": 1000000,       # cSt
                "pound/foot hour": 2419.088,
                "pound/foot second": 0.67197,
            },
            "Force": {
                "newton": 1,
                "kilonewton": 0.001,
                "dyne": 100000,
                "pound force": 0.224809,
                "kilogram force": 0.101972,
                "poundal": 7.23301,
            },
            "Acceleration": {
                "meter/second²": 1,           # Base unit
                "foot/second²": 3.28084,      # 1 m/s² ≈ 3.28084 ft/s²
                "gravity": 0.101972,          # 1 m/s² ≈ 0.101972 g
                "galileo": 100,               # 1 m/s² = 100 Gal
                "inch/second²": 39.3701,      # 1 m/s² ≈ 39.3701 in/s²
            },
            "Torque": {
                "newton meter": 1,
                "foot pound": 0.737562,
                "inch pound": 8.85074,
                "kilogram meter": 0.101972,
                "newton centimeter": 100,
            },
            "Density": {
                "kilogram/cubic meter": 1,
                "gram/cubic centimeter": 0.001,
                "pound/cubic foot": 0.062428,
                "pound/cubic inch": 3.61273e-5,
                "kilogram/liter": 0.001,
            },
            "Flow Rate": {
                "cubic meter/second": 1,
                "cubic foot/second": 35.3147,
                "liter/second": 1000,
                "gallon/minute": 15850.3,
                "cubic meter/hour": 3600,
            },
            "Banana Scale": {
                "banana": 1,
                "plantain": 1.2,
                "mini banana": 0.5,
                "king banana": 2,
                "banana bunch": 6,
                "banana box": 100,
                "banana truck": 10000,
                "banana container": 100000,
                "banana plantation": 1000000,
            },
            "Internet Time": {
                "real minute": 1,
                "youtube minute": 0.5,      # "I'll just watch one video"
                "social media minute": 0.1,  # "Just checking notifications"
                "loading time": 10,          # Feels like eternity
                "buffer time": 5,
                "ad time": 2,               # Feels longer than real time
                "skip ad time": 0.2,        # The longest 5 seconds
                "download time": 3,
                "windows update": 100,      # "Just a moment..."
            },
            "Developer Time": {
                "estimated hour": 1,
                "actual hour": 3,
                "quick fix": 2,             # "It will just take 5 minutes"
                "coffee break": 0.5,
                "debugging session": 4,
                "meeting hour": 0.75,       # Time spent actually discussing code
                "documentation time": 0.1,   # Time actually spent documenting
                "stack overflow time": 0.3,  # Time until finding the right answer
                "build time": 2,
            },
            "Internet Size": {
                "regular file": 1,
                "compressed file": 0.5,
                "after compression": 0.1,    # What you expect
                "after upload": 2,          # Somehow got bigger
                "download size": 1.5,       # Always bigger than advertised
                "available space": 0.8,     # Less than you thought
                "cloud storage": 0.7,       # After "unlimited" storage
                "attachment limit": 0.1,    # Never enough
                "free tier": 0.5,          # Actually usable space
            },
            "Procrastination": {
                "task minute": 1,
                "deadline minute": 0.1,     # Time flies near deadline
                "tomorrow": 1000,           # When you'll start working
                "last minute": 0.01,        # Super productive time
                "snooze time": 5,          # "5 more minutes"
                "weekend plan": 100,        # Time you think you have
                "monday motivation": 10,    # Time until it fades
                "new year resolution": 1000, # Time until giving up
                "study break": 2,          # Planned vs actual time
            },
        }

        # Capitalize first letter of each unit
        for category in self.conversions:
            self.conversions[category] = {
                k.title(): v for k, v in self.conversions[category].items()
            }

        # Kategorileri grupla
        self.category_groups = {
            "COMMON": [
                "Length", "Weight", "Volume", "Area", "Time", "Temperature"
            ],
            "SCIENCE ENGINEERING": [
                "Force", "Energy", "Power", "Pressure", "Speed", "Acceleration",
                "Torque", "Density", "Flow Rate", "Viscosity"
            ],
            "ELECTRONICS COMPUTING": [
                "Data Storage (Binary)", "Data Storage (Decimal)", "Digital Resolution",
                "Voltage", "Current", "Resistance", "Frequency"
            ],
            "SPECIALIZED": [
                "Typography", "Astronomical", "Absorbed Dose", "Equivalent Dose",
                "Radioactivity", "Magnetic Field", "Sound Level", "Textile",
                "Fuel Economy", "Angle"
            ],
            "FUN MEMES": [
                "Internet Time", "Banana Scale", "Developer Time",
                "Internet Size", "Procrastination", "Reddit Karma",
                "Meme Fame", "Cat Lives", "Dad Jokes", "Gaming Skill"
            ]
        }

        # Initialize category sections dictionary
        self.category_sections = {}

        # Pencere ayarları
        self.setWindowTitle("Unit Converter")
        self.setMinimumSize(900, 600)
        self.setStyleSheet("""
            QMainWindow {
                background-color: #2b2b2b;
            }
            QLabel {
                color: #ffffff;
            }
            QListWidget {
                background-color: #2b2b2b;
                border: none;
                border-radius: 8px;
                color: #ffffff;
                padding: 5px;
                font-size: 13px;
            }
            QListWidget::item {
                padding: 10px;
                margin: 2px;
                border-radius: 6px;
            }
            QListWidget::item:selected {
                background-color: #4CAF50;
                color: white;
            }
            QListWidget::item:hover {
                background-color: #404040;
            }
            QComboBox {
                background-color: #363636;
                border: none;
                border-radius: 5px;
                padding: 8px;
                color: #ffffff;
                min-width: 200px;
            }
            QComboBox::drop-down {
                border: none;
            }
            QComboBox::down-arrow {
                image: url(down_arrow.png);
                width: 12px;
                height: 12px;
            }
            QComboBox:on {
                border: 2px solid #4a4a4a;
            }
            QComboBox QAbstractItemView {
                background-color: #363636;
                color: #ffffff;
                selection-background-color: #4a4a4a;
                border: none;
            }
            QLineEdit {
                background-color: #363636;
                border: none;
                border-radius: 5px;
                padding: 8px;
                color: #ffffff;
                min-width: 200px;
            }
            QPushButton {
                background-color: #363636;
                border: none;
                border-radius: 5px;
                padding: 8px 15px;
                color: #ffffff;
            }
            QPushButton:hover {
                background-color: #4a4a4a;
            }
            QFrame#separator {
                background-color: #404040;
            }
            QLabel#resultLabel {
                font-size: 18px;
                font-weight: bold;
                color: #4CAF50;
            }
            QLabel#groupHeader {
                font-weight: bold;
                color: #4CAF50;
                padding: 15px 5px 5px 5px;
                font-size: 14px;
                border-bottom: 1px solid #404040;
                margin-bottom: 5px;
            }
        """)

        # Widget'ları oluştur
        self._create_widgets()

    def _create_widgets(self):
        # Create the central widget and main layout
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        main_layout = QHBoxLayout(central_widget)
        main_layout.setSpacing(0)  # Remove spacing between panels
        main_layout.setContentsMargins(0, 0, 0, 0)  # Remove margins

        # Left panel for categories
        left_panel = QWidget()
        left_panel.setFixedWidth(300)  # Fixed width for left panel
        left_panel.setStyleSheet("""
            QWidget {
                background-color: #2b2b2b;
                border-right: 1px solid #404040;
            }
        """)
        left_layout = QVBoxLayout(left_panel)
        left_layout.setContentsMargins(0, 0, 0, 0)
        left_layout.setSpacing(0)
        
        # Categories header
        categories_header = QLabel("CATEGORIES")
        categories_header.setStyleSheet("""
            font-size: 16px;
            font-weight: bold;
            color: white;
            padding: 15px;
            background-color: #363636;
            text-align: center;
            border-bottom: 1px solid #404040;
        """)
        categories_header.setAlignment(Qt.AlignmentFlag.AlignCenter)
        left_layout.addWidget(categories_header)
        
        # Add spacing after header
        spacing_widget = QWidget()
        spacing_widget.setFixedHeight(15)
        spacing_widget.setStyleSheet("background-color: transparent;")
        left_layout.addWidget(spacing_widget)
        
        # Container for category sections with padding
        categories_container = QWidget()
        categories_container.setStyleSheet("""
            QWidget {
                background-color: transparent;
                padding: 0 15px;  /* Sol ve sağ padding */
            }
        """)
        categories_layout = QVBoxLayout(categories_container)
        categories_layout.setContentsMargins(0, 0, 0, 0)
        categories_layout.setSpacing(0)
        
        # Create section for each category group
        for group in self.category_groups.keys():
            # Create container widget for the section
            section_widget = QWidget()
            section_layout = QVBoxLayout(section_widget)
            section_layout.setContentsMargins(0, 0, 0, 0)
            section_layout.setSpacing(0)
            
            # Create button
            btn = QPushButton(group.upper())
            btn.setStyleSheet("""
                QPushButton {
                    text-align: left;
                    padding: 12px 15px;
                    margin: 0 5px;
                    border: none;
                    background-color: transparent;
                    color: #4CAF50;
                    font-weight: bold;
                    font-size: 14px;
                }
                QPushButton:hover {
                    background-color: #363636;
                }
            """)
            btn.clicked.connect(lambda checked, g=group: self._toggle_subcategories(g))
            section_layout.addWidget(btn)
            
            # Create list widget for subcategories
            subcategories = QListWidget()
            subcategories.setFixedWidth(270)
            subcategories.setMinimumHeight(50)  # Minimum yükseklik ekle
            subcategories.setMaximumHeight(200)  # Maksimum yüksekliği azalt
            subcategories.setVerticalScrollMode(QListWidget.ScrollMode.ScrollPerPixel)  # Smooth scrolling
            subcategories.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOn)  # Scrollbar'ı her zaman göster
            subcategories.setStyleSheet("""
                QListWidget {
                    background-color: #2b2b2b;
                    border: none;
                    color: #ffffff;
                    padding: 5px;
                    font-size: 13px;
                    margin-left: 15px;
                }
                QListWidget::item {
                    padding: 12px;
                    margin: 2px;
                    border-radius: 6px;
                }
                QListWidget::item:selected {
                    background-color: #4CAF50;
                    color: white;
                }
                QListWidget::item:hover {
                    background-color: #404040;
                }
                QScrollBar:vertical {
                    border: none;
                    background: #2b2b2b;
                    width: 8px;
                    margin: 0px;
                }
                QScrollBar::handle:vertical {
                    background: #4a4a4a;
                    min-height: 20px;
                    border-radius: 4px;
                }
                QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical {
                    height: 0px;
                }
                QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {
                    background: none;
                    border-radius: 4px;
                }
            """)
            
            # Add subcategories to list
            for category in self.category_groups[group]:
                item = QListWidgetItem(category)
                item.setTextAlignment(Qt.AlignmentFlag.AlignLeft)
                subcategories.addItem(item)
            
            subcategories.hide()  # Initially hidden
            subcategories.itemClicked.connect(self._on_category_select)
            section_layout.addWidget(subcategories)
            
            # Store references
            self.category_sections[group] = {
                'button': btn,
                'list': subcategories,
                'widget': section_widget
            }
            
            categories_layout.addWidget(section_widget)
        
        categories_layout.addStretch()
        left_layout.addWidget(categories_container)
        
        # Vertical separator
        separator = QFrame()
        separator.setFrameShape(QFrame.Shape.VLine)
        separator.setObjectName("separator")
        
        # Right panel for conversion
        right_panel = QWidget()
        right_panel.setMinimumWidth(500)
        right_layout = QVBoxLayout(right_panel)
        right_layout.setContentsMargins(40, 20, 40, 20)
        
        # Add top stretch to push content to vertical center
        right_layout.addStretch(1)  # Üstten boşluk için
        
        # Title
        title = QLabel("Unit Converter")
        title.setFont(QFont("Arial", 24, QFont.Weight.Bold))
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        right_layout.addWidget(title)
        right_layout.addSpacing(30)  # Title ile conversion area arasına boşluk
        
        # Conversion area container for horizontal centering
        conversion_container = QWidget()
        conversion_container.setFixedWidth(600)  # Container genişliği
        conversion_layout = QHBoxLayout(conversion_container)
        conversion_layout.setContentsMargins(0, 0, 0, 0)
        
        # From section
        from_layout = QVBoxLayout()
        from_layout.setSpacing(10)  # Input ile combobox arası boşluk
        self.input_value = QLineEdit()
        self.input_value.setFixedWidth(200)  # Sabit genişlik
        self.input_value.setPlaceholderText("Enter value")
        self.input_value.setStyleSheet("""
            QLineEdit {
                background-color: #363636;
                border: none;
                border-radius: 5px;
                padding: 8px;
                color: white;
                min-width: 200px;
                font-size: 16px;
            }
            QLineEdit:focus {
                color: white;
            }
            QLineEdit::placeholder {
                color: #888888;
            }
        """)
        self.from_unit = QComboBox()
        self.from_unit.setFixedWidth(200)  # Sabit genişlik
        from_layout.addWidget(self.input_value, 0, Qt.AlignmentFlag.AlignCenter)
        from_layout.addWidget(self.from_unit, 0, Qt.AlignmentFlag.AlignCenter)
        
        # Middle section with swap button
        middle_layout = QVBoxLayout()
        middle_layout.setSpacing(10)  # Label ile button arası boşluk
        to_label = QLabel("TO")
        to_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.swap_button = QPushButton("⇄")
        self.swap_button.setFixedSize(40, 40)
        middle_layout.addWidget(to_label)
        middle_layout.addWidget(self.swap_button, 0, Qt.AlignmentFlag.AlignCenter)
        
        # To section
        to_layout = QVBoxLayout()
        to_layout.setSpacing(10)  # Result ile combobox arası boşluk
        self.result_label = QLineEdit()
        self.result_label.setFixedWidth(200)  # Sabit genişlik
        self.result_label.setReadOnly(True)
        self.result_label.setPlaceholderText("Result")
        self.result_label.setStyleSheet("""
            QLineEdit {
                background-color: #363636;
                border: none;
                border-radius: 5px;
                padding: 8px;
                color: #4CAF50;
                min-width: 200px;
                font-size: 16px;
                font-weight: bold;
            }
        """)
        self.to_unit = QComboBox()
        self.to_unit.setFixedWidth(200)  # Sabit genişlik
        to_layout.addWidget(self.result_label, 0, Qt.AlignmentFlag.AlignCenter)
        to_layout.addWidget(self.to_unit, 0, Qt.AlignmentFlag.AlignCenter)
        
        # Add sections to conversion layout with spacing
        conversion_layout.addStretch(1)  # Sol boşluk
        conversion_layout.addLayout(from_layout)
        conversion_layout.addLayout(middle_layout)
        conversion_layout.addLayout(to_layout)
        conversion_layout.addStretch(1)  # Sağ boşluk
        
        # Add conversion container to right panel
        right_layout.addWidget(conversion_container, 0, Qt.AlignmentFlag.AlignCenter)
        
        # Add bottom stretch to complete vertical centering
        right_layout.addStretch(1)  # Alttan boşluk için
        
        # Add panels to main layout
        main_layout.addWidget(left_panel)
        main_layout.addWidget(separator)
        main_layout.addWidget(right_panel)
        
        # Connect signals
        self.input_value.textChanged.connect(self._on_value_change)
        self.from_unit.currentTextChanged.connect(self._on_value_change)
        self.to_unit.currentTextChanged.connect(self._on_value_change)
        self.swap_button.clicked.connect(self._swap_units)
        
        # Initialize with default category and open COMMON section
        first_group = "COMMON"
        first_category = self.category_groups[first_group][0]
        self._toggle_subcategories(first_group)
        self._on_category_select(QListWidgetItem(first_category))

    def _on_category_select(self, item):
        try:
            if not item:
                return
                
            # Seçilen kategoriyi güncelle
            self.current_category = item.text()
            
            # Birimleri güncelle
            units = sorted(list(self.conversions[self.current_category].keys()))
            
            # Mevcut değerleri sakla
            current_value = self.input_value.text()
            
            # Combobox'ları temizle ve yeni birimleri ekle
            self.from_unit.clear()
            self.to_unit.clear()
            
            self.from_unit.addItems(units)
            self.to_unit.addItems(units)
            
            # İkinci birimi seç (eğer varsa)
            if len(units) > 1:
                self.to_unit.setCurrentIndex(1)
            
            # Eğer geçerli bir input varsa dönüşümü yap
            if current_value.strip():
                try:
                    float(current_value)  # Sayısal değer kontrolü
                    self._convert()
                except ValueError:
                    self.result_label.setText("Invalid number")
                    self.input_value.clear()
            else:
                self.result_label.clear()
                self.result_label.setPlaceholderText("Result")
                
        except Exception as e:
            print(f"Error in category selection: {e}")  # Hata ayıklama için
            self.result_label.setText("Error in conversion")
            self.input_value.clear()

    def _on_value_change(self):
        self._convert()

    def _convert(self):
        try:
            # Input boş ise sonucu temizle
            if not self.input_value.text().strip():
                self.result_label.clear()
                self.result_label.setPlaceholderText("Result")
                return

            # Gerekli değerlerin varlığını kontrol et
            if not hasattr(self, 'current_category') or \
               not self.from_unit.currentText() or \
               not self.to_unit.currentText():
                self.result_label.clear()
                self.result_label.setPlaceholderText("Result")
                return
                
            value = float(self.input_value.text())
            category = self.current_category
            from_unit = self.from_unit.currentText()
            to_unit = self.to_unit.currentText()

            # Boş birim seçimi kontrolü
            if not from_unit or not to_unit:
                self.result_label.clear()
                self.result_label.setPlaceholderText("Result")
                return

            # Handle special conversion types
            category_data = self.conversions[category]
            if isinstance(category_data, dict) and "_type" in category_data:
                if category_data["_type"] == "logarithmic":
                    result = self._convert_logarithmic(value, from_unit, to_unit, category_data)
                elif category_data["_type"] == "inverse":
                    result = self._convert_inverse(value, from_unit, to_unit, category_data)
                else:
                    result = self._convert_linear(value, from_unit, to_unit, category_data)
            elif category == "Temperature":
                result = self._convert_temperature(value, from_unit, to_unit)
            else:
                result = self._convert_linear(value, from_unit, to_unit, category_data)

            # Format result
            if result.is_integer():
                formatted_result = f"{result:,.0f}"
            else:
                formatted_result = f"{result:,.5f}".rstrip('0').rstrip('.')

            self.result_label.setText(formatted_result)

        except ValueError:
            self.result_label.setText("Invalid number")
        except ZeroDivisionError:
            self.result_label.setText("Cannot divide by zero")
        except KeyError:
            self.result_label.clear()
            self.result_label.setPlaceholderText("Result")
        except Exception as e:
            print(f"Conversion error: {e}")
            self.result_label.setText("Error in conversion")

    def _swap_units(self):
        from_idx = self.from_unit.currentIndex()
        to_idx = self.to_unit.currentIndex()
        
        self.from_unit.setCurrentIndex(to_idx)
        self.to_unit.setCurrentIndex(from_idx)
        
        self._convert()

    def _convert_temperature(self, value: float, from_unit: str, to_unit: str) -> float:
        # Celsius as base unit
        if from_unit == "Fahrenheit":
            celsius = (value - 32) * 5/9
        elif from_unit == "Kelvin":
            celsius = value - 273.15
        else:  # Celsius
            celsius = value

        # Convert from Celsius to target unit
        if to_unit == "Fahrenheit":
            return (celsius * 9/5) + 32
        elif to_unit == "Kelvin":
            return celsius + 273.15
        else:  # Celsius
            return celsius

    def _convert_linear(self, value, from_unit, to_unit, conversions):
        base_value = value / conversions[from_unit]
        return base_value * conversions[to_unit]

    def _convert_logarithmic(self, value, from_unit, to_unit, conversions):
        # Convert to base unit (dB)
        if from_unit != "decibel":
            value = value * conversions[from_unit]
        # Convert to target unit
        if to_unit != "decibel":
            value = value / conversions[to_unit]
        return value

    def _convert_inverse(self, value: float, from_unit: str, to_unit: str, conversions: dict) -> float:
        """Yakıt ekonomisi gibi ters orantılı dönüşümler için"""
        if value == 0:
            raise ZeroDivisionError

        if to_unit == "liters/100km":
            if from_unit == "miles/gallon":
                return 235.215 / value
            elif from_unit == "kilometers/liter":
                return 100 / value
            else:
                base_mpg = value / conversions[from_unit]
                return 235.215 / base_mpg
        elif from_unit == "liters/100km":
            if to_unit == "miles/gallon":
                return 235.215 / value
            elif to_unit == "kilometers/liter":
                return 100 / value
            else:
                mpg = 235.215 / value
                return mpg * conversions[to_unit]
        else:
            return value * conversions[to_unit] / conversions[from_unit]

    def _toggle_subcategories(self, group):
        # Update button styles and show/hide subcategories
        for g, section in self.category_sections.items():
            if g == group:
                # Toggle visibility of clicked section
                is_visible = section['list'].isVisible()
                section['list'].setVisible(not is_visible)
                
                # Update button style
                if not is_visible:
                    section['button'].setStyleSheet("""
                        QPushButton {
                            text-align: left;
                            padding: 12px 15px;
                            margin: 0 5px;
                            border: none;
                            background-color: transparent;
                            color: #4CAF50;
                            font-weight: bold;
                            font-size: 14px;
                        }
                    """)
                else:
                    section['button'].setStyleSheet("""
                        QPushButton {
                            text-align: left;
                            padding: 12px 15px;
                            margin: 0 5px;
                            border: none;
                            background-color: transparent;
                            color: #888888;
                            font-weight: bold;
                            font-size: 14px;
                        }
                        QPushButton:hover {
                            color: #4CAF50;
                        }
                    """)
            else:
                # Hide other sections and reset style
                section['list'].hide()
                section['button'].setStyleSheet("""
                    QPushButton {
                        text-align: left;
                        padding: 12px 15px;
                        margin: 0 5px;
                        border: none;
                        background-color: transparent;
                        color: #4CAF50;
                        font-weight: bold;
                        font-size: 14px;
                    }
                    QPushButton:hover {
                        color: #888888;
                    }
                """)

            # Update scrollbar style for the list
            section['list'].setStyleSheet("""
                QListWidget {
                    background-color: #2b2b2b;
                    border: none;
                    color: #ffffff;
                    padding: 5px;
                    font-size: 13px;
                }
                QListWidget::item {
                    padding: 12px;
                    margin: 2px;
                    border-radius: 6px;
                }
                QListWidget::item:selected {
                    background-color: #4CAF50;
                    color: white;
                }
                QListWidget::item:hover {
                    background-color: #404040;
                }
                QScrollBar:vertical {
                    border: none;
                    background: #2b2b2b;
                    width: 8px;
                    margin: 0;
                }
                QScrollBar::handle:vertical {
                    background: #404040;
                    min-height: 20px;
                    border-radius: 4px;
                }
                QScrollBar::add-line:vertical {
                    height: 0px;
                }
                QScrollBar::sub-line:vertical {
                    height: 0px;
                }
                QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {
                    background: none;
                }
            """)

def main():
    app = QApplication(sys.argv)
    window = UnitConverterQt()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main() 