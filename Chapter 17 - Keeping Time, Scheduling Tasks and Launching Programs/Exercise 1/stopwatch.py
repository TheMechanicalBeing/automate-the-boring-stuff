import time


if __name__ == "__main__":
    print("Press ENTER to begin. Afterward, press ENTER to \"click\" the stopwatch. Press CTRL-C to quit.")
    input()
    print("Started.")
    start_time = time.time()
    last_time = start_time
    lap = 1

    try:
        while True:
            input()
            lap_time = round(time.time() - last_time, 2)
            total_time = round(time.time() - start_time, 2)
            print(f"Lap #{lap}: {lap_time}\nTotal time: {total_time}")
            lap += 1
            last_time = time.time()
    except KeyboardInterrupt:
        print("\nDone.")
