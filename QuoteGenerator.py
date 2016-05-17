SpecialAffixes = {
	"HOT":"hot",
	"COLD":"cold",
	"PIG": "Pig",
	"VERYLOW": "very low",
	"BURNT": "burnt",
	"INGROUND": "sleeping",
	"ITEM": "held",
	"ACTIVE": "active",
	"STUMP": "stump",
	"PLANTED": "planted",
	"WITHERED": "withered",
	"NOHONEY": "no honey",
	"FULLHONEY": "full of honey",
	"SOMEHONEY": "some honey",
	"DONE": "finished",
	"COOKING_LONG":"cooking, long time left",
	"COOKING_SHORT":"cooking, short time left",
	"NEEDSFERTILIZER": "needs fertilizer",
	"DRYINGINRAIN": "drying in rain",
	"WATER": "in water",
	"LOWFUEL": "low fuel",
	"VALID": "full",
	"GEM": "missing gem"



}
Cleaning = {
	"(picked up)": "(held)",
	"(in the ground)": "(planted)",
	"(burned out)": "(out)",
	"(burnt out)": "(out)",
	"(run out)": "(out)",
	" (unpicked)":"",
	"(picked, the remains on the ground)": "(picked)",
	"(inventory)": "(held)",
	" (placed)": "",
	"(turned off)": "(off)",
	"(turned on)": "(on)",
	#"Grass Tuft": "Grass", #now conforming to it, not it to me.
	"Mangrove Tree": "Mangrove",
	"Octopus Chest": "Octo Chest",
	"Elephant Cactus (withered)": "Elephant Cactus (stump)",#withered = normal, had no spot for stump.
	"Cooked Wobster": "Delicious Wobster",
	"Watermelon (cooked)": "Grilled Watermelon",
	"Carrot (picked)": "Carrot",
	"Roasted Seeds": "Toasted Seeds",
	"(summer)": "(empty)",#walruscamp
	"(full with honey)": "(full of honey)",
	"Crock Pot-": "Crock Pot (empty)-",
	"Ash-": "Ashes-",
	"Divining Rod Base": "Divining Rod Holder",
	"Wormhole": "Worm Hole",
	"Bird Egg": "Egg",
	"Spider Hat": "Spiderhat",
	"Star-Sky": "Star-sky",
	"(shaved)": "(naked)",
	"(following)": "(follower)",
	"Eyeplant": "Eyeplant",
	"Lureplant": "Meat Bulb",
	"Quacken Tentacles": "Quacken Tentacle",
	"(closed)": "",
	"Bernie-": "Bernie (active)-",
	"Water Balloon": "Waterballoon",
	"Socket (empty)": "Socket (missing gem)",
	"Focus (incomplete)": "Focus (missing gem)",
	"Focus (charged)": "Focus (full)",
	"Animal Tracks":"Animal Track",
	




}
SpecialNounChange = {
	"Grass-": "Grass Tuft-",
	"Improved Farm": "Basic and Improved Farm",
	"Basic Farm": "Basic and Improved Farm",
	"Net": "Bug Net",
	"Pig Man": "Pig",
	"Gem Stand": "Telelocator Socket",


}
SpecialPrefixes = {
	"DISEASED": "Diseased ",
	"POISON": "Poison ",
	"DEAD": "Dead ",#idk if actually doing anything
	"LIMITED": "Sick ",#1  way worm hole

}
PicRename = {               #After overwriting lines, replaces pics that dont exist with pics already on the wiki.
	"A Lumpy Evergreen": "Lumpy Evergreen",
	"The End is Nigh": "The End is Nigh!",
	"Sand Bag Structure": "Sandbag",
	"Sand Bag": "Sandbag Item",
	"Mangrove Tree": "Mangrove",
	"Basalt1": "Basalt",
	"Walrus Camp Winter": "Walrus Camp",
	"Merm House Shipwrecked": "Merm Hut",
	"Slotmachine": "Slot Machine",
	"Octopus Chest Build": "Octo Chest",
	"Poison Hole": "Poisonous Hole",
	"X Marks The Spot": "X Marks the Spot",
	"Mushtree": "Blue Mushtree",
	"MushtreeRed": "Red Mushtree",
	"MushtreeGreen": "Green Mushtree",
	"Monkey Totem": "Splumonkey Pod",
	"Ancient": "Ancient Statue",
	"Relic Chair": "Relic",
	"Rook": "Clockwork Rook",
	"Damaged bishop": "Damaged Bishop",
	"Damaged Clockwork": "Damaged Rook",
	"Ghost Build": "Ghost",
	"WeeTusk": "Wee MacTusk",
	"Abigail build": "Abigail",
	"Cooked Wobster": "Delicious Wobster",
	"Cooked Coconut": "Roasted Coconut",
	"Cooked Coffee Beans": "Roasted Coffee Beans",
	"Webberskull": "Webber's Skull",
	"Gramophone": "Maxwell's Phonograph",
	"Minetranspattempt2": "Maxwell's Mosquito Trap",
	"Rock charcoal": "Charcoal Boulder",
	"Ash Tree": "Burnt Ash Tree",
	"Meaty Stew": "Deadly Feast",
	"Maxwell Head": "Maxwell's Head",
	"Basic Farm}}{{Pic32|Turbo Farm Plot":"Basic and Improved Farm",#hax
	"PickSlashAxe": "Pick/Axe",
	"Berry bush Juicy": "Juicy Berry Bush",
	"Rabbit Hole": "Crabbit Den",
	"Ornate Chest": "Large Ornate Chest",
	"Mermhouse Fisher": "Fishermerm's Hut",
	"Sinkhole": "Plugged Sinkhole",
	"Withered Elephant Cactus": "Elephant Cactus",
	"Elephant Cactus": "Prickly Elephant Cactus",
	"Elephant Cactus Stump 2": "Elephant Cactus Stump",
	"Eyeplant":"Eye Plant",
	"Lureplant": "Meat Bulb",
	"Star-Sky": "Star-sky",
	"Lavae": "Extra-Adorable Lavae",
	"Grass Tuft": "Grass",
	"Telebase": "Telelocator Focus",
	"Telelocator_Focus": "Telelocator Socket",
	#"": "",
	#"": "",
	#"": "",
	#"": "",
	#"": "",
	#"": "",
	#"": "",
	#"": "",
	#"": "",
	#"": "",
	#"": "",
	#"": "",
	#"": "",
	#"": "",
	#"": "",
	#"": "",
	#"": "",
	#"": "",
	#"": "",
	#"": "",
	#"": "",
	#"": "",
	#"": "",
	#"": "",
	#"": "",
}
def CreateNameDict(Source):
	f = open(Source)
	NameDict = {}
	cname = None
	for line in f.readlines():
		if cname:
			cname = cname.replace("WORMHOLE_LIMITED_1","WORMHOLE_LIMITED")
			cname = cname.replace("SLOW_","")#farms have same quotes
			cname = cname.replace("FAST_","")
			NameDict[cname] = line[7:-2]
			cname = None

		elif line.startswith('msgctxt "STRINGS.NAMES.'):
			cname = line[23:-2]
		elif line.startswith('msgctxt "STRINGS.DIRECTIONS.'):
			cname = line[28:-2]
	#print(NameDict)
	return NameDict

