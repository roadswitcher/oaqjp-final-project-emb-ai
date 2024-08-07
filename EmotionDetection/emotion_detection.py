import requests
import json
from requests.exceptions import SSLError

def emotion_detector(text_to_analyze):
    """Given text to analyze, determine emotions using IBM Watson NLP libraries"""
    url = "https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"
    input_json = {"raw_document": {"text": text_to_analyze}}
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    response = requests.post(url, json=input_json, headers=headers).json()

    generic_none_response = {
        "anger": None,"disgust": None,"fear": None,"joy": None,"sadness": None,"dominant_emotion": None,
    }

    if not text_to_analyze.strip():
        return generic_none_response

    emotion_predictions = response.get("emotionPredictions")


    predictions = emotion_predictions[0]["emotion"]
    if predictions:
        emotions = {key: predictions.get(key, None) for key in predictions}
        emotions["dominant_emotion"] = max(predictions, key=predictions.get)
    else:
        emotions = generic_none_response
    
    return emotions