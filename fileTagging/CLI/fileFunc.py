import os
import stringStore, basicUtil, DBfuncs, bgTasks

allTags = DBfuncs.listAllTags()

def search():
	searchStr = input(stringStore.fileFunc.search % ", ".join(allTags))
	tokens = list(  explode(searchStr(",")).trim(" ")  )	# really, how to do this in python, use regex?
	# if `tokens` is exactly a subset of `allTags` ONLY then proceed, otherwise tell which tag is not-at-all there in DB and `return`
	results = ""
	for _ in bgTasks.expandSearchString(searchStr):
		results+= DBfuncs.searchFor(_)
	basicUtil.lessDisplay(results)
	return



 

def getTheName_(purpose):
	'''
		finds usage in both rename() and modify()
	'''
	blah = "rename"	if purpose is 'r' else "modify tags of"
	choice = input(stringStore.fileFunc.getTheName_ % blah)
	if choice is 1:
		fileName = raw_input("\nOkay, enter the exact file name:\n")
		if os.path.isfile("path"+fileName):
			return fileName
		else:
			print("Said file doesn't exist in -- main \"Pool\" folder")
	elif choice is 2:
		search()
		return fetch_from_clipBoard()
	return #None

def rename():
	fileName = getTheName_('r')
	newName = input(stringStore.fileFunc.rename % fileName)
	DBfuncs.renameFile(fileName, newName)
	print("File renamed successfully.")
	return



 

def create_():
	'''
		finds usage in both create() and modify()
	'''
	tags = input(stringStore.fileFunc.create_)
	if tags is None:								# what does input() return when no string is entered and `Enter` is pressed directly?
		return 0
	elif tags is "--AVOID--":
		return -1

	tags = list(  explode(tags(",")).trim(" ")  )	# really, how to do this in python, use regex? see 2nd line of search()
	newTags = list()			# FIND a more pythonic way of doing the next 5 lines, REMEMBER to UNIQUEize each list via `x=list(set(x))`
	for _ in tags:
		if _ in allTags:
			pass
		else:
			newTags.append(_)
	if len(newTags) > 0:
		validTags = DBfuncs.createNewTags(newTags)

	DBfuncs.assignTagsToFile(aFile, validTags)
	return 1

def create():
	newOnes = bgTasks.getNewFilesList()
	for aFile in newOnes:
		basicUtil.clrscr()
		print(aFile)
		print("\n\nList of TAGs you have already created:\n%s" % ", ".join(allTags))
		job = create_()
		if job is 0:
			continue
		elif job is -1:
			return
		elif job is 1:
			choice = input(stringStore.fileFunc.create)
			if choice in "yY":
				basicUtil.clrscr()
				rename()
		else:
			break
	return



 

def modify():
	fileName = getTheName_('m')
	oldTags = DBfuncs.getInfo(fileName).tags 		# will this fnName().subObject syntax work?
	print(  stringStore.fileFunc.modify % (fileName, ", ".join(oldTags), ", ".join(allTags))  )
	job = create_()
	if job is 0:
		DBfuncs.assignTagsToFile(fileName, "")
	elif job is 1:
		print("\n\nChanges made in tagging information of said file successfully updated.")
	else:								# this should never occour
		basicUtil.quit(1)
	pass



def quit():
	"""
		quit() -- hibernative snapshot, when a user is tired s/he quits

		call `DBfuncs._scan()` and literally quit the program. Next
		time when program runs, `bgTasks.getPoolDirPath()` will be called,
		inside it call `DBfuncs.reportChanges()` iff the remanant temp.sqlite3
		of `DBfuncs._scan()` called during previous run exits in
		`poolDirPath\`
	"""
	pass
