"""
This module is for translating text using IBM Watson translator

FUNCTIONS:
    englishToFrench
    frenchToEnglish
"""
#import json
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)

language_translator.set_service_url(url)

def englishToFrench(englishText):
    """
    This function returns Franch text after translating the English text input
    """
    if englishText is None:
        return None
    if len(englishText) == 0:
        return ''
    translation = language_translator.translate(
    text=englishText,
    model_id='en-fr').get_result()
    return translation["translations"][0]["translation"]

def frenchToEnglish(frenchText):
    """
    This function returns English text after translating the French text input
    """
    if frenchText is None:
        return None
    if len(frenchText) == 0:
        return ''
    translation = language_translator.translate(
    text=frenchText,
    model_id='fr-en').get_result()
    return translation["translations"][0]["translation"]
