import os, json, datetime
import stringStore, basicUtil, DBfuncs

localDBfile = "db"																# could be db.sqlite3 or db.dat or whatever

def getPoolDirPath():
	basicUtil.drawWelcome()
	poolDirPath = input("Enter the complete (absolute) path to the main \
						pool folder:\n")										# suggest a list of 3-5 recently used directories?----	poolDirPath = os.path.abspath(poolDirPath) # pathlib.Path.resolve(".")  OR  os.path.normpath(os.path.join(os.getcwd(), "."))  OR  os.path.join(os.path.dirname(path), result)
	try:
		os.chdir(poolDirPath)
	except Exception:
		print("The directory whose path you typed is incorrect according to OS.")
		getPoolDirPath()
	else:
		try:
			with open(os.path.join(".", localDBfile), mode="rt"):
				pass
		except Exception:
			c = input("The directory exists but DB is uninitiated, do you \
						want to create new DB & start tagging (y/n)?")
			if c in "yY":
				DBfuncs.initiateDB()											# ask DBfuncs to scan and initiate database in this location
				print("Database initiated successfully, existing . . .")
				return
			else:
				basicUtil.quit(0)
	return

def makeLog(missingFilesList):
	reply = stringStore.bgTasks.makeLog[0] % \
			datetime.datetime.utcnow().strftime("%Y%m%d%H%M%S")					# how to get correct DDMMYYYYHHMMSS timestamp,, "time - Timestamp Python - Stack Overflow"
	for _ in missingFilesList:
		x = _anEntry.getInfo(_);	_anEntry.delete(_)
		reply+= json.dumps(x, sort_keys=True, indent=4) + "\n"
	reply+= stringStore.bgTasks.makeLog[1]
	with open(os.path.join(".","--logs.txt"), mode="at", encoding="UTF-8") as f:# ensure --logs.txt is the one in poolDirPath
		f.write(reply)
	return

def resolveSearchString(text):
	'''
		',' in searchString implies AND, for OR user inputs `a|b`.
		So, `a, b|c|d, e|f` ==> `[abe, abf, ace, acf, ade, adf]`
		also `b==x,y,z` i.e. searchString is `a, (x,y,z)|c|d, e|f`
		which would resolve to ``
		# see itertools before making up something
	'''
	pass




#------------------------------------------------------------------------------------------------------
# def anySubDirPresent(path):--NEWLINE--	x = lambda X: X if os.path.isdir(X) else None	# os.path.isdir VS pathlib.Path.is_dir--NEWLINE--	try:--NEWLINE--		list(set(  [x(_) for _ in os.listdir(path)]  ))[1]--NEWLINE--	except IndexError:--NEWLINE--		return False--NEWLINE--	return True
# fileList = [_ for _ in os.listdir(path) if os.path.isfile(_)]	# pythonically, get a list of all files in home folder
# windoezShit = subprocess.check_output("dir", shell=True).decode().split("\r\n")[5:-3]--NEWLINE--	for _ in windoezShit:--NEWLINE--		if "<DIR>" in _:--NEWLINE--			pass--NEWLINE--		else:--NEWLINE--			fileList.append(_[39:])
#------------------------------------------------------------------------------------------------------
# 	dbList = set(  '''get list of entries in DB'''  )
# 	newList = set(  getFileList()  )
# 	added = list(  newList.difference(dbList)  )
# 	removed = list(  dbList.difference(newList)  )

# 	# 1. pure ADDition -- newList has dbList doesn't have
# 	if len(added)>0 and len(removed) is 0:
# 		return 1, added			# okay -- now its upto user to add these into db or not, just show him the prompt
	
# 	# 2. pure REMOVal -- dbList has newList doesn't have
# 	elif len(removed)>0 and len(added) is 0:
# 		# fetch OriginalName, OriginalSize, NewName, NewSize, DOC, DOLM from names in list remove
# 		# update backEndDB to reflect these changes
# 		# call dump and quit

