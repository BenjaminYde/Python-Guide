#!/usr/bin/python3

import threading
import time

def non_daemon_task():
    try:
        time.sleep(6)
        print(f"Non-Daemon finished")
    except KeyboardInterrupt: # this will not run!
        print("Non-Daemon Thread: Caught KeyboardInterrupt")

def daemon_task():
    try:
        time.sleep(10)
        print(f"Daemon finished")
    except KeyboardInterrupt: # this will not run!
        print("Daemon Thread: Caught KeyboardInterrupt")

def run():
    # Creating non-daemon thread
    print("Started non-daemon")
    non_daemon_thread = threading.Thread(target=non_daemon_task)
    non_daemon_thread.start()

    # Creating daemon thread
    print("Started daemon")
    daemon_thread = threading.Thread(target=daemon_task)
    daemon_thread.daemon = True
    daemon_thread.start()
    
    # Wait
    try:
        print("Waiting...")
        time.sleep(3)
    except KeyboardInterrupt:
        print("Main Program: Caught KeyboardInterrupt")

    print("Main Program: Exiting")
    
run() # run and terminate the program