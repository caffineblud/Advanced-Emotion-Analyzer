"""
========================================
      Advanced Emotion Tone Analyzer
========================================

This program analyzes the emotional tone
of a sentence entered by the user.

Detected Emotions:
1. Happy
2. Sad
3. Angry
4. Neutral

Powered by HuggingFace Transformers
========================================
"""

from transformers import pipeline


class EmotionAnalyzer:

    def __init__(self):
        """
        Load the pre-trained emotion detection model.
        """
        print("\nLoading AI Emotion Model...\n")

        self.classifier = pipeline(
            task="text-classification",
            model="j-hartmann/emotion-english-distilroberta-base",
            top_k=None
        )

        # Mapping detailed emotions to simpler categories
        self.emotion_map = {
            "joy": "Happy",
            "sadness": "Sad",
            "anger": "Angry",
            "neutral": "Neutral",
            "fear": "Sad",
            "surprise": "Happy",
            "disgust": "Angry"
        }

    def analyze_emotion(self, text):
        """
        Analyze emotion from text.

        Parameters:
            text (str): User input sentence

        Returns:
            tuple:
                detected_emotion (str)
                detailed_results (list)
        """

        results = self.classifier(text)[0]

        # Get highest confidence emotion
        best_result = max(results, key=lambda item: item["score"])

        detected_emotion = self.emotion_map.get(
            best_result["label"].lower(),
            "Neutral"
        )

        return detected_emotion, results

    def display_results(self, emotion, results):
        """
        Display formatted emotion analysis results.
        """

        print("\n========== Analysis Result ==========")
        print(f"Detected Emotion : {emotion}")

        print("\nConfidence Scores:")
        print("-------------------------------------")

        for item in results:
            label = item["label"]
            score = item["score"] * 100

            print(f"{label.capitalize():<12} : {score:.2f}%")

        print("=====================================\n")


def main():
    """
    Main function of the program.
    """

    analyzer = EmotionAnalyzer()

    while True:

        user_input = input(
            "Enter a sentence (type 'exit' to quit): "
        )

        if user_input.lower() == "exit":
            print("\nProgram Closed Successfully.")
            break

        if not user_input.strip():
            print("Please enter a valid sentence.\n")
            continue

        emotion, results = analyzer.analyze_emotion(user_input)

        analyzer.display_results(emotion, results)


# Run Program
if __name__ == "__main__":
    main()
