# CyberSecTools
Creating my own personal tools as a learning experience.

# Keylogger
Current implementation utilises the pynput library to capture key presses to the console.
Currently also captures what the focused window is for Windows operating systems.

Usage: python3 KeyLogger.py [Options]

- Once running use F1 to stop the listener
- Options are:
    - -d --delay: sets the file writing delay e.g. 5 would update the file every 5 seconds.
    - -f --filename: sets where the data will be saved.
    - -v --version: prints out the current version.
# Miscellaneous

## Auto Clicker
Very basic script which utilises the pynput library to left click every 100ms or .1s.

Usage: python3 AutoClicker.py

- Use the 'a' key to start or stop the clicking.
- Use the 's' key to close the program

# Port Scanner 
Very basic script which utilizes pythons inbuilt socket library to make tcp calls to a 
set range of ports of a host both defined by the user.

Usage: python3 SimplePortScanner.py

* Enter the input when prompted to do so
    * Three prompts: 
        * IPv4 address
        * Port Range: 0-25565
        * Number of threads to run concurrently