# iChat Message Extractor

## **update** 11/6/23

Included the use of the tkinter library. Running this python script will now pull up a finder window so you can select your directory through the normal graphical interface on MacOS. If I use this script again or if anyone requests it, I will make this application into a full on app that can be shared and run like any other app on MacOS. 

---

<br>


This repository contains a Python script to extract messages and timestamps from iChat `.ichat` files and save them to `.txt` files. The script is designed to work with the iChat format and might be specific to certain versions of the software.

I built this script to handle my specific use-case of extracting the message content of a list of .ichat files that were dated from June, 2019 - January 2019. Because iChat files do not specify the precise version of iMessages I cannot explicitly know if other iChat files will work with this script as-is. So far, I've had no issues with any version of `.ichat` files.

You are encouraged to use this to whatever ends you so please if it helps in any way. If nothing else and you haven't already, this lays the groundwork for a customized script to transform the binary p_list of an iChat file into a more readable and useful xml file. 

## Requirements

- Python 3
- macOS (due to the use of the `plutil` command)

## Usage

1. Clone this repository or download the script to your computer.
2. Navigate to the directory containing the script using a terminal.
3. Run the script with the command:
   ```
   python app.py
   ```
## How it Works

- The script uses the `plutil` command to convert the binary plist iChat file to XML format.
- It then extracts the messages and their associated timestamps from the XML.
- The extracted messages and timestamps are saved to a `.txt` file.

## Limitations

This script has been tested on a specific iChat file format. Given the evolution of iChat (and later, Messages) over the years, different versions of the software might produce files in slightly different formats. Users should verify the extracted data for accuracy.

## License

This project is licensed under the Apache License - see the `LICENSE` file for details.