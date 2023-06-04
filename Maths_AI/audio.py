import speech_recognition as sr

def aud():
    global temp
    r = sr.Recognizer()

    mic = sr.Microphone(device_index=0)

    with mic as source:
        r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source,timeout=8)
    try:
        temp=r.recognize_google(audio)
        try:
            #print("You have spoken: ",temp)
            return temp
        except:
            print("Sorry, Unable to understand.")
            aud()
    except:
        print("Sorry, Unable to hear.")
        aud()
