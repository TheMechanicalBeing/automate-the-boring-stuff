# Chapter 9 - Reading and Writing Files

## Exercise 1 - Generating Random Quiz Files

Program that generates random quiz files. The quiz consists MCQ (multiple-choice questions) about US capitals.

### Requirements
- Creates 35 different quizzes
- Creates 50 MCQ for each quiz, in random order.
- Provides the correct answer and three random answers for each questions in random order
- Writes the quizzes to 35 text files
- Writes the answer keys to 35 text files
- Store the states and their capitals in a dictionary
- Call `open()` and `write()` for the quiz and answer key text files
- Use `random.shuffle()` to randomize the order of the questions and multiplce-choice options

## Exercise 2 - Updatable Multi-Clipboard

Rewriting program from CH6's example 1, but it uses `shelve` module. The user now be able to load to the clipboard without having to modify the source code.

### Requirements
- The command line argument for the keyword is checked
- If the argument is `save`, then the clipboard contents are saved to the keyword
- If the argument is `list`, then all the keywords are copied to the clipboard
- If the argument is `delete`, then keyword should be deleted
- Otherwise, the text keyword is copied to the clipboard
- Read the command line arguments from `sys.argv`
- Read and write to the clipboard
- Save and load to a shelf file

Note: You should add environmental variable to PATH for .bat files to run .bat file easily

## Exercise 3 - Mad Libs

Program that read in text files and lets the user add their own text anywhere the word ADJECTIVE, NOUN, ADVERB, or VERB appears in the text file. For example, a text file may look like this.

### Requirements
- Show the user file content
- Prompt the user to change each ADJECTIVE, NOUN, ADVERB, or VERB with specific word
- Show the user changed content
- Save the content into new file

## Exercise 4

### Requirements