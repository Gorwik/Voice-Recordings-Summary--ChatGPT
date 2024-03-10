# Folders paths for records, transcriptions, summarizes respectively
import os
from pathlib import Path

# API settings

# Api key for Deepgram
DG_API_KEY = os.getenv("DG_API_KEY")
# Api key for ChatGPT Client
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

RECORDS_FOLDER_PATH = Path(r"records")
TRANSCRIPTIOS_FOLDER_PATH = Path(r"transcriptions")
SUMMARIZES_FOLDER_PATH = Path(r"summarizes")

EXTENTIONS = {
    RECORDS_FOLDER_PATH: "mp3",
    TRANSCRIPTIOS_FOLDER_PATH: "txt",
    SUMMARIZES_FOLDER_PATH: "txt",
}

MAX_TOKENS = 4000
WORDS_TO_TOKENS_COEFFICIENT = 100 / 75

GENERAL_PROMPT = """By day you have been a journalist in a respected newsroom for more than 10 years. 
                    Your main task at work is to read statements, listen to eyewitness interviews of events. 
                    You then extract the most important information from them and present it in bullet points. 
                    You never leave out important details such as names or places of events, but you manage to leave out irrelevant details.
                    Below is a statement that you are to summarise descriptively step by step. Please ensure that your answer is in Markdown format.\n\n"""

SHORT_PROMPT = "Summarise the following text step by step."

IF_SHORT_PROMPT = True
PROMPT = SHORT_PROMPT if IF_SHORT_PROMPT else GENERAL_PROMPT

# PDF settings
INPUT_FOLDER = r"summarizes"
OUTPUT_FILE = r"summarize.pdf"
