import subprocess
import pyautogui

subprocess.run('D:\Games\EPIC\Epic Games\Launcher\Portal\Binaries\Win32\EpicGamesLauncher.exe')

onHomeScreen = False
onGameScreen = False
onThePurchaseScreen = False

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





