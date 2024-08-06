import requests
import json
from requests.exceptions import SSLError

def get_emotion(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    input_json = {"raw_document": {"text": text_to_analyze}}
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    
    try:
        response = requests.post(url, json=input_json, headers=headers)
        response.raise_for_status() 
        return response.json()
    except requests.RequestException as e:
        return str(e) 

def emotion_detector(text_to_analyze):
    if text_to_analyze:
        response = get_emotion(text_to_analyze)
        emotion_predictions = response.get("emotionPredictions")
    else:
        emotion_predictions = {}
    
    if emotion_predictions:
        predictions = emotion_predictions[0]['emotion']
        emotions = {key: predictions.get(key,None) for key in predictions }
        emotions['dominant_emotion'] = max(predictions, key=predictions.get)
    else:
        emotions = {'anger': None, 'disgust': None, 'fear': None, 'joy': None, 'sadness': None, 'dominant_emotion': None}
    return emotions


    