"""
This module is responsible for handling voice commands using speech recognition
and spacy.
"""
import spacy
import speech_recognition as sr

from api.gpt_chat import chat_gpt, chat_gpt_custom
from api.graph_api import (create_new_appointment, get_emails,
                           get_next_appointment, send_email_with_attachments,
                           user_object_id)
from api.vin_decoder import decode_vin, parse_vin_response
from audio.audio_output import tts_output
from config import GRAPH_EMAIL_ADDRESS
from utils.commands import ELM327_COMMANDS, voice_commands
from utils.serial_commands import (process_data, send_command,
                                   send_diagnostic_report)

nlp = spacy.load("en_core_web_lg")


def get_similarity_score(text1, text2):
    """
    Compute the similarity score between two texts using spacy nlp pipeline.

    Args:
        text1 (str): The first text to compare.
        text2 (str): The second text to compare.

    Returns:
        float: The similarity score between the two texts.
    """
    doc1 = nlp(text1)
    doc2 = nlp(text2)
    return doc1.similarity(doc2)


def recognize_command(text, commands):
    """
    Recognizes a command from the given text.

    Args:
        text (str): The input text to recognize the command from.
        commands (list): A list of available commands.

    Returns:
        str: The recognized command if found, otherwise None.
    """
    if text is None:
        return None

    max_similarity = 0
    best_match = None

    for command in commands:
        similarity = get_similarity_score(text.lower(), command)

        if similarity > max_similarity:
            max_similarity = similarity
            best_match = command

    if max_similarity > 0.7:  # You can adjust this threshold
        return best_match
    else:
        return None


def recognize_speech():
    """
    Recognizes speech using the default microphone as the audio source.

    Returns:
        str: The recognized text if successful, otherwise None.
    """
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source, duration=2)
        print("Listening...")
        try:
            audio = recognizer.listen(source, timeout=10, phrase_time_limit=30)
        except sr.WaitTimeoutError:
            print("Timeout: No speech detected")
            return None
    try:
        text = recognizer.recognize_google(audio)
        print(f"You said: {text}")
        return text
    except sr.UnknownValueError:
        print("Could not understand audio")
        return None
    except sr.RequestError as request_error:
        print(f"Could not request results; {request_error}")
        return None
