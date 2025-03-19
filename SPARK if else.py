def scan_type_classification(modality):
    """
    Given modality = "MRI", write an if-elif-else statement that prints:
    "Magnetic Resonance Imaging" for "MRI",
    "Computed Tomography" for "CT",
    "Other imaging modality" otherwise.
    
    Returns:
        str: The classification of the imaging modality.
    """
    modality = input("Enter Modality", scan_type_classification(modality))
   
        if input ==MRI:
            print("Magnetic Resonance Imaging")

        elif input ==CT:
            print("Computed Tomography")
        else:
            print("Other imaging modalities")
    return scan_type_classification()