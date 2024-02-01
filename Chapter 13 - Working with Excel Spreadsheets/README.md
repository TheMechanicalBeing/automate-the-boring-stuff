# Chapter 13 - Working with Excel Spreadsheets

## Exercise 1 - Reading data from a Spreadsheet

Script that can read from the census spreadsheet file and calculate statistics for each country in a matter of seconds

### Requirements
- Read the data from the Excel spreadsheet
- Count the number of census tracts in each country
- Count the total population of each country
- Print the result
- Open and read the cells of an Excel document with `openpyxl` module
- Calculate all the tract and population data and store it in a data structure
- Write the data structure to a text file with the .py extensions using the `pprint` module

## Exercise 2 - Updating a Spreadsheet

Program that automatically updates cells in spreadsheet of produce cells. To be more precise, it changes the product price of garlic, celery and lemon

### Requirements
- Open the spreadsheet file
- Loop over all the rows
- If the row is garlic, celery, or lemons, change the price
- Save the spreadsheet to a new file

## Exercise 3 - Multiplication Table Maker

Program that makes a number _N_ from the command line and creates an _N_ x _N_ multiplication table in an Excel spreadsheet.

### Requirements
- Use `sys.argv` to retrive dimensions of multiplication table
- Use `openxpyxl` module to do Excel spreasheet manipulation
- Save the file with _.xlsx_ extension

## Exercise 4 - Blank Row Inserter

Program that takes two integers and a filename string as command line arguments. The first integer is starting row and second one is how many rows to be blank.

### Requirements
- Use `sys.argv` to get two integers and filename as input
- Use `openpyxl` module to manipulate on Excel spreadsheets
- Print out the message

## Exercise 5 - Spreadsheet Cell Inverter

Program that inverts the row and column of the cells in the spreadsheet.

### Requirements
- Use `sys.argv` to get _.xlsx_ filename that has to be inverted
- Use `openpyxl` module to invert cells
- Print out the message

## Exercise 6 - Text Files to Spreadsheets

Program that reads the contents of several text files and insert those contents into a spreadsheet, with one line of text per row.

### Requirements
- Use `sys.argv` to let user input text files
- Use `openpyxl` module to make operations into spreadsheet

## Exercise 7 - Spreadsheet to Text Files

### Requirements