# 	# 3. mixed ADDition and REMOVal-- some files (n) have been added and some files (n or k) removed
# 	elif len(added)*len(removed) not 0:
# 		# for added do same steps as case1
# 		# for 

# 	# filenames have changed but content is intact
# 	elif :

# 	# filenames are same but content has changed, don't overlook this - changes can be as harmless as additionOfBookmarksToPDF or as devastating as 0byte file created with same name -- user must be informed
# 	elif len(added) is 0 and len(removed) is 0:
# 		# ok so this could mean either "nothing has changed" or "everything has changed" anyways gotta scan SHA1s
# 		# order files by size??
# 		# start cross-checking SHA1s -- modifiedList.append(  if sha1(newList[i]) != sha1(dbList[i])  ) ======  instead of checking SHA1s better check `os.stat(fileName).st_mtime` which may be unreliable due to OS date reset but if it is change then & only then cross-check via SHA1
# 		# ask user to open files in the list `modified` one-by-one and validate the changes -- if validated then update DB else send info to --log.txt

# 	# filename and content both has changed -- we are forced to assume it is a new file, unless we can compare coverPage_PDF
# 	else:
# 	else:							# looks simple but can be a big a MF
# 		pass	
# 	if strangeCase:					# MF == when num of files in pool hasn't changed but files/fileNames have changed
#------------------------------------------------------------------------------------------------------


# attendence by DB's register'
# 	lambda is_file_internally_modified: if d(st_mtime) not 0 --> True if d(SHA1) is 0 else False
# 	present -- if is_file_internally_modified "MODIFIED" else "the only normal case"
# 												modified_without_changing_name--> ask user to auth. if user_says yes--ok_updateDB
# 																										no-- created dump, could be 0byte
# 	absent -- if anySHA1matches "RENAMED_WOUT_PERMISSION" else "DELETED"
# 	newStudent -- if anySHA1matches "RENAMED_WOUT_PERMISSION" else "ADDED"



#------------------------------------------------------------------------------------------------------
# def resolveNest(text):
# 	if nest.search(text):		pass
# 	else:						return text
# 	try:
# 		beg = text.rindex("(")
# 		end = text.index(")", beg)		# CONTRIBUTE-- cannot do str.index(substr, start=x)--- error  TypeError: find() takes no keyword arguments
# 	except ValueError:
# 		return text
# 	text = text[:beg] + csv_list(text[beg+1:end]) + text[end+1:]
# 	resolveNest(text)
# ------------------------------------------------------------------------------------------------------------
# import json
# csv_list = lambda text: [_.strip() for _ in text.split(",")]
# def xss(searchString):
# 	tokens = dict(zip(  [_ for _ in range(searchString.count(",")+1)], csv_list(searchString)  ))
# 	for i in range(len(tokens)):
# 		value = tokens.get(i)
# 		if "|" in value:
# 			tokens[i] = value.split("|")
# 	print(json.dumps(tokens, sort_keys=True, indent=4))
# 	return tokens
# ------------------------------------------------------------------------------------------------------------
# def listMul(a, b):	# itertools.product
# 	c = list()
# 	if len(a) is 0:
# 		return b
# 	elif len(b) is 0:
# 		return a
# 	else:
# 		pass
# 	for i in a:
# 		for j in b:
# 			c.append([i, j])
# 	return c

# def parse(nested):
# 	suljha = []
# 	for x in nested:
# 		suljha = listMul(x, suljha)
# 	return suljha

# def xSS(searchString):
# 	''' `a, b|c|d, e|f` == abe abf ace acf ade adf '''
# 	tokens = [_.strip(" ") for _ in searchString.split(",")]
# 	for i, aToken in enumerate(tokens):
# 		tokens.pop(i)
# 		if '|' in aToken:
# 			tokens.insert(i, aToken.split('|'))
# 		else:		# explicitly convert to list
# 			tokens.insert(i, [aToken])
# 	[(x, y, z) for x in tokens[0] for y in tokens[1] for z in tokens[2]]
# 	return parse(tokens)
