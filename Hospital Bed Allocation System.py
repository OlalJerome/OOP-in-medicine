# Hospital Bed Allocation System
# Filename: hospital_bed.py
# Create a `HospitalBed` class with:
# - `bed_number`
# - `patient_name` (default `None`)
# Implement methods:
# - `assign_bed(patient_name)` → Assigns a patient to the bed.
# - `release_bed()` → Frees up the bed

class HospitalBed:
    def __init__(self, bed_number, patient_name=None):
        self.bed_number = bed_number
        self.patient_name = patient_name

    def assign_bed(self, patient_name):
        self.patient_name = patient_name
        print(f"Patient {self.patient_name} is assigned to bed {self.bed_number}")

    def release_bed(self):
        self.patient_name = None
        print(f"Bed number {self.bed_number} is now free")

# Example usage:
bed1 = HospitalBed(101)
bed1.assign_bed("John Doe")
bed1.release_bed()
