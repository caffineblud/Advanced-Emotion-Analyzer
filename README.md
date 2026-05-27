# Advanced Emotion Tone Analyzer
**An AI-powered Python application that analyzes the emotional tone of user-entered sentences using Hugging Face Transformers and NLP models.**
**The program can detect emotions such as:**
* Happy
* Sad
* Angry
* Neutral
*It also displays confidence scores for multiple detected emotions.*
## Features:
* AI-based emotion detection :)
* Uses Hugging Face Transformers
* Confidence score analysis
* Clean object-oriented structure
* Interactive command-line interface
* Handles multiple emotions intelligently
## Technologies Used:
*Python*
*Transformers*
*PyTorch*
*NLP (Natural Language Processing)*
## Installation
1. Clone the Repository
```bash
git clone https://github.com/your-username/emotion-tone-analyzer.git
```
2.Navigate to project folder
```command
cd emotion-tone-analyzer
```
3. intall required libraries
```bash

pip install transformers torch
```
## Project Structure:
```text
emotion-tone-analyzer/
│
├── emotion_analyzer.py
├── README.md
```
## How to Run:
```bash
python emotion_analyzer.py
```
## Sample usage:
```text
========================================
      Advanced Emotion Tone Analyzer
========================================

Loading AI Emotion Model...

Enter a sentence (type 'exit' to quit): I finally achieved my dream!

========== Analysis Result ==========
Detected Emotion : Happy

Confidence Scores:
-------------------------------------
Joy          : 94.82%
Neutral      : 2.11%
Surprise     : 1.56%
Sadness      : 0.71%
=====================================
```
## Example Emotions:
Input Sentence-----------------Detected Emotion
*"I am feeling amazing today!" - Happy*
*"Nobody understands me." - Sad*
*"I hate this situation!" - Angry*
*"I went to school today." - Neutral*
## Future Improvements:
* GUI version using Tkinter or PyQt
* Speech emotion detection
* Multilingual support
* Web application deployment
* Emotion visualization charts
## Author:
***Developed by Yash Kr Singh***
## License:
*This project is open-source and available under the MIT License.*
