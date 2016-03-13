"""
	simple and nice-- was DISCARDED because namedtuple's fieldnames cannot start with `_` :(
"""

from collections import namedtuple						# inspired by platform.uname()

basicUtil = namedtuple("basicUtil", ["colorize"])
DBfuncs = namedtuple("DBfuncs", ["scan_", "reportChanges"])
bgTasks = namedtuple("bgTasks", ["makeLog"])
fileFunc = namedtuple("fileFunc", ["search", "getTheName_", "rename", "create_", "create", "modify"])
homeScreen = namedtuple("homeScreen", ["main"])


basicUtil.colorize = "Alas!\nWe apologise for the lack in your experience.\n\n\nP.S. kannadChar Blame it on the pathetic code running below this OS"

DBfuncs.scan_ = "\n\nFatal Error: The main \"Pool\" folder contains one or more sub-folders. This is a serious Design Violation, sub-folders cause mess & confusion.\n\nThe main \"Pool\" folder MUST ONLY contain (normal) files.\n\nHere's what we suggest:\n  1. if the folders are counter-parts of .htm(l) web pages, please run\n\t_,_,_,_,_,_ utility\n  2. if the contents of foder are integral/dependent i.e. part of an entire\n\tcourse/session/project, please zip them into a file at \'Store\' level\n\tcompression\n  3. when steps 1 and 2 are done throughly AND recursively, put all files into\n\tthe main \"Pool\" Folder\n\nThank You\n\n\n\n\n"
DBfuncs.reportChanges = [
	"\nthe contents of \"%(_)s\" have changed, did you make these changes?\n\to. Open the file\n\td. open the folder containing the file\n\ty. yes I understand the changes made and validate it\n\tn. no I didn't change anything, something's not right\n\ti. Ignore the truth and move on",
	"\n\n\nFatal Error: some files are missing from the main \"Pool\" folder, a suitable report has been created in \'--logs.txt\' file\n\n\n\n\n"
]

bgTasks.makeLog = [
	"\n\n\n_______________________________%s________________________________\nList of files missing as detected on above mentioned date & time:\n",
	"\n----x----x----x----x----x----x----x----x----x----x----x----x----x----x----x----"
]

fileFunc.search = "searching syntax help by examples:\n  - <a, b> means files having tags in which tag<a> is followed by tag<b>\n  - <a, b|c> means files having tags in which tag<a> followed by either\n\ttag<b> or tag<c>\n%s\n\n\nType the name of tag(s) you want to search here:\n"
fileFunc.getTheName_ = "To %s a file, we must know its current name, so you can either:\n\t1. specify the EXACT file name\n\t\tOR\n\t2. search for that file by means of tags assigned to it\n\nYour choice: "
fileFunc.rename = "\n\nGreat! So the file name you want to change is:\n\t%s\n\nEnter below the new name you wish to give it:\n\t"
fileFunc.create_ = "\n\nEnter (comma seperated) tags you wish to assign to this file (in decreasing order of relavance):\n"
fileFunc.create = "\nTags assigned successfully, before moving on to the next file would you like to\nrename this file - so that file name is more readable and non-cryptic (y/n)?"
fileFunc.modify = "\nThe file:\n\t%s\nhas the tags:\n\n[%s]\nassociated with it. Following is a list of all existing tags:\n"

main = "\nWhat would you like to do?\n%s\n  s. Search through files on basis of tags.\n  r. Rename an existing file.\n  m. Modify tags assigned to a file.\n  q. Quit this application in a safe manner - rescan the directory and\n\tvalidate modification_done_to_files and files_added_to_directory\n\n"














"""
Really important info discovered about decoding info recieved from terminal via methods like subprocess.check_output--NEWLINE--	import locale--NEWLINE--	decode(binaryAnswer, encoding=locale.getpreferredencoding()).encode("UTF-8")--NEWLINE-----------------------------------------------------------------------------------------------------------------------------NEWLINE--__doc__ = "using filename as classname and exploiting classes as `struct`s\--NEWLINE--	if a function has more than one large_strings, then it is put in array"--NEWLINE----NEWLINE--class basicUtil():--NEWLINE--	drawWelcome = ""--NEWLINE--class DBfuncs():--NEWLINE--	reportChanges = --NEWLINE--	_scan = --NEWLINE--class bgTasks():--NEWLINE--	makeLog = [--NEWLINE--	]--NEWLINE--	num_NewFilesAdded = --NEWLINE--class homeScreen():--NEWLINE--	main = [--NEWLINE--		"",	# transfered to bgTasks.DBscan._scan--NEWLINE--		--NEWLINE--	]--NEWLINE--class fileFunc():--NEWLINE--	search = --NEWLINE--	_getTheName = --NEWLINE--	rename = --NEWLINE--	_create = --NEWLINE--	create = --NEWLINE--	modify = --NEWLINE--
"""
