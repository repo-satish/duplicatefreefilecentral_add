import os, sys
import shutil
import hashlib
from functools import partial

class UncleanDirectory(Exception):
	def __init__(self, root):
		print("Fatal Error, directory found at `%(root)s`; it should not have existed" % locals())
		sys.exit(0)

class Interactor():
	""" handles user interaction """
	jobs = list()
	bn = lambda x: os.path.basename(x)

	@classmethod
	def notify(fifc, copies):
		""" called when the file under observation is already
		present in file_central. So no need to copy, but the
		user must be aptly informed """
		if len(copies) is 1:
			if bn(fifc) is bn(copies[0]):
				pass
			else:
				ch = input("`%s` <in %s> is already present in file_central as `%s`. Update name? (y/n) [n]\n" % (bn(copies[0]), os.path.split(copies)[0], bn(fifc)))
				if ch in 'yY':
					os.ren(fifc, bn(copies[0]))
		else:
			print("The file `%s` in file_central is present in alien directory as follows:\n\n" % bn(fifc))
			for i, aFile in enumerate(copies):
				print("%d. `%s` in <%s>" % (i, bn(aFile), os.path.split(aFile)[0]))
			ch = input("If you wish to rename `%s`, you may enter:\n\t1. index from above list\n\t2. `n` to type-in a new name\n\t3. `return` to ignore this prompt" % bn(fifc))
			if ch in 'nN':
				newName = input("Enter new name")
				os.ren(fifc, newName)
			elif ch is '':
				pass
			else:
				os.ren(fifc, copies[int(ch)])
		return

	@classmethod
	def batch(fifc, copies):
		""" called when file under consideration is entirely
		new and not present in file_central, so besides just
		deciding a name, we must perform file copy operation
		from alien directory to file_central """
		if len(copies) is 1:
			fileToCopy = copies[0]
		else:
			print("The following files are internally same but have either different names or locations or both:\n\n")
			for i, aFile in enumerate(copies):
				print("%d. `%s` in <%s>" % (i, bn(aFile), os.path.split(aFile)[0]))
			ch = input("\nSo it will be copied as one file. Please input index of file name you want to keep: ")
			fileToCopy = copies[int(ch)]
		if os.path.isfile(  os.path.join(os.path.split(fifc)[0], bn(fileToCopy))  ):		# change name
			newName = input("Another file with same name (i.e. `%s`) is present in file_central, please enter a different name for this file:\n" % bn(fileToCopy))
			shutil.copy2(fileToCopy, os.path.join(os.path.split(fifc)[0], newName))
			jobs.append("RENAMED & COPIED `%s` from `%s` to `%s` as `%s`" % (fileToCopy, os.path.split(fileToCopy)[0], os.path.split(fifc)[0], newName))
		else:		# shutil copy
			shutil.copy2(fileToCopy, os.path.split(fifc)[0])
			jobs.append("COPIED `%s` from `%s` to `%s`" % (fileToCopy, os.path.split(fileToCopy)[0], os.path.split(fifc)[0]))
		return

	@classmethod
	def jobsDump():
		print("SUMMARY OF COPY JOBS PERFORMED")
		print(  '\n'.join(jobs)  )
		return

def createMap(locn):	#?-- use multi-threading here?
	""" creates a dict of files inside locn (raises
	FatalError if any directory is found). dict has
	keys as SHA1 of files and their values contain a
	list of files which have that SHA1 """
#---TEST_BEG okay---
	def calcSHA1(filePath):
		CHUNK_SIZE = 128
		d = hashlib.sha1()
		with open(filePath, mode="rb") as f:
			for buf in iter(partial(f.read, CHUNK_SIZE), b''):
				d.update(buf)
		return d.hexdigest()
#---TEST_END okay---
#---TEST_BEG okay---
	def listAllFiles(x):
		allFiles = list()
		for root, dirs, files in os.walk(x):
			if len(dirs) != 0:
				err(root)
			allFiles+= [os.path.join(root, _) for _ in files]
		return allFiles
#---TEST_END okay---
#---TEST_BEG pending---
	hashes = dict()
	for _ in listAllFiles(locn):
		x = calcSHA1(_)
		# hashes[x]+= full if x in hashes.keys() else hashes[x] = [full]
		try:
			hashes[x].append(full)
		except IndexError:
			hashes[x] = [full]
	return hashes
#---TEST_END pending---

def cleanup(path):
	for root, dirs, files in os.walk(fileCentral):
		if "_files" in dirs or ".htm" in files:
			try:
#---TEST_BEG pending---
				import webpageSanitize as x
				x.silentClean(root)		# build carefull --- EXTERNAL
#---TEST_END pending---
			except ImportError:
				input("Critical dependency missing, please re-install")
				sys.exit(0)
	return

def main(fileCentral, alien):
	for _ in os.listdir(fileCentral):
		if os.path.isdir(_):
			raise UncleanDirectory(fileCentral)
	cleanup(alien)
	big, small = createMap(fileCentral), createMap(alien)
	for _ in small.keys():
		if _ in big.keys():			# do not copy, notify if file name has changed
			Interactor.notify(big[_], small[_])
		else:			# put into file-to-be-copied job list, if os.nameAlreadyExistsError rises when copying then the responsibility of asking user which name to keep is handled by someone else
			Interactor.batch(big[_], small[_])
	Interactor.jobsDump()
	return

if __name__ == '__main__':
	home, ext = map(input, ["Where is the mothership", "Who wants to come in"])
	home, ext = map(os.path.abspath, [home, ext])
	if os.path.isdir(home) and os.path.isdir(ext):
		main(home, ext)
	else:
		print("Incorrect paths")




