from threading import Thread, Lock
from datetime import datetime
from queue import Queue
import ipaddress
import socket
import sys
from pyfiglet import Figlet

ip = None
port_range = [0, 25565]
threads = 1
thread_array = []
debug = True
queue = None
print_lock = Lock()


def main():
    f = Figlet(font='slant')
    print(f.renderText('Simple Portscan'))
    print('Enter the ip which you are targeting: ')
    global ip
    valid_ip = False
    while not valid_ip:
        ip = input()
        try:
            ip = ipaddress.ip_address(ip)
            valid_ip = True
        except ValueError:
            print('The address provided is invalid: %s' % ip)
            print('Please enter a proper ip: ')

    print('Enter the port range 0-25565')
    test_range = input()
    while not (check_range(test_range)):
        print('Please enter a valid port range i.e 0-25565: ')
        test_range = input()
    global port_range
    port_range = [test_range.split('-')[0], test_range.split('-')[1]]
    if debug:
        print('Set port-range is: %s' % port_range)
    initialise_queue()
    print('How many threads do you wish to run: ')
    global threads
    threads = int(input())
    if threads <= 0:
        print('You cannot have no threads - defaulting to one')
        threads = 1
    print("You are scanning {} with range {}".format(ip, port_range))
    start_time = datetime.now()
    print("Start time {}".format(start_time))
    for i in range(threads):
        thread = Thread(target=discover_port, args=(i,))
        thread_array.append(thread)
        thread.start()
    for thread in thread_array:
        thread.join()
    finish_time = datetime.now()
    print("Finished at {}".format(finish_time))
    print("Total elapsed time {}".format(finish_time - start_time))


def check_range(test_range):
    splits = test_range.split('-')
    if len(splits) != 2:
        return False
    try:
        lower_range = int(splits[0])
        upper_range = int(splits[1])
    except SyntaxError:
        print('There was an error parsing your input is it in the format 0-255 ?')
        return False
    if lower_range < 0 or lower_range > 25565:
        print('There was an issue with the lower bound, it needs to be within 0 through 25565')
        return False
    if upper_range < 0 or upper_range > 25565 or upper_range < lower_range:
        if upper_range < lower_range:
            print('Lower range cannot be higher than the upper range')
        else:
            print('There was an issue with the upper bound, it needs to be within 0 through 25565')
        return False
    return True


def discover_port(thread_id):
    while not queue.empty():
        port = queue.get()
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            result = sock.connect_ex((str(ip), port))
            if result == 0:
                with print_lock:
                    print("Port {} is open".format(port))
            if debug:
                with print_lock:
                    print(str(port) + ' port queried from thread ' + str(thread_id))
            sock.close()
        except socket.error:
            print("Could not connect to the server")
            sys.exit()
        except KeyboardInterrupt:
            print("Keyboard Interrupt occured. Exiting.")
            sys.exit()


def initialise_queue():
    global queue
    queue = Queue(maxsize=int(port_range[1]) - int(port_range[0]) + 1)
    for i in range(int(port_range[0]), int(port_range[1])):
        queue.put(i)


if __name__ == "__main__":
    main()
