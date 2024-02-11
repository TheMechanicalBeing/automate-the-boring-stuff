# Chapter 16 - Working with CSV Files and JSON Data

## Exercise 1 - Removing the Header from CSV Files

Program that opens every file with _.csv_ extension in the current working directory, read in the contents of the CSV file, and rewrite the contents without the first row to a file of the same time.

### Requirements
- Find all the CSV files in the current directory
- Read in the full contents of each file
- Write out the contents, skipping the first line, to a new CSV file
- Loop over a list of files from `os.listdir()`, skipping the non-CSV files
- Create a CSV `reader` object and read in the contents of the file, using the `line_num` attribute to figure out which line to skip
- Create a CSV `writer` object and write out the read-in data to the new file

## Exercise 2 - Fetching Current Weather Data

Program that prints out current weather data from _OpenWeatherMap.org_

### Requirements
- Read the requested location from the command line
- Download JSON weather data from _OpenWeatherMap.org_
- Convert the string of JSON data to Python data structure
- Print the weather for today and the next two days
- Join strings in `sys.argv` to get the location
- Call `requests.get()` to download the weather data
- Call `json.loads()` to convert the JSON data to Python data structure
- Print the weather forecast

## Exercise 3 - Excel-toCSV Converter

### Requirements