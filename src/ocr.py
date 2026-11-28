import cv2
import mss
import numpy as np
import keyboard
from time import sleep
from paddleocr import PaddleOCR

SCREENSHOTS_FOLDER_PATH = "src/data/screenshots/"
SCREENSHOT_REGION = {"left": 888, "top": 873, "width": 80, "height": 26}
POLL_INTERVAL_SECONDS = 0.2

import cv2
import mss
import numpy as np
from time import sleep
from paddleocr import PaddleOCR

SCREENSHOT_REGION = {"left": 888, "top": 873, "width": 80, "height": 26} # INFO: Work button
POLL_INTERVAL_SECONDS = 0.2

def persistent_zone_text_prediction(zone: dict[str, int]=SCREENSHOT_REGION) -> None:
    ocr = PaddleOCR(
            lang="fr",
            ocr_version="PP-OCRv3",
            enable_mkldnn=False,
            use_doc_orientation_classify=False,
            use_doc_unwarping=False,
            use_textline_orientation=False,
        )

    previous_frame = None
    previous_texts = None

    with mss.MSS() as sct:
        while True:
            sleep(POLL_INTERVAL_SECONDS)
            screenshot = sct.grab(SCREENSHOT_REGION)
            image = cv2.cvtColor(np.asarray(screenshot), cv2.COLOR_BGRA2BGR)

            if previous_frame is not None and np.array_equal(image, previous_frame):
                continue
            previous_frame = image

            results = ocr.predict(image)
            texts = [text for page in results
                        for text in page["rec_texts"]]

            if texts != previous_texts:
                print(texts)
                previous_texts = texts


def take_screen_zone(zone: dict[str, int]=SCREENSHOT_REGION) -> cv2.cvtColor:
    """Take screenshot of a zone and return cv2 array image"""
    with mss.MSS() as sct:
        screenshot = sct.grab(zone)
        image = cv2.cvtColor(np.asarray(screenshot), cv2.COLOR_BGRA2BGR)
        return image


def predict_text(image: cv2.cvtColor) -> list[str]:
    """Predict text on a cv2 array image"""
    ocr = PaddleOCR(
        lang="fr",
        ocr_version="PP-OCRv3",
        enable_mkldnn=False,
        use_doc_orientation_classify=False,
        use_doc_unwarping=False,
        use_textline_orientation=False,
    )
    results = ocr.predict(image)
    texts = [text for page in results
                for text in page["rec_texts"]]
    return texts


def read_zone(zone: dict[str, int]=SCREENSHOT_REGION) -> list[str]:
    """ Read and predict text in zone (OneShot) Return text"""
    ocr = PaddleOCR(
                lang="fr",
                ocr_version="PP-OCRv3",
                enable_mkldnn=False,
                use_doc_orientation_classify=False,
                use_doc_unwarping=False,
                use_textline_orientation=False,
            )
    
    with mss.MSS() as sct:
        # screenshot = sct.grab(sct.monitors[1]) # INFO: to screen entire screen
        screenshot = sct.grab(zone)

    image = cv2.cvtColor(np.asarray(screenshot), cv2.COLOR_BGRA2BGR)

    # INFO: To write image
    # SCREENSHOTS_PATH = SCREENSHOTS_FOLDER_PATH + f"test.png"
    # cv2.imwrite(SCREENSHOTS_PATH, image)

    results = ocr.predict(image)

    texts = [text for page in results
             for text in page["rec_texts"]] # INFO: ["rec_scores"] for confidence score
    
    return texts




# python -m src.ocr