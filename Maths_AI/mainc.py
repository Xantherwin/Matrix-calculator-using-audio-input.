import speech_recognition as sr
from text2speech import ai

global temp
def m_aud():
    r = sr.Recognizer()

    mic = sr.Microphone(device_index=0)

    with mic as source:
        r.adjust_for_ambient_noise(source, duration=1)
        print("Speakup your operation: ")
        ai("Speakup your operation")
        audio = r.listen(source,timeout=5)
    try:
        temp=r.recognize_google(audio)
        try:
            print("You have spoken:",temp)
            return temp
        except:
            print("Sorry, Unable to understand.")
            m_aud()
    except:
        print("Sorry, Unable to hear.")
        m_aud()
