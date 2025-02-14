from gpiozero import LED
from time import sleep

led = LED("GPIO17")
MORSECODE_DICT = {
    'A':'.-', 'B':'-...',
    'C':'-.-.', 'D':'-..', 'E':'.',
    'F':'..-.', 'G':'--.', 'H':'....',
    'I':'..', 'J':'.---', 'K':'-.-',
    'L':'.-..', 'M':'--', 'N':'-.',
    'O':'---', 'P':'.--.', 'Q':'--.-',
    'R':'.-.', 'S':'...', 'T':'-',
    'U':'..-', 'V':'...-', 'W':'.--',
    'X':'-..-', 'Y':'-.--', 'Z':'--..',
    '1':'.----', '2':'..---', '3':'...--',
    '4':'....-', '5':'.....', '6':'-....',
    '7':'--...', '8':'---..', '9':'----.',
    '0':'-----', ', ':'--..--', '.':'.-.-.-',
    '?':'..--..', '/':'-..-.', '-':'-....-',
    '(':'-.--.', ')':'-.--.-'
    }

def convert_to_morsecode(phrase):
    morsecode = ''
    
    
    for letter in phrase:
        if letter != ' ':
            morsecode += MORSECODE_DICT[letter.upper()] + ' '
        else:
            morsecode += ' '

    return morsecode
    
    
def display_morsecode(morsecode: str):
    
    while True:
        for m in morsecode:
            print(m)
            if m == " ":
                sleep(1)
            elif m == ".":
                led.on()
                sleep(1)
                led.off()
                sleep(1)
            else:
                led.on()
                sleep(3)
                led.off()
                sleep(1)
    
if __name__ == '__main__':
    phrase = input("Enter a phrase to be translated to morse code on loop?\n")
    try:
        morsecode = convert_to_morsecode(phrase)
        print("hi")
        display_morsecode(morsecode)
    except:
        print("Ending Program")