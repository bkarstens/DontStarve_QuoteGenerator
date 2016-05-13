SpecialCases = [
	"HOT",
	"COLD",
] # in dictionary as "overheating" and "freezing." Allows to find items like heatrock (hot).

def CreateNameDict(Source):
	f = open(Source)
	names = {}
	cname = None
	for line in f.readlines():
		if cname:
			names[cname] = line[7:-2]
			cname = None

		elif line.startswith('msgctxt "STRINGS.NAMES.'):
			cname = line[23:-2]
	return names

def CreateQuoteDict(Source, Character):
	names = CreateNameDict(Source)
	Character = Character.upper()
	f = open(Source)
	quotes = {}
	caction = None
	for line in f.readlines():
		if caction:

			Prefix = ""
			Affix = ""

			if caction[len(caction)-7:] == "GENERIC":
				caction = caction[:-8]
				#print("Minus GENERIC:", caction)
			if caction[len(caction)-8:] == "DISEASED":
					caction = caction[:-9]
					Prefix = Prefix + "Diseased "
					#print("Minus DISEASED:", caction)
			if caction.startswith("DESCRIBE"):
				caction = caction[9:]
				#print("Minus DESCRIBE:", caction)

			if caction.startswith("ANNOUNCE"):
				caction = caction[9:]
				#print("Minus ANNOUNCE:", caction)

			if caction.find(".") != -1:
				i = caction.find(".")
				Affix = caction[i+1:]#-----no "."
				if len(Affix) > 2 and Affix not in SpecialCases:#--------------min length 3 so compass directions stay caps
					try:
						Affix = names[Affix]
					except KeyError:
						if Affix == "VERYLOW":
								Affix = Affix[:4] + " " + Affix[4:]
						Affix = Affix.lower()
				if Affix == "PIG":
					Affix = Affix.capitalize()
				else:
					Affix = Affix.lower()		
				Affix = " ({})".format(Affix)
				#print("Affix:", Affix)
				caction = caction[:i]
				#print("Minus Affix:", caction)
			try:
					#print("IGN:", names[caction])
					quotes[Prefix + names[caction]+ Affix] = line[6:-1]
					#print("––––––––––––––––––––––––––––––––––––––––{}- {}".format(Prefix + names[caction] + Affix, quotes[Prefix + names[caction] + Affix]))
			except KeyError:
				#print("====Not in Dictionary====")
				caction = caction.replace("_"," ")
				caction = caction.replace("."," ")
				#caction = caction.replace("\"","")
				caction = caction.capitalize()
				#print("Cleaned Action:", caction)
				quotes[Prefix + caction + Affix] = line[6:-1]
				#print("––––––––––––––––––––––––––––––––––––––––{}- {}".format(Prefix + caction + Affix, quotes[Prefix + caction + Affix]))
			caction = None

		elif line.startswith('msgctxt "STRINGS.CHARACTERS.{}'.format(Character)):
			caction = line[29 + len(Character):-2]
			#print ("Raw action:",caction)
	return quotes

def EnterQuotes(Source, Character, InputFile, OutputFile):
	print("========================================")
	print("Using Source: {}".format(Source))
	Character = Character.upper()
	if Character == "WILSON": #no quotes are actually labelled for Wilson, he is the generic.
		Character = "GENERIC"
	QuoteDict = CreateQuoteDict(Source, Character)
	Used = []
	f = open(InputFile)
	Appendedf = open(OutputFile, "w")
	print("Quotes added:")
	for line in f.readlines():

		for key in QuoteDict:

			if line.find("*{}- {}".format(key, QuoteDict[key])) != -1:
				if key not in Used:
					Used.append(key)
				break

			if line.find("*{}-\n".format(key)) != -1: #----------if spot doesnt have " "
				temp = QuoteDict[key]
				if Character == "WATHGRITHR":
					temp = temp.replace("o", "ö")
					temp = temp.replace("O", "Ö")
				index = line.find("*{}-\n".format(key))
				line = line[:index + len(key)+2] + " " + temp + line[index + len(key)+2:]
				print (line)
				if key not in Used:
					Used.append(key)
				index = None
				break

			elif line.find("*{}- \n".format(key)) != -1: #----------if spot has " "
				temp = QuoteDict[key]
				if Character == "WATHGRITHR":
					temp = temp.replace("o", "ö")
					temp = temp.replace("O", "Ö")
				index = line.find("*{}- \n".format(key))
				line = line[:index + len(key)+3] + temp + line[index + len(key)+3:]
				print (line)
				if key not in Used:
					Used.append(key)
				index = None
				break


		Appendedf.write(line)
	else:
		print("––––––––––––––––––––––––––––––––––––––––")
		"""if Used != "": #----------shows actions found in source but couldn't find/place in file. The file here isn't the prettiest.
			Appendedm = open("unused_" + OutputFile, "w")
			print("Quotes not used in {}".format("unused_" + OutputFile))
			for key in Used:
				del QuoteDict[key]
			for key in QuoteDict:
				Appendedm.write("*{}- {}\n".format(key, QuoteDict[key]))"""
		print('Exported to "{}"'.format(OutputFile))
		print("Done!")
def GetQuote(Source, Character, entity):
	Dict = CreateQuoteDict(Source, Character)
	try:
		return Dict[entity]
	except:
		pass






Character = input("Caracter DebugSpawn (file should also be named Character.txt):")
#EnterQuotes("strings.pot",input("Character DebugSpawn: "), input("Import file (e.x. file.txt) :"), input("Export file (e.x. file.txt) :"))
EnterQuotes("strings.pot",Character, Character + ".txt", Character + "temp.txt")
EnterQuotes("stringsDST.pot",Character, Character + "temp.txt", Character + "_Export.txt")