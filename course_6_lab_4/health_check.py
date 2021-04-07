#!/usr/bin/env python3

import shutil
import psutil
import socket
import emails


def check_cpu_usage():
    usage = psutil.cpu_percent(1)
    return usage > 80


def check_disk_usage(disk):
    du = shutil.disk_usage(disk)
    space = du.free / du.total * 100
    return space < 20


def check_available_memory():
    memory = psutil.virtual_memory().available / 1024 / 1024
    return memory < 500


def check_localhost():
    localhost = socket.gethostbyname('localhost')
    return localhost == '127.0.0.1'


def send_email(subject):
    try:
        sender = "automation@example.com"
        receiver = "student-01-293986bc8109@example.com"
        body = "Please check your system and resolve the issue as soon as possible"
        email = emails.generate_error_message(sender, receiver, subject, body)
        emails.send_email(email)
    except NameError:
        pass


if __name__ == "__main__":

    if check_cpu_usage():
        subject = "Error - CPU usage is over 80%"
        send_email(subject)
    if check_disk_usage('/'):
        subject = "Error - Available disk space is less than 20%"
        send_email(subject)
    if check_available_memory():
        subject = "Error - Available memory is less than 500MB"
        send_email(subject)
    if not check_localhost():
        subject = "Error - localhost cannot be resolved to 127.0.0.1"
        print(subject)
        send_email(subject)