def CreateQuoteDict(Source, Character):
	NameDict = CreateNameDict(Source)
	Character = Character.upper()
	f = open(Source)
	QuoteDict = {}
	item = None
	for line in f.readlines():
		if item:

			Prefix = ""
			Affix = ""
			Ptemp = ""
			Atemp = ""
			Dug = False
			PicName = ""
			if item[len(item)-7:] == "GENERIC":
				item = item[:-8]
				#print("Minus GENERIC:", item)

			if item.startswith("DESCRIBE"):
				item = item[9:]
				#print("Minus DESCRIBE:", item)

			if item.startswith("ANNOUNCE"):
				item = item[9:]
				#print("Minus ANNOUNCE:", item)

			if item.startswith("DUG"):
				item = item[4:] #-----distinction from non-Dug verison
				Affix = "held"
				Dug = True
				#print("Minus DUG:", item)
			for Case in SpecialPrefixes:
				if item[len(item) - len(Case):] == Case:
					item = item[:len(Case) + 1]
					Ptemp = Case
					Prefix = Prefix + SpecialPrefixes[Case]
					break

			for Case in SpecialAffixes:
				if item[len(item) - len(Case):] == Case:
					#print("--------------------")
					item = item[:len(item) - len(Case)-1]
					Atemp = Case
					Affix = SpecialAffixes[Case]
					#print ("item:", item)
					
					break

			if item.find(".") != -1:
				i = item.find(".")
				Affix = item[i+1:]#-----also removes "."
				if Affix not in SpecialAffixes:
					try:
						Affix = NameDict[Affix]
					except KeyError:
						Affix = Affix.lower()
				item = item[:i]
			if Affix:
				Affix = " ({})".format(Affix)


			for Case in SpecialNounChange:
				try:
					if NameDict[item] == Case:
						NameDict[item] = SpecialNounChange[Case]
						break
				except KeyError:
					pass
			#print("Affix:", Affix)
			#print("Minus Affix:", item)
			#print("----------------")


			if Dug and "DUG_" + item in NameDict:
				#print("DUG_" + item)
				PicName = NameDict["DUG_" + item]
			if item + "_" + Ptemp in NameDict:
				#print(item + "_" + Ptemp)
				PicName = NameDict[item + "_" + Ptemp]
			elif item + "." + Ptemp in NameDict:
				#print(item + "." + Ptemp)
				PicName = NameDict[item + "." + Ptemp]

			elif item + "_" + Atemp in NameDict:
				#print (item + "_" + Atemp)
				PicName = NameDict[item + "_" + Atemp]

			elif item + "." + Atemp in NameDict:
				#print (item + "." + Atemp)
				PicName = NameDict[item + "." + Atemp]

			elif item in NameDict:
				PicName = NameDict[item]
			if PicName:
				#print("PicName: ", PicName)
				#print("--------------------")
				pass


			try:
				#print("item:", item)
				#print("NameDict[item]:", NameDict[item])
				if item == "COMPASS":
					pass
				else:
					QuoteDict[Prefix + NameDict[item]+ Affix] = [line[6:-1], PicName]
				#print("IGN:", NameDict[item])
				#print("––––––––––––––––––––––––––––––––––––––––{}- {}".format(Prefix + NameDict[item] + Affix, QuoteDict[Prefix + NameDict[item] + Affix][0]))
			except KeyError:
				#print("====Not in Dictionary====")
				item = item.replace("_"," ")
				item = item.replace("."," ")
				item = item.replace("\"","'")
				item = item.title()
				#print("Cleaned Action:", Prefix + item + Affix)
				QuoteDict[Prefix + item + Affix] = [line[6:-1], PicName]
				#print("––––––––––––––––––––––––––––––––––––––––{}- {}".format(Prefix + item + Affix, QuoteDict[Prefix + item + Affix][0]))
			item = None

		elif line.startswith('msgctxt "STRINGS.CHARACTERS.{}'.format(Character)):
			item = line[29 + len(Character):-2]
			#print ("Raw action:",item)
	try:
		del QuoteDict[""]
	except:
		pass
	#print(QuoteDict)
	return QuoteDict

