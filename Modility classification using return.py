def scan_type_classification(modality):
    
    if modality =="MRI":
        return "Magnetic Resonance Imaging"
    elif modality =="CT":
        return "Computed Tomography"
    else:
        return "Other modality"
modality = input("Enter modality:").strip().upper()
print(scan_type_classification(modality))