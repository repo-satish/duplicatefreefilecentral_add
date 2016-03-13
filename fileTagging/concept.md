# The Idea
MongoDB File Manager with Python Frontend

## Expectations
One stop solution for all my file sorting, categorising and managing needs.
Ability to TAG files, in a cross-platform & neat manner.
	Hence, avoid FS dependent file meta properties or tagging for that matter, also do not insert tags in file name itself in CSV style - that's just plain ugly.
Ability to atleast detect changes made in file (happens when bookmarks/annotations are made) raise ticket and ask appropriate questions.
	Therefore, instead of SHA1 of file as UID use mongo's inbuilt UID as primary key. Ticket implies a dialog box which asks appropriate questions which can be like - would you like to edit tags of this file (mostly unlikely), write a summary of the changes made, would you like to keep a backup copy of the unmodified file in REPO (OMG-versionControl)
Beautiful, fast & intutive interface.
	I wish I could define beautiful. Fast implies that all functions should be readily available. Intutive - don't show off vocab. skills, just use simple english, UI that feels natural to the masses & not just me.
Take inspiration from `7zFM.exe` and add on things to it.
	Ability to selectively-display-on-demand and sort by fields like Name, DOC, DOM, Size, Format, etc.
	Right pane dedicated entirely for managing TAGs, its wireframe consists of-
		1. Search Bar -- TAG suggestion and for searching files with multiple TAGs u can do like `abc & def` or `abc | def`
		2. Image preview?
		3. TAGs assigned to the file selected, if no file is selected then show TAG popularity cloud.
		4. double clicking on a TAG shows all files TAGed by that tag in DB

## Questions
MongoDB or SQLite?
	MongoDB cuz its cool, trendy and most importantly worth learning.
	SQLite because its well - light in weight and easy on system resources.
	Hence - initial builds (meant only for running on single computer) will run SQLite behind the scenes but for learning and future (i.e. when going for the enterprise-cloud-massive-multipleDevices version) builds use MongoDB.
