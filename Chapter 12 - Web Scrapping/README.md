# Chapter 12 - Web Scrapping

## Exercise 1 - mapIt.py with the webbrowser Module 

Program that automatically launches the map in browser using the contents of clipboard.

### Requirements
- Get a street address from the command line arguments or clipboard
- Open the web browser to the Google Maps page for the address
- Read the command line arguments from `sys.argv`
- Read the clipboard contents
- Call the `webbroser.open()` function to open the web browser

## Exercise 2 - Opening All Search Results

Program that automatically opens a browser and  open all the search results for Python Package Index in https://pypi.org.

### Requirements
- Get search keywords from command line arguments
- Retrieve the search results page
- Open a browser tab for each result
- Read the command line from `sys.argv`
- Fetch the search result with the `requests` module
- Find the links to each search result
- Call the `webbrowser.open()` function to open the web browser

## Exercise 3 - Downloading all XKCD Comics

Program that downloads each comic image from XKCD geek webcomic website.

### Requirements
- Load the XKCD home page
- Save the comic image on that page
- Follow the Previous Comic link
- Repeat until it reaches the first comic
- Download pages with the `requests` module
- Find the URL of the comic image for a page using Beautiful Soup
- Download and save the comic image to the hard drive with `iter_content()`
- Find the URL of the Comic Link, and repeat

## Exercise 4 - Command Line Emailer

A program that takes an email address and string of text on the command line and then, using `selenium`, logs in to your email account and sends an email of the string to the provided address.

### Requirements
- Get two command line arguments one for email address and another for text using `sys.argv`
- Manipulate on HTML elements using `selenium` module
- Open the browser
- Log in to your email
- Input the email and text to send

## Exercise 5 - Image Site Downloader

Program that goes to a photo-sharing site like Flickr, searches for a category of photos, and then downloads all the resulting images.

### Requirements
- Prompt the user for searching term and quantity of images to be downloaded
- Open the https://www.flickr.com/ and input the search term
- Download the images
- Save the images to folder

## Exercise 6 - 2048

### Requirements

## Exercise 7 - Link Verifications

### Requirements