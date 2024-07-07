from django.db.models import TextChoices


class BrandChoices(TextChoices):
    Toyota = 'Toyota'
    Honda = 'Honda'
    Ford = 'Ford'
    Chevrolet = 'Chevrolet'
    BMW = 'BMW'
    MercedesBenz = 'Mercedes-Benz'
    Audi = 'Audi'
    Volkswagen = 'Volkswagen'
    Nissan = 'Nissan'
    Hyundai = 'Hyundai'
    Kia = 'Kia'
    Subaru = 'Subaru'
    Mazda = 'Mazda'
    Jeep = 'Jeep'
    Lexus = 'Lexus'
    Dodge = 'Dodge'
    Tesla = 'Tesla'
    Volvo = 'Volvo'
    Porsche = 'Porsche'
    LandRover = 'Land Rover'

CAR_MODELS = {
    'Toyota': ['Camry', 'Corolla', 'RAV4', 'Highlander', 'Prius'],
    'Honda': ['Civic', 'Accord', 'CR-V', 'Fit', 'Pilot'],
    'Ford': ['F-150', 'Mustang', 'Explorer', 'Escape', 'Focus'],
    'Chevrolet': ['Silverado', 'Equinox', 'Malibu', 'Tahoe', 'Impala'],
    'BMW': ['3 Series', '5 Series', 'X3', 'X5', '7 Series'],
    'Mercedes-Benz': ['C-Class', 'E-Class', 'GLC', 'GLE', 'S-Class'],
    'Audi': ['A3', 'A4', 'Q5', 'Q7', 'A6'],
    'Volkswagen': ['Golf', 'Passat', 'Tiguan', 'Jetta', 'Atlas'],
    'Nissan': ['Altima', 'Sentra', 'Rogue', 'Murano', 'Maxima'],
    'Hyundai': ['Elantra', 'Sonata', 'Tucson', 'Santa Fe', 'Palisade'],
    'Kia': ['Forte', 'Optima', 'Sorento', 'Sportage', 'Soul'],
    'Subaru': ['Impreza', 'Outback', 'Forester', 'Crosstrek', 'Legacy'],
    'Mazda': ['Mazda3', 'Mazda6', 'CX-5', 'CX-9', 'MX-5 Miata'],
    'Jeep': ['Wrangler', 'Grand Cherokee', 'Cherokee', 'Compass', 'Renegade'],
    'Lexus': ['RX', 'ES', 'NX', 'GX', 'LS'],
    'Dodge': ['Charger', 'Challenger', 'Durango', 'Journey', 'Grand Caravan'],
    'Tesla': ['Model S', 'Model 3', 'Model X', 'Model Y', 'Roadster'],
    'Volvo': ['XC40', 'XC60', 'XC90', 'S60', 'S90'],
    'Porsche': ['911', 'Cayenne', 'Macan', 'Panamera', 'Taycan'],
    'Land Rover': ['Range Rover', 'Discovery', 'Defender', 'Evoque', 'Velar'],
}


class CarChoices(TextChoices):
    Sedan = 'Sedan'
    Hatchback = 'Hatchback'
    Station = 'Station'
    Wagon = 'Wagon'
    Coupe = 'Coupe'
    Convertible = 'Convertibl'
    Roadster = 'Roadster'
    Crossover = 'Crossover'
    SUV = 'SUV'
    Pickup = 'Pickup'
    Truck = 'Truck'
    Van = 'Van'
    Minivan = 'Minivan'
    Limousine = 'Limousine'
    Fastback = 'Fastback'
    Liftback = 'Liftback'


class CurrencyChoices(TextChoices):
    USD = 'USD', 'USD'
    EUR = 'EUR', 'EUR'
    UAH = 'UAH', 'UAH'
