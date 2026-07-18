import time

while True:
    user_choice = input("Enter 'start' or 's' to begin or 'exit' or 'q' to quit: ")
    if user_choice in ('exit', 'q'):
        break
    elif user_choice in ('start', 's'):
        try:
            time1 = int(input("Enter minutes (0-60): "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        if time1 < 0 or time1 > 60:
            print("Invalid input. Please enter a time between 0 and 60.")
            continue

        for m in range(time1):
            for s in range(59, -1, -1):
                for ms in range(999, -1, -1):
                    print(f"\r{m:02}:{s:02}:{ms:02}", end="")
                    time.sleep(0.001)
        print("\nTimer finished.")
    else:
        print("Invalid operation or subcommand.")