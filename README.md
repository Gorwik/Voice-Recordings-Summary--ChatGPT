# Voice Recordings Summary - ChatGPT


## General Information
Do you have that one friend who always sends voice recordings? Me too. All you have to do is put the recordings in the appropriate [folder](https://github.com/Gorwik/Voice-Recordings-Summary--ChatGPT/tree/master/records). The app will transcribe the given audio files, summarise them and finally save this as a PDF.


## Tools Used

* [ChatGPT API](https://img.shields.io/badge/ChatGPT-API)
* [Deepgram API](https://img.shields.io/badge/Deepgram-API)


### Requirements:
- Python version 3.11
- Account and API_KEY on [OpenAI](https://platform.openai.com/docs/overview)
- Account and API_KEY on [Deepgram](https://deepgram.com/)

### To run the application:
1. In root folder create .venv environment.  
``
python -m venv openai-env
``
1. Activate it.  
On Windows:  
``
openai-env\Scripts\activate
``  
On Unix or MacOS:  
``
source openai-env/bin/activate
``
1. Install dependencies included in [requirements.txt](https://github.com/Gorwik/Voice-Recordings-Summary--ChatGPT/blob/master/requirements.txt). 

``
pip install -r requirements.txt
``

1. Set up API keys.  
On Windows:  
``
setx OPENAI_API_KEY "your-openai-key-here"
setx DG_API_KEY "your-deepgram-key-here"
``  
On Unix or MacOS:  
``
export OPENAI_API_KEY='your-openai-key-here'
export DG_API_KEY='your-deepgram-key-here'
``

1. Run main.  
``
python ./main.py
``  <br>
Don't forget to add your records to the [records](https://github.com/Gorwik/Voice-Recordings-Summary--ChatGPT/tree/master/records) folder.
