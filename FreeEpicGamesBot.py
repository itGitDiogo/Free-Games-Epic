import subprocess
import pyautogui
import time

time.sleep(3)

epicProcess = subprocess.run('D:\Games\EPIC\Epic Games\Launcher\Portal\Binaries\Win32\EpicGamesLauncher.exe')

onHomeScreen = False
onGameScreen = False
onThePurchaseScreen = False
closeScreen = False

while onHomeScreen == False: 
    gameButtonLocation = pyautogui.locateCenterOnScreen('img/free.png', confidence= 0.7)
    print(gameButtonLocation)
    if gameButtonLocation == None:
        pyautogui.scroll(-400)
    else:
        print(gameButtonLocation)
        pyautogui.moveTo(gameButtonLocation)
        pyautogui.click()  
        onHomeScreen = True

while onGameScreen == False:
    cartButtonLocation = pyautogui.locateCenterOnScreen('img/addOnCart.png', confidence= 0.7)
    if cartButtonLocation != None:
        pyautogui.moveTo(cartButtonLocation.x,cartButtonLocation.y-50)
        pyautogui.click()
        onGameScreen = True

while onThePurchaseScreen == False:
    purchaseButtonLocation = pyautogui.locateCenterOnScreen('img/purchase.png', confidence= 0.7)
    if purchaseButtonLocation != None:
        pyautogui.moveTo(purchaseButtonLocation)
        pyautogui.click()
        onThePurchaseScreen = True

while closeScreen == False:
    xButtonLocation = pyautogui.locateCenterOnScreen('img/closeApp.png', confidence= 0.7)
    print(xButtonLocation)
    if xButtonLocation != None:
        pyautogui.moveTo(xButtonLocation.x+40,xButtonLocation.y)
        time.sleep(3)
        pyautogui.click()
        closeScreen = True


	




