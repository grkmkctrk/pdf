import pyscreenshot as ImageGrab
import time
import pyautogui

print("program başlayacak ilgili sayfaya geçiş yapın")
    
for i in range(0,10):
    print(f"son {10-i}")
    time.sleep(1)
    

# part of the screen
pyautogui.KEYBOARD_KEYS

for sayfa in range(0,428):    
    im = ImageGrab.grab(bbox=(413, 0, 1366-410, 745))  # X1,Y1,X2,Y2
    im.save(f"her_yonuyle_fpga_ve_vhdl_{sayfa+1}.png")
    time.sleep(2)
    pyautogui.press("space")
    