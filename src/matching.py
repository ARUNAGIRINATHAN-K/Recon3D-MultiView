import cv2

def match_features(desc1, desc2, method='SIFT'):
    """
    Match features between two images.
    
    Args:
        desc1, desc2: Descriptors from two images.
        method (str): 'SIFT' or 'ORB' (determines norm type).
        
    Returns:
        matches
    """
    if method == 'SIFT':
        # NORM_L2 for SIFT
        norm = cv2.NORM_L2
    else:
        # NORM_HAMMING for ORB
        norm = cv2.NORM_HAMMING

    bf = cv2.BFMatcher(norm, crossCheck=True)
    matches = bf.match(desc1, desc2)
    
    # Sort matches by distance
    matches = sorted(matches, key=lambda x: x.distance)
    return matches
