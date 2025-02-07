# Unit Converter

Unit Converter is a comprehensive and user-friendly unit conversion application developed with PyQt6, featuring a modern interface.

## Features

- **35+ different categories**
- **300+ unit conversions**
- Modern dark theme interface
- Real-time conversion
- Category grouping
- Special conversion formulas (Temperature, Fuel Economy, etc.)
- Easy unit swap button

## Categories

### Common Units
- Length
- Weight
- Volume
- Area
- Time
- Temperature

### Science & Engineering
- Force
- Energy
- Power
- Pressure
- Speed
- Acceleration
- Torque
- Density
- Flow Rate
- Viscosity

### Electronics & Computing
- Data Storage (Binary)
- Data Storage (Decimal)
- Digital Resolution
- Voltage
- Current
- Resistance
- Frequency

### Specialized
- Typography
- Astronomical
- Radioactivity
- Magnetic Field
- Sound Level
- Textile
- Fuel Economy
- Angle

### Fun & Memes
- Internet Time
- Banana Scale
- Developer Time
- Internet Size
- Procrastination
- Reddit Karma
- Meme Fame
- Cat Lives
- Dad Jokes
- Gaming Skill

## Installation

1. Download the application.
2. Run the `.exe` file.
3. No installation required.

## Requirements (For Development)

- Python 3.6+
- PyQt6
- PyInstaller (for creating executable)

## Development

```bash
# Install required libraries
pip install PyQt6 pyinstaller

# Run the application
python unit_converter_qt.py

# Create executable file
python -m PyInstaller --name="Unit Converter" --windowed --onefile --noconsole --clean --icon=ikon.png --add-data="ikon.png;." unit_converter_qt.py
