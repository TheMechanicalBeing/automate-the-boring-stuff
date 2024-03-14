# Chapter 18 - Sending Email and Text Messages

## Exercise 1 - Sending Member Dues Reminder Emails

Script that sends emailing reminders to members that has not paid for subscription last month.

### Requirements
- Read data from Excel spreadsheet
- Find all members who have not paid dues for the latest month
- Find their email addresses and send them personalized remindes
- Open and read the cells of an Excel document with the `openpyxl` module
- Create a dictionary of members who are behind on their dues
- Log in to SMTP server by calling `smtplib.SMTP()`, `ehlo()`, `starttls()`, and `login()`
- For all members behind on their dues, send a personalized reminder email by calling the `sendmail()` method

### Note
I learned these concepts in this chapter but. I have not made other exercises due to not being able to use `smtp` and `imap` on emails.