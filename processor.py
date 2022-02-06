# Python program to process aws transcription result, and provide a more comprehensible text output 
# Rupert Hu 2022

from functions.filemanip import *

data = readJsonTranscript('asrOutput.json')

printJson(data['results']['items'][:10])