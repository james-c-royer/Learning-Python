import time
my_time = int(input("Enter the time in seconds: "))

for x in range(my_time, 0, -1):
    hours = int(x / 3600)
    minutes = int(x / 60 % 60)
    seconds = int(x % 60)
    print(f"{hours:02}:{minutes:02}:{seconds:02}")
    time.sleep(1)
    if x == 1:
        print("Time's up")