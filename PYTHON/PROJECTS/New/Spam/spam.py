import pyautogui
import pyperclip
import random
import time

msg = input('Spam messages: ').split(" || ")
n = int(input('So lan spam: '))
m = float(input('Thoi gian delay: '))
print('Chuan bi!')
for i in range(5, 0, -1):
    print(i, end='...', flush='True')
    time.sleep(1)
print('Bat dau!')

for i in range(n):
    pyperclip.copy(random.choice(msg))
    pyautogui.hotkey('ctrl', 'v')
    pyautogui.press('enter')
    time.sleep(m)
