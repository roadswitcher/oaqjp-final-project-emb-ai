'''This application displays a text interface on port 5000 to process text input using IBM Watson NLP technology.
'''
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)

@app.route("/")
def render_index_page():
    '''This function renders a default HTML index page as part of a flask application'''
    return render_template("index.html")

@app.route("/emotionDetector")
def get_emotion_response():
    ''' This code takes HTML text input and displays detected emotions by passing the data to the IBM Watson NLP libraries.
    '''
    text_to_analyze = request.args.get(
        "textToAnalyze",
    )
    response = emotion_detector(text_to_analyze)

    if response["dominant_emotion"] is None:
        return "Invalid text! Please try again!"

    emotions = ", ".join(
        [
            f"'{key}': {value}"
            for key, value in response.items()
            if key != "dominant_emotion"
        ]
    )
    dominant_emotion = response.get("dominant_emotion", "No dominant emotion detected")
    formatted_response = (
        f"For the given statement, the system response is {emotions}. "
        f"The dominant emotion is {dominant_emotion}."
    )

    return formatted_response

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
