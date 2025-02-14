import Keypad
from LCD1602 import CharLCD1602
from time import sleep

ROWS = 4
COLS = 4
keys =  [   '1','2','3','A',
            '4','5','6','B',
            '7','8','9','C',
            '*','0','#','D'     ]
rowsPins = [18, 23, 24, 25]
colsPins = [10, 22, 27, 17]

lcd1602 = CharLCD1602() 

def loop():
    lcd1602.init_lcd()
    keypad = Keypad.Keypad(keys,rowsPins,colsPins,ROWS,COLS)
    keypad.setDebounceTime(50)
    password = ""
    was_password_checked = False
    input_display(0)
    while(True):
        key = keypad.getKey()
        if(key != keypad.NULL):
            if was_password_checked:
                was_password_checked = False
                password = ""
                input_display(0)
                continue
            
            password += key
            input_display(len(password))
                
            if len(password) == 4:
                was_password_checked = access_display(password)
            
                
    
def input_display(digits: int):
    lcd1602.clear()
    lcd1602.write(0, 0, 'Enter Password:' )
    lcd1602.write(0, 1,'      ' + '*' * digits )
    sleep(1)
    
def access_display(password: str):
    correct_password = "1999"
    lcd1602.clear()
    if correct_password == password:
        lcd1602.write(0, 0, 'Access Granted!!!' )
        lcd1602.write(0, 1, 'Good Job')
    else:
        lcd1602.write(0, 0, 'Access Denied' )
        lcd1602.write(0, 1, 'Try Again')
    
    sleep(1)
    return True
    
def destroy():
    lcd1602.clear()
        
if __name__ == '__main__':     # Program start from here
    print ("Program is starting ... ")
    try:
        loop()
    except KeyboardInterrupt:  # When 'Ctrl+C' is pressed, the child program destroy() will be  executed.
        destroy()
        print("Ending program")