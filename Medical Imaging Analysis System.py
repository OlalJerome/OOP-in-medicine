# Medical Imaging Analysis System
# Filename: mri_scan.py
# Create an `MRI_Scan` class with:
# - `patient_name`
# - `scan_date`
# - `findings` (default `None`)
# Implement methods:
# - `add_findings(report)` → Updates the scan findings.
# - `get_scan_details()` → Returns patient name, date, and findings.

class MRI_Scan:
    def __init__(self, patient_name, scan_date, findings=None):
        self.patient_name = patient_name
        self.scan_date = scan_date
        self.findings = findings

    def add_findings(self, report):
        self.findings= report

    def get_scan_details(self):
        return self.patient_name, self.scan_date, self.findings
        
scan1 = MRI_Scan("Abel", "22-04-2001")
print(f"Patient: {scan1.patient_name}")

scan1.add_findings("Mild brain swelling detected.")
print(f"Scan Details: {scan1.get_scan_details()}")  
