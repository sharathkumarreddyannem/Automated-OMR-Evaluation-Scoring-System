import cv2
import json
import os

def evaluate_sheet(image_path):
    # Dummy evaluation logic for now
    # Replace with contour detection + answer comparison
    filename = os.path.basename(image_path)
    return {
        "student_id": filename.split('.')[0],
        "marks": {"Maths": 15, "Physics": 18, "Chemistry": 17, "Biology": 16, "English": 14},
        "total": 80
    }
