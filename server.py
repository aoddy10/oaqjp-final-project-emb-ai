'''
This application use for emotion detection and it is the final project
'''

from flask import Flask, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detection App")


@app.route('/emotionDetector')
def detect_emotion():
    '''
        This function handle request by get the text from request args
        Then send to IBM Watson NPL to get the emotion detection,
        and return the result of dominant emotion.
    '''

    # check request text with IBM Watson NLP
    text_to_check = request.args.get("textToCheck")
    response = emotion_detector(text_to_check)

    # check if the dominant emotion is None, return invalid text
    if response['dominant_emotion'] is None:
        return "Invalid text! Please try again!"

    # create the emotion result list
    emotion_result = ", ".join(
        [f"'{k}': {v}" for k, v in response.items() if k != "dominant_emotion"]
    )

    # return the format text
    return (
        f"For the given statement, the system response is {emotion_result}. "
        f"The dominant emotion is {response['dominant_emotion']}."
    )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
