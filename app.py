#!/usr/bin/env python3

import re
import datetime
import subprocess
import os


def apple_time_to_datetime(apple_time):
    """Convert Apple's timestamp to a standard datetime."""
    base_date = datetime.datetime(2001, 1, 1)
    delta = datetime.timedelta(seconds=float(apple_time))
    return base_date + delta


def ichat_to_xml(file_path):
    """Convert an iChat binary plist file to XML format."""
    output = subprocess.check_output(
        ["plutil", "-convert", "xml1", "-o", "-", file_path])
    return output.decode('utf-8')


def extract_messages_from_content(content):
    """Extract messages and timestamps from the XML content."""
    message_pattern = re.compile(
        r'<key>NS\.string<\/key>\s*<string>(.*?)<\/string>', re.DOTALL)
    time_pattern = re.compile(
        r'<key>NS\.time<\/key>\s*<real>(.*?)<\/real>', re.DOTALL)

    messages_extracted = message_pattern.findall(content)
    timestamps = time_pattern.findall(content)
    timestamps_converted = [apple_time_to_datetime(t) for t in timestamps]

    return list(zip(timestamps_converted, messages_extracted))


def main():
    """Main function to process iChat files in the given directory."""
    import sys
    if len(sys.argv) < 2:
        print("Usage: python script_name.py path_to_directory_with_ichat_files")
        sys.exit(1)

    directory_path = sys.argv[1]
    ichat_files = [os.path.join(directory_path, f) for f in os.listdir(
        directory_path) if f.endswith('.ichat')]

    for file_path in ichat_files:
        output_file_path = os.path.splitext(file_path)[0] + ".txt"
        xml_content = ichat_to_xml(file_path)
        messages = extract_messages_from_content(xml_content)
        with open(output_file_path, 'w') as outfile:
            for timestamp, message in messages:
                outfile.write(f"{timestamp} - {message}\n")


if __name__ == "__main__":
    main()
