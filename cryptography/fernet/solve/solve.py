from cryptography.fernet import Fernet

key = b'SM_jawmHkB0O3n2KSYv-y19q7MarIArBN0F9b08ea7U='
f = Fernet(key)

enc = b'gAAAAABjzgA5ETZjZMeQsWHSYmhS8aZVDUmDf3iXmEg0neZG3dFSDiJZie55-XRwSI3ezhPAKsNB5knaDIc0Bu5kpMR3cMFt8xtBF5-tQbQMcwUn8vtLeDY='
flag = f.decrypt(enc)
print(flag)
