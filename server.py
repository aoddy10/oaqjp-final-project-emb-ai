from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detection App")


@app.route('/emotionDetector')
def detect_emotion():
    # check request text with IBM Watson NLP
    text_to_check = request.args.get("textToCheck")
    response = emotion_detector(text_to_check)

    # check if the dominant emotion is None, return invalid text
    if response['dominant_emotion'] is None:
        return "Invalid text! Please try again!"
    else:
        # create the emotion result list
        emotion_result = ", ".join([f"'{k}': {v}" for k, v in response.items() if k != "dominant_emotion"])
        # return the format text
        return "For the given statement, the system response is {}. The dominant emotion is {}.".format(emotion_result, response["dominant_emotion"])

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)