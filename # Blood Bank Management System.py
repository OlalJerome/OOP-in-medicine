# Blood Bank Management System
# Filename: blood_bank.py
# Create a `BloodBank` class with:
# - `blood_type`
# - `units_available`
# Implement methods:
# - `donate_blood(units)` → Increases the units available.
# - `request_blood(units)` → Decreases units if enough stock exists.

class BloodBank:
    def __init__(self, blood_type, units_available):
        self.blood_type = blood_type
        self.units_available = units_available
    def donate_blood(self, units):
        if units > 0:
          self.units_available += units
          print(f"{units} units of blood donated")
        else:
          print("Invalid units. Units must be greater than 0.")
    def request_blood(self, units):
        if self.units_available >= units:
            self.units_available -= units
            print(f"{units} units of blood requested")
        else:
            print("Insufficient blood units available.")
       
bank = BloodBank("O+", 10)
print(bank.units_available)
print(bank.blood_type)

bank.donate_blood(5)
print(bank.units_available)

bank.request_blood(7)
print(bank.units_available)
