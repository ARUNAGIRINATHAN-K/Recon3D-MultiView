import cv2
import numpy as np

def detect_features(image_path, method='SIFT'):
    """
    Detect features in an image using SIFT or ORB.
    
    Args:
        image_path (str): Path to the image file.
        method (str): 'SIFT' or 'ORB'.
        
    Returns:
        keypoints, descriptors
    """
    img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    if img is None:
        raise ValueError(f"Could not load image at {image_path}")

    if method == 'SIFT':
        detector = cv2.SIFT_create()
    elif method == 'ORB':
        detector = cv2.ORB_create()
    else:
        raise ValueError("Method must be 'SIFT' or 'ORB'")

    keypoints, descriptors = detector.detectAndCompute(img, None)
    return keypoints, descriptors
