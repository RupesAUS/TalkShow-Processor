# Python program to process aws transcription result, and provide a more comprehensible text output 
# Rupert Hu 2022

from functions.filemanip import readJsonTranscript

data = readJsonTranscript('asrOutput.json')

print(data)