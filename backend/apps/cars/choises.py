from django.db.models import TextChoices


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


class FuelChoices(TextChoices):
    Diesel = 'Diesel'
    Petrol = 'Petrol'
    Gas = 'Gas'
    Electric = 'Electric'
    Hybrid = 'Hybrid'
    Hydrogen = 'Hydrogen'


class DriveChoices(TextChoices):
    FrontWheel = 'FrontWheel'
    RearWheel = 'RearWheel'
    AllWheel = 'AllWheel'
    FourWheel = 'FourWheel'


class GearBoxes(TextChoices):
    Manual = 'Manual'
    Automatic = 'Automatic'
    Variable = 'Variable'
    AutomatedManual = 'Automated Manual'
    SequentialTransmission = 'Sequential Transmission'
