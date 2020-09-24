# Clean Text

## Problem Statement:

A client provides a csv file that has characters that are not ascii. The file can have many records and the non-ascii character can be different everytime. The non-ascii characters need to be changed to the ascii equivalent becuase the file needs to be uploaded to another system, but the upload freezes if there are non-ascii characters.

## Solution

I created a simple program that does the following:  
    * Import unidecode  
    * Asks for the path to the file  
    * Create new file name for the output with _cleaned.csv at the end  
    * Opens the file and reads each line  
    * Change each line with unidecode  
    * Write the new line into a new csv file  
    * Characters should now all be ascii  