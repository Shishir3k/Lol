import ctypes

def display_error_messages():
    errors = [
        "You Got Pranked😜😛."
    ]
    
    for error in errors:
        ctypes.windll.user32.MessageBoxW(None, error, "VIRUS.LOL", 1)

if __name__ == "__main__":
    while True:
        display_error_messages()
