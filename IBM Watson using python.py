#!/usr/bin/env python
# coding: utf-8

# In[2]:


pip install --upgrade ibm-watson


# In[11]:


pip install ibm-cloud-sdk-core


# In[21]:


from ibm_watson import SpeechToTextV1
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
iam_apikey_s2t = IAMAuthenticator('xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx')
s2t=SpeechToTextV1(authenticator=iam_apikey_s2t)
s2t.set_service_url("https://api.us-south.speech-to-text.watson.cloud.ibm.com/instances/xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
filename='whatstheweatherlike.wav'
with open(filename,mode="rb") as wav:
    response = s2t.recognize(audio=wav,content_type="audio/wav")
response.result


# In[22]:


recognized_text=response.result['results'][0]["alternatives"][0]["transcript"]
recognized_text


# In[33]:


apikey_lt = IAMAuthenticator('xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'')
language_translator=LanguageTranslatorV3(authenticator=apikey_lt,version="2018-05-01")
language_translator.set_service_url("https://api.us-south.language-translator.watson.cloud.ibm.com/instances/xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
language_translator.list_identifiable_languages().get_result()


# In[37]:


translation_response=language_translator.translate(text=recognized_text,model_id="en-es")
translation=translation_response.get_result()
translation


# In[40]:


spanish_translation = translation['translations'][0]["translation"]
spanish_translation


# In[50]:


translation_new1 = language_translator.translate(text=spanish_translation,model_id="es-en").get_result()
english_translation = translation_new1['translations'][0]["translation"]
english_translation


# In[51]:


translation_new2 = language_translator.translate(text=english_translation,model_id="en-te").get_result()
telugu_translation = translation_new2['translations'][0]["translation"]
telugu_translation


# In[ ]:
