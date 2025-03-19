"""
    Given modality = "MRI", write an if-elif-else statement that prints:
    "Magnetic Resonance Imaging" for "MRI",
    "Computed Tomography" for "CT",
    "Other imaging modality" otherwise.
    
    Returns:
        str: The classification of the imaging modality.
"""
def scan_type_classification():
    modality = input("Enter imaging modality:").strip().upper()

    if modality =="MRI":
        print("Magnetic Resonance Imaging")
    elif modality =="CT":
        print("Computed Tomography")
    else:
        print("Other imaging modality")

scan_type_classification()