Breadcrumbs?
	Never, the entire point is to avoid making folders inside folders inside folders... All files are pooled in one big folder. Each file has one-and-only-one major TAG(which is kinda like file's category) and several minor TAG - when you search for a tag, say `abc`, all files having `abc` as their major tag appear first, followed by files having `abc` as their minor tag.
	**ASSUMPTION & INSTRUCTION** to user-- it is the responsibility of user to write/arrange tags assigned to a file in decreasing order of relevance i.e. most natural/likely/appropriate tag comes first then come helping tags.
______________________________________________________________________________

## Data-Structure
something like
	> UID   -- [SHA1] -- Real Name when Downloaded -- Given Name -- [TAGs]
	> const -- var    -- const                     -- var        -- var

## PseudoCode
MetaStep 1. merge all HTM(L) files and their respective (associated) folders into one unit using `Store` level compression.
MetaStep 2. everytime the program runs, check for newly_added/previously_untagged files in PoolFolder. NO there is nothing like .hgignore or .gitignore here :(
MetaStep 3. once the program is up & running use a different thread to cross-check SHA1s of all files to detect modifications.
Show the user info from MetaStep 2 & 3 constantly, at bottom of each screen in different color (blue?)

### CLI version
The most initial builds will work with csv DB until proficient in SQLite. Hence **implement abstraction**
Create
	0. display all files in a folder one-by-one, followed by newline chacter, followed by a list of tags already invented.
		In the bg, calculate the SHA1 of file being worked upon, this is the initial SHA1 which is coupled with UID
	1. user then types the list of tags s/he thinks are appropriate in decreasing order of relevance.
		> if user is tired/not_sure/doesn't_want to do tagging of that file, s/he types `--AVOID--` to skip to next file
		> if new tag is seen, explicitly ask user's permission "New tag name _tag_ found, do you want to create n insert it into AllTagsDB?", after all it could be a spelling mistake. ?Suggest 3-5 auto-corrects based on LevDistance?
		> if tag exists in DB but case is changed, prompt user `Did you mean "ABc" when you typed "abC"?` If yes, apply corrected tag name, if no ask user to decide which is the *one correct* way to write that tag's name & update DB accordingly
	2. offer user a chance to rename the file if s/he thinks it is required (readability, name too long/cryptic, etc.).
		Recalculate SHA1 **has it has changed**
Search
	0. `print("(You can use \'&\' for AND and \'|\' for OR)\n\n")` `print("Search:\n  \n\nTAGs:\n[%s]", TAGs.join(", "))`
		> it is important to show a list of all existing tags in DB so user doesn't have to guess spellings or avoid inventing new ones when coming back to work after long vacation, and then auto-complete feature isn't implemented yet.
	1. Take cursor (represented by `_`) back to `Search:\n  _` now user will type the search string.
		> make the bg search algorithm smart enough to tackle queries like `(abc | def) & (ghi | jkl | uvw)`
	2. Display results on a new screen, EXPLOIT `LESS.sh` if list is too long.
		The format should be like-- SrNO then file name then newline_followed_by_2_spaces then the tags assigned to that particular file. Note that the tagging info should appear in a different color (dark green?).
	3. User can enter `open SrNO` to open the file, if dissatisfied continue searching from where s/he left-off.
Modify
	0. print("Which file's tagging info do you wish to modify?\n\ta- mention exact file name\n\tb- search for file via tags")
	1a. if file found in PoolFolder, continue with step2, if not show user error n then step0 screen. It doesn't matter if the file is currently untagged or not but the bottom status bar should change accordingly **ponder**
	1b. Search utility runs and in step3 instead of `open SrNO` user types `mod SrNO` and then flow passes back to Modify.exe
	2. Display file name followed by other info (if it looks cool) and then list of tags assigned to it and finally list of all tags. User then enters the tags s/he wishes to assign in decreasing order of relevance, no luxury like `+abc +"def ghi" -xyz`
	-- how to track files which do not have any tags assigned? --
Pressing `Esc` at any point takes you back to the previous logical screen or directl back to the welcome screen.

FilesDB.csv-------------------------------------------------------------------------------------------+
UID,	OriginalName,			SHA1s,					NewName,				TagsAssigned		  |
b9a,"NiceSong[TPB].mp3","34ibv32udi,oe43j3mkwb","Nice Song (Artist).mp3","Indie,Rock,Hip Hop,Electric"|
c21,"BadSong[Yify].flac",	"sd6fa87e6f",		"Bad Song (Artist).flac","Jazz,Dance"				  |
______________________________________________________________________________________________________/

TAGs.txt------------------------------+
Indie,Rock,Hip Hop,Electric,Jazz,Dance|
______________________________________/


QQ.... both `fileFunc.py->create()` and `homeScreen.py` call `rename()`, is it possible for `return` to return flow to the page which called it??

### GUI version
eventually number of tags will become too large to be displayed in a sane manner on screen, hence when listing all tags currently existing in the DB (to help user pick/make_new tags), give option to sort by popularity/recently_created/size/activity/least_used
For Storage & BackUpFrequency issues it would be wise to divide main Pool folder into sub dirs like eBooks,VIDs,compressed,EXE,etc. - in which case DB should be able to see through `main_Pool_folder\<sub-dir-name>` and treat all files as if they were present in main_Pool_folder. But sub-foldering STOPS RIGHT HERE, NO WAY does `main_Pool_folder\<sub-dir-name>\` contain another sub-folder like `AVI\` or `INSPIRATIONAL\`.
?? Take natural/obvious/intutive(ok, not intutive) interTAG inheritance in account for better search experience ??--
	e.g. tags like
		- `bbc` and `ffm` would always come under `porn`
		- `PAWG` and `MILF` may come under either `porn` or something else(`sizzling song vids`) :: 80-20 chance
		- `ass`, `bum` and `booty` may come under either `porn` or something entirely different :: 30-70 chance
	also, who defines such inheritance - user or trend-analysis-among-masses
______________________________________________________________________________________________________

## Optimzations
TryExceptElseFinally is musch faster than if else
instead of doing `if str1 in str2` optimize with regex
______________________________________________________________________________________________________

## To Do
add forgetDir() and mergeDirs()