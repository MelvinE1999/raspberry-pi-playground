import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522


def readInfoFromRfid(reader) -> bool:
    was_read = False
    
    try:
        print("\nNow place your tag to read")
        id, text = reader.read()
        print(f"\nTag ID: {id} \n Text: {text} \n")
        was_Read = True
    finally:
        return was_Read


def writeInfoToRfid(reader, text:str) -> bool:
    was_written_to = False
    
    try:
        print("\nNow place your tag to write")
        reader.write(text)
        print(f"\n{text} was written to tag\n")
        was_written_to = True
    finally:
        return was_written_to


def getSelection() -> str:
    while True:
        selection = input("\nWould you like to write or read to your tag?\n").lower()
        if selection in ["write", "read"]:
            return selection


if __name__ == "__main__":
    reader = SimpleMFRC522()
    GPIO.setwarnings(False)
    
    while True:
        selection = getSelection()
        if selection == "write":
            text = input("What would you like to be written on the tag:\n")
            writeInfoToRfid(reader,text)
        else:
            readInfoFromRfid(reader)
        
        continue_flag_temp = input("If you want to continue then type in y or yes. All other will terminate program.\n")
        if continue_flag_temp.lower() not in ["y","yes"]:
            break
    
    GPIO.cleanup()
    
    
    
    