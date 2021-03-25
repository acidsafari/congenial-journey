# In this case they are explaining a speech to text service
# MORE INFORMATION ON THIS LINK https://cloud.ibm.com/apidocs/speech-to-text?code=python
# !pip install PyJWT==1.7.1 ibm_watson wget
#speech to text

#!pip install PyJWT==1.7.1 ibm_watson wget

from ibm_watson import SpeechToTextV1
import json
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

# To find out which URL to use, view the service credentials and paste the url here.
url_s2t = "https://api.eu-de.speech-to-text.watson.cloud.ibm.com/instances/8a0fc867-a69d-416b-b84c-0d181191c14f"
#You require an API key, and you can obtain the key on the Dashboard .
iam_apikey_s2t = "5pYfP1whofrdRhtNhVLKXvosurlIznyTZw61eaFt--4L"
# You create a Speech To Text Adapter object the parameters are the endpoint and API key.
authenticator = IAMAuthenticator(iam_apikey_s2t)
s2t = SpeechToTextV1(authenticator=authenticator)
s2t.set_service_url(url_s2t)
s2t
#Lets download the audio file that we will use to convert into text.
# I AM HAVING TROUBLE WITH THIS LINE - NOT RETRIEVING
!wget -O PolynomialRegressionandPipelines.mp3  https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/labs/Module%205/data/PolynomialRegressionandPipelines.mp3

filename='PolynomialRegressionandPipelines.mp3'

with open(filename, mode="rb")  as wav:
    response = s2t.recognize(audio=wav, content_type='audio/mp3')

#The attribute result contains a dictionary that includes the translation:
response.result
from pandas.io.json import json_normalize

json_normalize(response.result['results'],"alternatives")
response

#We can obtain the recognized text and assign it to the variable recognized_text:
recognized_text=response.result['results'][0]["alternatives"][0]["transcript"]
type(recognized_text)



# language translator

from ibm_watson import LanguageTranslatorV3

#The service endpoint is based on the location of the service instance
url_lt='https://api.eu-de.language-translator.watson.cloud.ibm.com/instances/c2d090d0-8e06-4f12-a68b-04f3a8b5be5a'
apikey_lt='7SRJS70C0dYVCio9ATg34medPPP6LOEl0quCk5LYMksN'
# API requests require a version parameter that takes a date in the format version=YYYY-MM-DD.
# This lab describes the current version of Language Translator, 2018-05-01
version_lt='2018-05-01'
#we create a Language Translator object language_translator:
authenticator = IAMAuthenticator(apikey_lt)
language_translator = LanguageTranslatorV3(version=version_lt,authenticator=authenticator)
language_translator.set_service_url(url_lt)
language_translator

#We can get a Lists the languages that the service can identify. The method Returns the language code.
# For example English (en) to Spanis (es) and name of each language.
from pandas.io.json import json_normalize

json_normalize(language_translator.list_identifiable_languages().get_result(), "languages")

#We can use the method translate this will translate the text. The parameter text is the text.
#Model_id is the type of model we would like to use use we use list the language .
#In this case, we set it to 'en-es' or English to Spanish. We get a Detailed Response object translation_response
translation_response = language_translator.translate(\
    text=recognized_text, model_id='en-es')
translation_response

translation=translation_response.get_result()
translation #The result is a dictionary.
#We can obtain the actual translation as a string as follows:
spanish_translation =translation['translations'][0]['translation']
spanish_translation
#We can translate back to English
translation_new = language_translator.translate(text=spanish_translation ,model_id='es-en').get_result()
#We can obtain the actual translation as a string as follows:
translation_eng=translation_new['translations'][0]['translation']
translation_eng

translation_response = language_translator.translate(\
    text=recognized_text, model_id='en-fr')
translation_response

translation=translation_response.get_result()
translation #The result is a dictionary.
#We can obtain the actual translation as a string as follows:
french_translation =translation['translations'][0]['translation']
french_translation

"""
OG - VIDEO
from ibm_watson import SpeechToTextV1 # this is a service they have
import json
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

url_s2t = 'https://api.eu-de.speech-to-text.watson.cloud.ibm.com'
# To find out which URL to use, view the service credentials and paste the url here
#this might change for another service
iam_apikey_s2t = '' # CAN'T FIND THE KEY

s2t = SpeechToTextV1(iam_apikey = iam_apikey_s2t, url = url_s2t)

filename = 'hello_this_is_python.wav'
with open(filename, mode = 'rb') as wav :
    response = s2t.recognize(audio = wav, content_type = 'audio/wav')

response.result() # this will generate a dictionary

{'result':[{'alternatives':[{'confidence':0.91, 'transcript': 'hello this is python'}], 'final':True}], 'result_index':0}

recognize_text = response.result()['results'][0]['alternatives'][0]['transcript']

# recognize_text : 'hello this is python'
"""
