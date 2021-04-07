#!/usr/bin/env python3

import emails
import os
from datetime import date
import reports

path = os.path.expanduser('~') + '/supplier-data/descriptions/'

result = []
text_file_data = []

for text_file in os.listdir(path):
    with open(path + text_file, 'r') as f:
        text_file_data.append([line.strip() for line in f.readlines()])


def process_data(data):
    for item in data:
        result.append("name: {}<br/>weight: {}\n".format(item[0], item[1]))
    return result


if __name__ == "__main__":
    # generate report
    title = "Processed Update on {}\n".format(date.today().strftime("%B %d, %Y"))
    attachment = "/tmp/processed.pdf"
    paragraph = "<br/><br/>".join(process_data(text_file_data))
    reports.generate_report(attachment, title, paragraph)

    # send email
    subject = "Upload Completed - Online Fruit Store"
    sender = "automation@example.com"
    # receiver = "<username>@example.com"
    receiver = "{}@example.com".format(os.environ.get('USER'))
    body = "All fruits are uploaded to our website successfully. A detailed list is attached to this email."
    message = emails.generate_email(sender, receiver, subject, body, attachment)
    emails.send_email(message)
