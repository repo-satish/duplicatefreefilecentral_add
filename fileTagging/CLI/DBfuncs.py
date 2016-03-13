'''
	all functions dealing directly with DBengine which need to be ABSTRACT
	to be able incorporate various DB technologies.
'''

import basicUtil

centeralDBfile = ""																# full path to program's store of folders it has tracked, static cz we already know it
addedList, modifiedList, removedList = list(), list(), list()

class anEntry_(xx):																# DB, class:: it is a meta-class thingy, if it can be satisfactorily implemented, it would be great for fns - renameFile, assignTags & searchFor
	'''
		object to hold the entire entry-stuff into a single
		easily(-n-universally) accessible variable
		this is ABSTRACTION
	'''
	def __init__(self, arg):
		super(anEntry_, self).__init__()
		self.arg = arg

	self.UID = # type BSON, stringed
	self.Name = # type string
	self.TAGs = # type list of strings
	self.OldName = # type list of strings
	self.EtC = 

	def getInfo(self, fileName):	# controversial, then why don't you just provied a fn to execute raw strings in DB environment n return DB engine's reply
		# ideally it should be getInfo(self, value="abc.pdf", fieldName="fileName/tag/sha1") -- how to do it
		pass

	def updateInfo(self, fieldName, from, to, searchBy):
		pass

	def delete(self, fileName):
		pass



# following are fns dealing with TAG ONLY-n-DIRECTLY
def listAllTags():
	pass

def createNewTags(newTagsList):
	'''
		remember to return the corrected tagList i.e. the original
		newTagsList minus theTyposWhichUserAccidentallyEntered
	'''
	pass							# here's a list of all tags u have created. Check if _ is a typo or you want to add a new tag.

def renameExistingTag(oldName, newName):
	'''
		heaviest COZ it must find-n-replace that tag throughout
		the entire DB
	'''
	pass



# --------------------------------------------------------------------------------

def iFiM_(present_fileName):													# if File Internally Modified?
	x = os.stat(present_fileName)												# refer `class os.stat_result` in Python 3.4.3 docs.chm
	sysSays = [basicUtil.calcSHA1(os.path.join(".",present_fileName)), x.st_mtime, x.st_ctime]
	dbSays = # DB, class::	fetch SHA1, st_mtime and st_ctime stored in DB i.e. its last known recorded value
	# now decide weather the file has changed or not and return True(yes it is internally modified) or Flase

def scan_():
	'''
		scans everything in CWD, stores it in a variable/temp_file
		and returns it. Used by reportChanges().
	'''	#  The result of scanning may get extremely large - pickle it?
	fileList, folderList = list(), list()
	for root, dirs, files in os.walk(".", topdown=True, onerror=None, followlinks=False):
		if root is ".":
			fileList = files
			folderList = dirs
		else:
			break
	try:
		folderList[0]
	except IndexError:
		return fileList
	else:
		print(stringStore.bgTasks.scan_)
		basicUtil.quit("failure")

def initiateDB():
	'''
		create `localDBfile` in "." and send CWD to `centeralDBfile` and thats it
	'''
	pass# DB::	

def reportChanges():
	'''
		call scan_() and use its `return`ed value for comparisions against
		existing `localDBfile`, report changes AND as a responsibility destroy temp_file created by scan_()
		REMEMBER-- list of files now_added_to_PoolDirPath PLUS files_tracked_in_DB_with_no_tags
	'''
	newList = scan_()
	dbList = # DB::	get complete list of fileNames stored in localDBfile
	for _ in dbList:
		if _ in newList:				# present teacher
			if iFiM_(_):				# => MODIFIED_without_changing_name
				while True:
					r = input(stringStore.DBfuncs.reportChanges % locals())
					if r in "oO":
						os.startfile(_)
					elif r in "dD":
						# ask SO how to open dir with THIS file selected
					elif r in "yY":
						# DB::	ok, nice to know NOW update DB appropriately
						break
					elif r in "nN":
						removedList.append(_);						break
					else:
						modifiedList.append(_);						break
			else:
				pass					# the only normal case
		else:							# absent
			sha1 = basicUtil.calcSHA1(os.path.join(".",present_fileName))
			if :						# DB::	return True --IFF-- sha1 exists in DB albeit with a different name ofcourse # RENAMED_WOUT_PERMISSION
				# DB::	update fileName in DB to _, querying by sha1
				print("Naughty User! Behave yourself.")
			else:
				removedList.append(_)

	newNames = list(  set(newList).difference(set(dbList))  )	# newGuys -- mera naam to aaya hi nahi
	for _ in newNames:
		sha1 = basicUtil.calcSHA1(os.path.join(".",present_fileName))
		if :						# DB::	return True --IFF-- sha1 exists in DB albeit with a different name ofcourse # RENAMED_WOUT_PERMISSION
			# DB::	update fileName in DB to _, querying by sha1
			print("Naughty User! Behave yourself.")
		else:
			addedList.append(_)

	if len(removedList) is 0:
		return
	else:
		from bgTasks import makeLog
		makeLog(removedList)
		print(stringStore.DBfuncs.reportChanges)
		basicUtil.quit("failure")

def searchFor(strng):
	# AND condition between successive tag_names given in the strng
	# HOPING that if no matches are found DB engine politely return a string like "No matches found"
	# get a list of fileNames (UIDs shall anEntry_ succeed) which meet the search criteria in list form
	final = "\n --- Results for searching %(strng)s --- \n" % locals()
	for _ in fileNames:
		# final+= " " + SrNo + ". " + _ + "\n\t" + basicUtil.colorize(  getInfo(_).tags.join(", "), "BLUE"  ) + "\n"
		# don't use static variable of this class to keep track of SrNo, basicUtil's lessDisplay should handle it
	return final

def renameFile(from, to):
	# just as with getInfo(), this fn should be like updateInfo(from="a", to="b", fieldName="fileName")
	pass

def assignTagsToFile(fileName, tags):
	'''
		erase all previously assigned tags and insert given value
	'''
	# just as with getInfo(), this fn should be like updateInfo(from=nt_needed??, to="b p,c", fieldName="tags")
	pass
