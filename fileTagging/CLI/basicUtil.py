"""
	Almost all Cross Platform issues are addressed here so that other files
	using basicUtil don't have to worry.
"""

import os, sys, subprocess

class UnderTheHood(underTheHood):
	"""
		things which are between system and program
		programs ask us for something, questions and actions which remain hidden from users
		like calcSHA1 and detectOS
	"""
	def __init__(self, arg):
		super(UnderTheHood, self).__init__()
		self.arg = arg

class OverTheTop(overTheTop):
	"""
		FROM programs TO user (after modify/beautiy)
		things which are between user and program, like colorize and lessDisplay
	"""
	def __init__(self, arg):
		super(OverTheTop, self).__init__()
		self.arg = arg

this_os = str()
getXYlimits = lambda: (os.get_terminal_size().columns, os.get_terminal_size().lines)	# cross-platform, get the x-axis and y-axis limits of shell in which this program is running # NOT WORKING--- getXYlimits = lambda: os.get_terminal_size().columns, os.get_terminal_size().lines

def quit(msg):
	code = 1 if msg is "failure" else 0
	temp = input()
	sys.exit(code)

def detectOS():
	global this_os
	this_os = platform.uname().system						# worse `sys.platform` WORST big no no to `os.name`
	if this_os not in "Windows":							# update values for other *nix OSes, CONTRIBUTE table to docs "16.14. platform — Access to underlying platform’s identifying data"
		print("Unknown Operating System or Environment, terminating")
		quit("failure")
	return

def clrscr():												# from os import popen--NEWLINE--	# with popen('clear') as f:--NEWLINE--	#	clear = f.read()	# clear = "\x1b[H\x1b[2J" -- move the cursor to the top-left corner && clear all the screen--NEWLINE--	# print(clear)--NEWLINE--	# ----------------------------------------------------NEWLINE--	# sys.stdout.flush().print()
	shellExec = lambda x: subprocess.call(x, shell=True)
	if this_os is "Windows":
		temp = None if b"65001" in subprocess.check_output("chcp", shell=True) else shellExec("chcp 65001")
		temp = shellExec("cls")
	else:
		temp = shellExec("clear")
	return

def colorize(text, colorCode):
	"""
		cross-platform, colors `text` according to the given `colorCode`
	"""
	if this_os is "Windows":
		try:
			import UniCurses as curses
		except ImportError:
			ctypes.windll.user32.MessageBoxW(None, stringStore.__file__.__name__, "Apologies", 0)
	else:
		import curses
	curses.()
	pass

def drawWelcome(text="WELCOME"):
	"""
		draws an ascii kinda beautiful welcome screen, requires
		getXYlimits(), clrscr(), colorize()
	"""
	def full(strng):
		#### str.center(strng, maxWidth-4)
		x = maxWidth-len(strng)
		return "||" + " "*(x//2-2) + strng + " "*(x-x//2-2) + "||"
	maxWidth, maxLength = getXYlimits()
	decoration = [
		"." + '_'*(maxWidth-2) + ".",
		"||" + " "*(maxWidth-4) + "||",
		" \\" + "_"*(maxWidth-4) + "/ "
	]
	final = decoration[0]+decoration[1]+decoration[1]
	lines = list()
	while True:
		lines.append(text[:maxWidth-8])
		if len(text) > (maxWidth-6):
			text = text[maxWidth-8:]
		else:
			break
	try:
		lines[0]
		for _ in lines:
			final+= full(_)
	except IndexError:
		final+= full(text)
	print(final+decoration[1]+decoration[2])
	return

def calcSHA1(pathToFile):
	"""
		best n fastest way to calculate SHA1 of given file ignoring file's
		name i.e. calculate SHA1 of the file's content
	"""
	return sha1_hash

def lessDisplay(hugeString):
	"""
		exploit `echo hugeString | less` kinda functionality in shell.
		The functions are, press:
			- ` ` to view more
			- `Esc` to stop viewing
			- `opn SrNo` to copy folder+file path to clip-board
			- `ren SrNo` to copy file name to clip-board
			- `mod SrNo` to copy file name to clip-board
		show stuff like `page 6 of 20`
	??from pager import getheight, getheight			# pypi.python.org/pypi/pager
	"""
	clrscr()
	return



# !!! Peter G. Marczis opinion --- calling cls with os is a bad idea generally. Imagine if I manage to change the cls or clear command on your system, and you run your script as admin or root
