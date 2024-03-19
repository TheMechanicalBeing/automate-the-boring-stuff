# Chapter 19 - Manipulating Images

## Exercise 1 - Adding a Logo
Program that can resize thousands of images and add a small logo watermark to the corner of each.

### Requirements
- Load the logo image
- Loop over all _.png_ and _.jpg_ files in the working directory
- Check whether the image is wider or taller than 300 pixels
- If so, reduce the width or height (whichever is larger) to 300 pixels and scale down the other dimension proportionally
- Open the _catlogo.png_ file as an `Image` object
- Loop over the strings returned from `os.listdir(".")`
- Get the width and height of the image from the `size` attribute
- Calculate the new width and height of the resized image
- Call the `resize()` method to resize the image
- Call the `paste()` method to paste the logo
- Call the `save()` method to save the changes, using the original filename

## Exercise 2 - Extending and Fixing the Chapter Project Programs
Same as same chapter's Exercise 1 but works with *.gif* file extensions, scales proportions with logo, and is case-insensitive.

### Requirements
- Add conditional for finding *.gif* files during directory files iteration
- Check for file extensions case-insensitively (ex. it should work on both *.PNG* and *.png*)
- Scale the logo and background image by making background image at least 2 times larger
- Iteratoe over each image in *.gif* to add logo on whole 'animation'

## Exercise 3 - Identifying Photo Folders on the Hard Drive

### Requirements

## Exercise 4 - Custom Seating Cards

### Requirements