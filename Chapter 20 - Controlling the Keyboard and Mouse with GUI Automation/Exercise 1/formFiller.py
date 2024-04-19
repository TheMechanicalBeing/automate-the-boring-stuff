import time

import pyautogui

form_data = [
    {'name': 'Alice', 'fear': 'eavesdroppers', 'source': 'wand', 'robocop': 4, 'comments': 'Tell Bob I said hi.'},
    {'name': 'Bob', 'fear': 'bees', 'source': 'amulet', 'robocop': 4, 'comments': 'n/a'},
    {'name': 'Carol', 'fear': 'puppets', 'source': 'crystal ball', 'robocop': 1,
     'comments': 'Please take the puppets out of the break room.'},
    {'name': 'Alex Murphy', 'fear': 'ED-209', 'source': 'money', 'robocop': 5,
     'comments': 'Protect the innocent. Serve the public trust. Uphold the law.'},
]

if __name__ == "__main__":
    pyautogui.PAUSE = 0.5
    print("Ensure that the browser window is active and the form is loaded!")

    for person in form_data:
        print('>>> 5-SECOND PAUSE TO LET USER PRESS CTRL-C <<<')
        time.sleep(5)

        print(f'Entering {person["name"]} info...')
        pyautogui.write(['\t', '\t', '\t', '\t'])

        pyautogui.write(person['name'] + '\t')

        pyautogui.write(person['fear'] + '\t')

        if person['source'] == 'wand':
            pyautogui.write(['down', '\t'], 0.5)