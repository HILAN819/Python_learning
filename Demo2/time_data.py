import time
print(time.time())


def send_emails():
    for i in range(10000):
        pass


start_time = time.time()
send_emails()
end_time = time.time()
duration = end_time - start_time
print(duration)
