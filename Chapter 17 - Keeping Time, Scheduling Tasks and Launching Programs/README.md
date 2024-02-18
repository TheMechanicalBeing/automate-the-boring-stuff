# Chapter 17 - Keeping Time, Scheduling Tasks and Launching Programs

## Exercise 1 - Super Stopwatch

Simple stopwatch that prints out times between "laps" and also the lap number.

### Requirements
- Track the amount of time elapsed presses of the __ENTER__ key, with each key press starting a new "lap" on the timer
- Print the lap number, total time, and lap time
- Find the current time by calling `time.time()` and store it as a timestamp at the start of the program, as well as at the start of each lap
- Keep a lap counter and increment if every time the user presses __ENTER__
- Calculate the elapsed time by subtracting timestamps
- Handle the `KeyboardInterrupt` exception so the user can press __CTRL__-__C__ to quit

## Exercise 2 - Multithreaded XKCD Downloader

Chapter 12's third exercise but multithreaded implementation.

### Requirements
- Same as singlthreaded XKCD Downloader but with one catch
- Code implementation should be multithreaded

## Exercise 3 - Simple Countdown Program

Countdown program that plays an alarm at the end of the countdown.

### Requirements
- Count down from 60
- Play a sound file (alarm.wav) when the countdown reaches zero
- Pause for 1 second in between displaying each number in the countdown by calling `time.sleep`
- Call `subprocess.Popen()` to open the sound file with the default application

## Exercise 4 - Pretiffied Stopwatch

### Requirements

## Exercise 5 - Scheduled Web Comic Downloader

### Requirements