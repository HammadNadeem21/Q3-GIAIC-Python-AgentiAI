import time
# For Sound
import winsound

def countdown():
    seconds = int(input("Enter the time in seconds: "))

    while seconds:
        mins, secs = divmod(seconds, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end="\r")
        time.sleep(1)
        seconds -= 1

    print("Timer Completed!")

    # For Sound
    duration = 900
    freq = 500
    winsound.Beep(freq, duration)
    

if __name__ == '__main__':
    countdown()