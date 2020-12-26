import pyautogui

# pyautogui.typewrite(['win'])
# pyautogui.typewrite('Chrome')
# pyautogui.typewrite(['enter'])

# pyautogui.moveTo(1077, 247, duration= 2)

pyautogui.hotkey('ctrl', 'p')
pyautogui.rightClick(1077, 247, duration = 1)
pyautogui.hotkey('ctrl', 'a')
pyautogui.hotkey('ctrl', 'c')
pyautogui.hotkey('ctrl', 't')
pyautogui.typewrite('www.gmail.com')
pyautogui.typewrite(['enter'])
pyautogui.rightClick(75, 173, duration = 5)
pyautogui.moveTo(1110, 373, duration = 5)
pyautogui.typewrite('shahnawazmlk3@gmail.com')
pyautogui.typewrite(['tab'])
pyautogui.moveTo(1110, 773, 1)
pyautogui.typewrite(['tab'])
pyautogui.typewrite(['tab'])
pyautogui.hotkey('ctrl', 'v')
pyautogui.hotkey('ctrl', 'enter')
