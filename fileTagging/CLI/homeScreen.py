import stringStore, basicUtil, bgTasks

def main():
	"""
		RUN scan_() after every any_call_to_fn_in_DBfuncs
	"""
	bgTasks.getPoolDirPath()
	
	print("\n*8\tPerforming prelimnary checks, please wait . . .")

	delta = bgTasks.#num_NewFilesAdded()
	if delta is 0:
		extra = ""
	else:
		extra =	"\n\tc. Create/Assign tags to %(delta)d currently untagged files." % locals()
	# basicUtil.clrscr()
	choice = input(stringStore.homeScreen.main % extra)

	if choice in "cC":			# create assign tags for currently untagged files OR modify/assign new tags to aleady tagged files
		fileFunc.create() if delta > 0 else basicUtil.quit(1)
	elif choice in "sS":		# search for files on basis of tags
		fileFunc.search()
	elif choice in "rR":		# rename a file safely
		fileFunc.rename()
	elif choice in "mM":		# validate modification detected in files whose names haven't changed
		fileFunc.modify()
	elif choice in "qQ":		# quit the application
		fileFunc.quit()
	else:
		basicUtil.quit(1)

if __name__ == '__main__':
	main()