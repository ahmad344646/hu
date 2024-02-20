# heroku profitcentr
from apscheduler.schedulers.background import BackgroundScheduler
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from github import Github
import requests
import speech_recognition as sr
from pydub import AudioSegment
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time
import json
import os
from flask import Flask
import threading
import random
import re



def download_audio(url, output_file_path):
    response = requests.get(url, stream=True)

    if response.status_code == 200:
        with open(output_file_path, "wb") as f:
            for chunk in response.iter_content(chunk_size=128):
                f.write(chunk)
        print("Audio downloaded successfully.")
    else:
        print(f"Failed to download audio. Status code: {response.status_code}")


def convert_mp3_to_wav(mp3_file_path, wav_file_path):
    audio = AudioSegment.from_mp3(mp3_file_path)
    audio.export(wav_file_path, format="wav")

def audio_to_text(wav_file_path):
    recognizer = sr.Recognizer()
    with sr.AudioFile(wav_file_path) as audio_file:
        recognizer.adjust_for_ambient_noise(audio_file)
        try:
            audio_data = recognizer.record(audio_file)
            text = recognizer.recognize_google(audio_data)
            return text
        except sr.UnknownValueError:
            print("Google Web Speech API could not understand audio")
        except sr.RequestError as e:
            print(f"Could not request results from Google Web Speech API; {e}")


account_number = os.getenv("ACCOUNT_NUMBER")
app = Flask(__name__)

@app.route('/')
def hello():
    return "i am flask app "

port = int(os.environ.get("PORT", 5000))

def flask_thread():
    app.run(host="0.0.0.0", port=port)

def running():
    # your existing running() function
    # Use ChromeOptions directly
    
    chrome_options = Options()
    #chrome_options.add_argument(f'--proxy-server={proxy_with_port}')
    #chrome_options.add_argument(f'--user-agent={test_ua}')
    chrome_options.add_argument('--headless')
    #chrome_options.add_extension('./2.crx')
    chrome_options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36")
    chrome_options.add_argument('--disable-gpu')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    
    # Use context manager to handle the WebDriver instance
    with webdriver.Chrome(options=chrome_options) as driver1:
        driver1.get("https://seo-task.com/register")
        #driver1.maximize_window()
        driver1.set_window_size(1280, 775)
        print("Please wait...")
        WebDriverWait(driver1, 1).until(
                        EC.element_to_be_clickable((By.NAME, 'login'))).send_keys("afedehtjg")
        WebDriverWait(driver1, 1).until(
                        EC.element_to_be_clickable((By.NAME, 'email'))).send_keys("es.dgtr.45@gmail.com")
        WebDriverWait(driver1, 1).until(
                        EC.element_to_be_clickable((By.NAME, 'password'))).send_keys("ahmaD4764346@")
        time.sleep(1)
        actions = webdriver.ActionChains(driver1)
        actions.send_keys(Keys.TAB)
        actions.perform()
        time.sleep(0.5)

        actions = webdriver.ActionChains(driver1)
        actions.send_keys(Keys.ENTER)
        actions.perform()
        time.sleep(4)


        
        actions = webdriver.ActionChains(driver1)
        actions.send_keys(Keys.TAB)
        actions.perform()
        time.sleep(0.5)

        actions = webdriver.ActionChains(driver1)
        actions.send_keys(Keys.ENTER)
        actions.perform()
        time.sleep(2)

        actions = webdriver.ActionChains(driver1)
        actions.send_keys(Keys.TAB)
        actions.perform()
        time.sleep(0.5)
        actions = webdriver.ActionChains(driver1)
        actions.send_keys(Keys.TAB)
        actions.perform()
        time.sleep(0.5)

        actions = webdriver.ActionChains(driver1)
        actions.send_keys(Keys.ENTER)
        actions.perform()
        time.sleep(2)



        driver1.switch_to.window(driver1.window_handles[1])
        url = driver1.current_url
        output_file_path = "audio.mp3"
        download_audio(url, output_file_path)
        time.sleep(1)
        mp3_file_path = "./audio.mp3"
        wav_file_path = "./audio.wav"
        convert_mp3_to_wav(mp3_file_path, wav_file_path)
        result = audio_to_text(wav_file_path)
        print("Text from audio:", result)
        driver1.close()
        driver1.switch_to.window(driver1.window_handles[0])
        v=7
        d=1
        while d < v:
            actions = webdriver.ActionChains(driver1)
            actions.send_keys(Keys.TAB)
            actions.perform()
            time.sleep(0.3)
            d=d+1
        
        time.sleep(1)

        actions = webdriver.ActionChains(driver1)
        actions.send_keys(result)
        actions.perform()
        time.sleep(1)

        v=6
        d=1
        while d < v:
            actions = webdriver.ActionChains(driver1)
            actions.send_keys(Keys.TAB)
            actions.perform()
            time.sleep(0.3)
            d=d+1
        time.sleep(1)
        actions = webdriver.ActionChains(driver1)
        actions.send_keys(Keys.ENTER)
        actions.perform()
        time.sleep(3)


        WebDriverWait(driver1, 1).until(
                        EC.element_to_be_clickable((By.XPATH, '//*[@id="form_register"]/form/button'))).click()

        time.sleep(4)
        print("register success")
        # with open(f'{account_number}.json', 'r') as f:
        #     cookies = json.load(f)
        # for cookie in cookies:
        #     driver1.add_cookie(cookie)
        


def sdsf():
    while True:
        try:
            running()
        except:
            continue





# Start Flask in a separate thread
flask_thread = threading.Thread(target=flask_thread)
flask_thread.start()



flask_thread1 = threading.Thread(target=sdsf)
flask_thread1.start()






if __name__ == '__main__':
    # This block will only be executed when the script is run directly, not when imported
    try:
        while True:
            pass  # Keep the main thread alive
    except KeyboardInterrupt:
        scheduler.shutdown()


