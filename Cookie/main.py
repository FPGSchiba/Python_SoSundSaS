import os
import time
import threading
import pyperclip

from pynput.mouse import Controller
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from pynput.keyboard import KeyCode, Listener

chrome_options = webdriver.ChromeOptions()
driver = webdriver.Chrome(ChromeDriverManager().install())

start_stop_key = KeyCode(char='v')
stop_key = KeyCode(char='b')
save_file = os.path.join(os.getcwd(), 'game.txt')


def load_game():
    if os.path.isfile(save_file):
        driver.find_element_by_id('prefsButton').click()
        ActionChains(driver).key_down(Keys.CONTROL).key_down('o').perform()
        with open(save_file, 'r+', encoding='utf-8') as file:
            data = file.read()
        pyperclip.copy(data)
        ActionChains(driver).key_down(Keys.CONTROL).key_down('v').perform()
        driver.find_element_by_id('promptOption0').click()
        driver.find_element_by_id('prefsButton').click()


def save_game():
    ActionChains(driver).key_down(Keys.CONTROL).key_down('s').perform()
    time.sleep(1)
    game_save = driver.execute_script("return window.localStorage;")['CookieClickerGame']
    with open(save_file, 'w+', encoding='utf-8') as file:
        file.write(game_save)


driver.get("https://orteil.dashnet.org/cookieclicker/")
time.sleep(3)
driver.find_element_by_id('langSelect-EN').click()
time.sleep(5)

load_game()


class ClickMouse(threading.Thread):
    def __init__(self):
        super(ClickMouse, self).__init__()
        self.running = False
        self.element = driver.find_element_by_id('bigCookie')
        self.program_running = True
        load_game()

    def start_clicking(self):
        self.running = True

    def stop_clicking(self):
        self.running = False

    def exit(self):
        self.stop_clicking()
        save_game()
        self.program_running = False

    def run(self):
        while self.program_running:
            while self.running:
                self.element.click()
                time.sleep(0.00001)
            time.sleep(0.1)


mouse = Controller()
click_thread = ClickMouse()
click_thread.start()
print("Ready to click...")


def on_press(key):
    if key == start_stop_key:
        if click_thread.running:
            click_thread.stop_clicking()
        else:
            click_thread.start_clicking()
    elif key == stop_key:
        click_thread.exit()
        listener.stop()
        driver.quit()


with Listener(on_press=on_press) as listener:
    listener.join()
