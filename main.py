import pyttsx3
import speech_recognition as sr
import os
import time
import datetime
from fuzzywuzzy import fuzz
import wikipedia
from translate import Translator
import random
import webbrowser
wikipedia.set_lang("ru")
opts = {
    "alias": ('никс', 'nyx', 'микс', 'некс', 'мекс',
              'nix', 'mix', 'myx'),
    "tbr": ('скажи', 'расскажи', 'покажи', 'сколько', 'произнеси','переведи'),
    "cmds": {
        "ctime": ('текущее время', 'сейчас времени', 'который час'),
        "radio": ('включи музыку', 'воспроизведи радио', 'включи радио'),
        "stupid1": ('расскажи анекдот', 'рассмеши меня', 'ты знаешь анекдоты'),
        "tranc":('переведи','переведи слово','выполни перевод','слово')
    }
}
def translating(cmd):
    lang='ru'
    tlang='en'
    translator=Translator(from_lang=lang, to_lang=tlang)
    print(translator.translate(cmd))
    wrd=str(translator.translate(cmd))
    return wrd


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices') #даёт подробности о текущем установленном голосе
engine.setProperty('voice', voices[0].id)  # 0-мужской , 1-женский

def speak(audio):
    engine.say(audio)
    engine.runAndWait() #Без этой команды мы не услышим речь

if __name__=="__main__" :
    speak(' Я Никс, ваш персональный помошник!')

def wishme():
    hour = int(datetime.datetime.now().hour)


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Бодрого утречка!")

    elif hour >= 12 and hour < 18:
        speak("Добрый денечек!")

    else:
        speak("Добрейший вечерок!")


r = sr.Recognizer()
m= sr.Microphone()
def takeCommand():
    #Принимает на входе аудио от микрофона, возвращает строку с нашими словами

     with m as source:
         print("Listening...")
         r.pause_threshold = 1
         audio = r.listen(source)
         try:
             voice = r.recognize_google(audio, language="ru-RU").lower()
             print("[log] Распознано: " + voice)
             if voice.startswith(opts["alias"]):
                 cmd = voice

                 for x in opts['alias']:
                     cmd = cmd.replace(x, "").strip()

                 for x in opts['tbr']:
                     cmd = cmd.replace(x, "").strip()

                 # распознаем и выполняем команду
                 cmd = recognize_cmd(cmd)
                 execute_cmd(cmd['cmd'],voice)
         except Exception as e:# будет выведено, если речь не распознаётся
                return 'None'  # вернётся строка "Пусто"

def recognize_cmd(cmd):
    RC = {'cmd': '', 'percent': 0}
    for c, v in opts['cmds'].items():

        for x in v:
            vrt = fuzz.ratio(cmd, x)
            if vrt > RC['percent']:
                RC['cmd'] = c
                RC['percent'] = vrt

    return RC

def execute_cmd(cmd,voice):
    if cmd == 'ctime':
        # сказать текущее время
        now = datetime.datetime.now()
        speak("Сейчас " + str(now.hour) + ":" + str(now.minute))

    elif cmd == 'stupid1':
        # рассказать анекдот
        random_item = random.SystemRandom().choice(["Данный анекдот доступен для прослушивания только натуралам", "Сидят три девушки в баре. Первая говорит: -Вот я своему мужу минет делаю, а у него яйца холодные. Вторая говорит: - Я тоже когда своему минет делаю яйца у него холодные. Третья молчит. Проходит день, они снова встречаются в баре, а у третьей всё лицо разбито. У нее спрашивают: - Что с тобой случилось?! - Я своему мужу минет делала, а яйца у него теплые. Вот я ему и говорю, почему это у всех мужиков холодные, а у тебя теплые?", "Дотер приезжает на планету девственниц, теперь это планета девственниц и девственника, приезжает второй дотер,...теперь это планета девственниц"])
        speak(random_item)
    elif cmd == 'tranc':
        # переводчик
        res_str = voice.replace('никс переведи слово','никс переведи')
        C=translating(res_str)
        speak(C)
    else:
        print('Команда не распознана, повторите!')
wishMe()
while True:
    takeCommand()
    #if 'никс' or 'mix' or 'nyx' or 'микс' in query:
     #   query = query.replace('никс', "")
    ###  query = query.replace('mix', "")
      # query = query.replace('nyx', "")
      #  query = query.replace('микс', "")
       # if 'включи музыку' in query:
      #              query = takeCommand().lower()
      #              speak('Включаю ваше любимое')
       #             music_dir = 'E:\olbum'
          #          songs = os.listdir(music_dir)
       #             print(songs)
        #            os.startfile(os.path.join(music_dir, songs[1]))
          #          query = takeCommand().lower()
       # elif 'сколько время' in query:
          #          strTime = datetime.datetime.now().strftime("%H:%M:%S")
         #           speak(f"Сейчас {strTime}")
        #            query = takeCommand().lower()
       # elif 'расскажи анекдот' in query:
       #             speak('Идет медведь по лесу, видит дом горит, зашел, сгорел')
       # elif 'переведи' in query:
          #          query = query.replace("переведи", "")
        #            speak(translating())
       # elif 'википедия' in query:
         #   results = wikipedia.summary(query, sentences=2)
        #    print(query)
       #     speak(results)
       # elif 'хлам' or 'пусто' in query:
            #       speak('Я не знаю как на это отвечать')


