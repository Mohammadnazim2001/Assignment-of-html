import time

class Timer:
    def __init__(self, timeout):
        self.timeout = timeout
        self.start_time = None
        self.end_time = None

    def start(self):
        self.start_time = time.time()
        self.end_time = self.start_time + self.timeout

    def is_alive(self):
        return time.time() < self.end_time

    def join(self):
        while self.is_alive():
            time.sleep(0.1)

    def get_remaining_time(self):
        return self.end_time - time.time()


def timeout_function():
    print("Function called")

def main():
    timer = Timer(timeout=5) # Set the timeout to 5 seconds
    timer.start() # Start the timer
    timeout_function() # Call the function that should be stopped after the timeout
    print("Function execution complete")
    timer.join() # Wait for the timer to finish
    print("Timeout occurred")


if __name__ == "__main__":
    main()