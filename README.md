# iChat Message Extractor

This repository contains a Python script to extract messages and timestamps from iChat `.ichat` files and save them to `.txt` files. The script is designed to work with the iChat format and might be specific to certain versions of the software.

I built this script to handle my specific use-case of extracting the message content of a list of .ichat files that were dated from June, 2019 - January 2019. Because iChat files do not specify the precise version of iMessages I cannot explicitly know if other iChat files will work with this script as-is. 

You are encouraged to use this to whatever ends you so please if it helps in any way. If nothing else and you haven't already, this lays the groundwork for a customized script to transform the binary p_list of an iChat file into a more readable and useful xml file. 

You can also perform this action over several documents at once thereby automating a task that would have taken you some time longer.
And then wWith this newly unallocated time, you will now be able to work even harder for your company and with less distractions! 

## Requirements

- Python 3
- macOS (due to the use of the `plutil` command)

## Usage

1. Clone this repository or download the script to your computer.
2. Navigate to the directory containing the script using a terminal.
3. Run the script with the command:
   ```
   python extract_to_separate_files.py path_to_ichat_file1 path_to_ichat_file2 ...
   ```
   Replace `path_to_ichat_file1`, `path_to_ichat_file2`, etc., with the paths to your `.ichat` files.
4. For each input `.ichat` file, an output `.txt` file will be created in the same directory with the extracted messages.

## How it Works

- The script uses the `plutil` command to convert the binary plist iChat file to XML format.
- It then extracts the messages and their associated timestamps from the XML.
- The extracted messages and timestamps are saved to a `.txt` file.

## Limitations

This script has been tested on a specific iChat file format. Given the evolution of iChat (and later, Messages) over the years, different versions of the software might produce files in slightly different formats. Users should verify the extracted data for accuracy.

## License

This project is licensed under the Apache License - see the `LICENSE` file for details.