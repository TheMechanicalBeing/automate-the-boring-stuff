# Chapter 10 - Organizing Files

## Exercise 1 - Renaming Files With American-Style Dates to European-Style Dates

Program that takes many files with American-style (MM-DD-YYYY) dates in their names and renames it to European-style (DD-MM-YYYY) dates.

### Requirements
- Program searches all the filenames in provided working directory for American-style dates
- When one is found, it renames the file with the month and day swapped to make it European-style
- Create a regex that can identify the text pattern of American-style dates
- Call `os.listdir()` to find all the files in the working directory
- Loop over each filename, using regex to check whether it has a date
- If it has a date, rename the file with `shutil.move()`

## Exercise 2 - Backing up a Folder into a ZIP File

Program that creates a ZIP file "snapshots" of the entire folder.

### Requirements
- Use `zipfile` module
- Make snapshots of folder as example_1.zip, example_2.zip, and so on
- Use function for main execution

## Exercise 3 - Selective Copy

Program that walks through a folder tree and searches for files with a certain file extension (such as .pdf and .jpg).

### Requirements
- Prompt user for extension to know which files to find
- Search through each file and copy only files that match user's input
- Copy files from whatever location they are in to a new folder

## Exercise 4

### Requirements

## Exercise 5

### Requirements