def EnterQuotes(Source, Character, InputFile, OutputFile):
	print("========================================")
	print("Using Source: {}".format(Source))
	Character = Character.upper()
	if Character == "WILSON": #no Quotes are actually labelled for Wilson, he is the generic.
		Character = "GENERIC"
	elif Character == "WIGFRID":
		Character = "WATHGRITHR"
	QuoteDict = CreateQuoteDict(Source, Character)
	NameDict = CreateNameDict(Source)
	Used = []
	Input = open(InputFile)
	Output = open(OutputFile, "w")
	#print("Quotes added:")
	for line in Input.readlines():

		for Case in Cleaning:
			line = line.replace(Case, Cleaning[Case])
		
		for key in QuoteDict:
			temp = QuoteDict[key][0]
			if Character == "WATHGRITHR":
				temp = temp.replace("o", "ö")
				temp = temp.replace("O", "Ö")

			PicName = QuoteDict[key][1]
			Icon = "{}{}{}".format("{{Pic32|", PicName, "}}")
			#print ("Name: {}|Quote: {}|PicName: {}".format(key, temp, QuoteDict[key][1]))
			if line.find("*{}-".format(key)) != -1:
				
				if PicName:
					line = "*" + Icon + "{}- {}\n".format(key, temp)
				else:
					line ="*{}- {}\n".format(key, temp)
				break


			elif line.find("] {}-".format(key)) != -1 or line.find("]{}-".format(key)) != -1:

				if PicName:
					line = "*" + Icon + "{}- {}\n".format(key, temp)
				else:
					line ="*{}- {}\n".format(key, temp)
				break


			elif line.find("{} {}-".format("}", key)) != -1 or line.find("{}{}-".format("}", key)) != -1:

				if PicName:
					line = "*" + Icon + "{}- {}\n".format(key, temp)
				else:
					line ="*{}- {}\n".format(key, temp)
				break
		for Case in PicRename:
			line = line.replace(PicRename[Case] + "}", Case + "}")
		Output.write(line)
	else:
		Unused = open("unused_" + Character + ".txt", "a")
		Unused.write("––––––––––––––––––––––––––––––––––––––––\n")
		UnusedR = open("unused_" + Character + ".txt", "r")
		
		for key in QuoteDict:
			if Input.read().find("*{}- {}".format(key, QuoteDict[key])) == -1:
				if UnusedR.read().find("*{}- {}\n".format(key, QuoteDict[key])) == -1:
					Unused.write("*{}- {}\n".format(key, QuoteDict[key]))



		print("––––––––––––––––––––––––––––––––––––––––")
		"""if Used != "": #----------shows actions found in source but couldn't find/place in file. The file here isn't the prettiest.
			UnusedOld = open("unused_old_" + OutputFile, "w")
			print("Quotes not used in {}".format("unused_" + OutputFile))
			for key in Used:
				del QuoteDict[key]
			for key in QuoteDict:
				UnusedOld.write("*{}- {}\n".format(key, QuoteDict[key]))"""
		print('Exported to "{}"'.format(OutputFile))
		print("Done!")
def GetQuote(Source, Character, entity):
	Dict = CreateQuoteDict(Source, Character)
	try:
		return Dict[entity]
	except:
		pass






Character = input("Character (file should also be named Character.txt):")
#EnterQuotes("strings.pot",input("Character DebugSpawn: "), input("Import file (e.x. file.txt) :"), input("Export file (e.x. file.txt) :"))
EnterQuotes("stringsDST.pot",Character, Character + ".txt", Character + "temp.txt")
EnterQuotes("strings.pot",Character, Character + "temp.txt", Character + "_Export.txt")
