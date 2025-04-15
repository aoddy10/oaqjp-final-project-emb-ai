import requests
import json
import operator

def emotion_detector(text_to_analyse):
    # define the require parameter
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    myobj = { "raw_document": { "text": text_to_analyse } }

    # send request to server, then return the result
    response = requests.post(url, json = myobj, headers=header)

    # parsing the JSON reqponse
    formatted_response = json.loads(response.text)

    # if the response status code is 200, extract the emotion and return dict
    if response.status_code == 200:
        # extracting emotion from response
        emotion = formatted_response['emotionPredictions'][0]['emotion']
        # finding the highest score
        highest_emotion = max(emotion.items(), key=operator.itemgetter(1))
        
        resp = {
            "anger": emotion['anger'],
            "disgust": emotion['disgust'],
            "fear": emotion['fear'],
            "joy": emotion['joy'],
            "sadness": emotion['sadness'],
            "dominant_emotion": highest_emotion[0]
        }
    # if the response status code is 400, return dict with value None for all key
    elif response.status_code == 400:
        resp = {
            "anger": None,
            "disgust": None,
            "fear": None,
            "joy": None,
            "sadness": None,
            "dominant_emotion": None
        }

    return resp