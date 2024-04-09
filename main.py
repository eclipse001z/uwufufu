from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from multiprocessing import Pool
import time

def start_game(game_id, rounds, winner):
    driver = webdriver.Chrome()
    driver.get(f'https://new.uwufufu.com/quiz/worldcup/{game_id}/rank')
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="worldCupRankPage"]/div/div/main/div/section[1]/div/div'))).click() 
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="content-container"]/div[3]/div/div[2]/div/div/div[2]/div/a'))).click()

    for i in range(rounds):
        a = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="trigger-left"]/div/div/div/a/div[2]/div/p'))).text
        if a == winner:
            WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="trigger-left"]'))).click() # Red - Left
        else:
            WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="trigger-right"]'))).click() # Blue - Right
        time.sleep(2)
    driver.quit()

if __name__ == '__main__':
    print("Enter the game id")
    game_id = input()

    print("Amount of games/instances (Really Unstable with alot)")
    print("Enter The amount of games:")
    games = int(input())
    print(games)

    print("Rounds are 2, 4, 8, 16, 32, 64, 128, 256, 512")
    print("Enter the amount of rounds")
    rounds = (int(input()) -1)
    print(rounds)

    print('Who do you want to win (Spell Correctly)')
    print('Enter the Winner')
    winner = input()
    print(winner)

    with Pool(processes=games) as pool:
        pool.starmap(start_game, [(game_id, rounds, winner)] * games)
