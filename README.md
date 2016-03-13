# Vision and Concept

## Aim
### Problems

I have many knowingly & unknowingly created (and modified (as in bookmarked, updated, edited) in some cases) copies of the same original file.

When merging these files it becomes extremely tedious, especially because they get heavily scattred due to change in directory structure (original@home vs. working_copy@out) and the modifications done to file.

Also, many of those files/complete-in-itself-folders belong to more than one category, so tagging was required anyway.
### Solutions

A DIRECTORY MERGER
KEEP ONLY ONE COPY OF EACH FILE
a version control is needed, atleast aids in deciding which file to keep which to delete

## FEATUREs
 - Primary key is SHA1 of file
 - A duplicate finder that either creates links or avoids re-copying redundant file
 - Versions of a file are decided by
	- common-ness in file name
	- by user
 - When importing from dirty-nested-directory tree, this app intelligently assigns ParDir name as tags to the file when moving to FileCentral-- weather or not to apply these tags depends on user

## DEPENDENCIES
webpage to .htmz convertor

## DEFINATIONS
FileCentral:	
