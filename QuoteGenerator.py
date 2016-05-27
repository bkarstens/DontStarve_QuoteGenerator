Overwrite = False#WARNING: ERROR-PRONE
PicOverwrite = True
Debuging = False
Character = ""
from time import time
from math import floor
SpecialAffixes = {
	"HOT":"hot",
	"COLD":"cold",
	"PIG": "Pig",
	"VERYLOW": "very low",
	"BURNT": "burnt",#----------Not needed, except stupid mangrove
	"INGROUND": "sleeping",
	"ITEM": "held",
	#"ACTIVE": "active",#----------Not needed
	#"STUMP": "stump",
	"PLANTED": "planted",
	#"WITHERED": "withered",#----------Not needed
	"NOHONEY": "no honey",
	"SOMEHONEY": "some honey",
	"FULLHONEY": "full of honey",
	"DONE": "finished",
	"COOKING_LONG":"cooking, long time left",
	"COOKING_SHORT":"cooking, short time left",
	"NEEDSFERTILIZER": "needs fertilizer",
	"DRYINGINRAIN": "drying in rain",
	"WATER": "in water",
	"LOWFUEL": "low fuel",
	"VALID": "full",
	"GEM": "missing gem",
	"SAND": "sand",
	"LONG": "stage 1",
	"MEDIUM": "stage 2",
	"SOON": "stage 3",
	"HAUNTED_GROUND": "ready",
	"HAUNTED_POCKET": "ready, held",
	"CHOPPED": "stump",
	"BLOOM": "blooming",
	"WEBBED": "webbed",
	#"": "",
	#"": "",
	#"": "",
	#"": "",
	#"": "",
}
PicAffixes = [
	"Stump",
	"Withered",
	"Burnt",
	"Picked",
	"Planted",
	"Sleeping",
	"Naked",
	"Dug",
	"Barren",
	"Naked",
	"No Honey",
	"Some Honey",
	"Full Of Honey",
	"Stage 1",
	"Stage 2",
	"Stage 3",
	"Ready, Held",
	"Ready",
	"Blooming",
	"Webbed",
	"Sand",
	#"",
	#"",
	#"",
	#"",
	#"",
	#"",

]
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
	"Mangrove Tree ": "Mangrove ",
	"Octopus Chest ": "Octo Chest ",
	"Cooked Wobster": "Delicious Wobster",
	"Watermelon (cooked)": "Grilled Watermelon",
	"Carrot (picked)": "Carrot",
	"Roasted Seeds ": "Toasted Seeds ",
	"(summer)": "(empty)",#walruscamp
	"(full with honey)": "(full of honey)",
	"Crock Pot ": "Crock Pot (empty) ",
	"Ash ": "Ashes ",
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
	"Bernie ": "Bernie (active) ",
	"Water Balloon": "Waterballoon",
	"Socket (empty)": "Socket (missing gem)",
	"Focus (incomplete)": "Focus (missing gem)",
	"Focus (charged)": "Focus (full)",
	#"*Animal Tracks":"*{{Pic32|Shown track}}Animal Track",
	"(depleted)": "(sand)",
	"Abigail's flower": "Abigail's Flower",
	"Elephant Cactus (active)": "Prickly Elephant Cactus",
	"Elephant Cactus (stump)": "Elephant Cactus Stump",
	"(chopped)": "(stump)",
	"(unpicked, sleeping)": "(sleeping)",#mushrooms
	"Cut Grass Tuft": "Cut Grass",
	" ": "",
	#"": "",
	#"": "",
	#"": "",
	#"": "",
}
SpecialNounChange = {
	"Grass": "Grass Tuft",
	"Improved Farm": "Basic and Improved Farm",
	"Basic Farm": "Basic and Improved Farm",
	"Net": "Bug Net",
	"Pig Man": "Pig",
	"Gem Stand": "Telelocator Socket",
	#"Prickly Elephant Cactus": "Elephant Cactus",
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
SpecialPrefixes = {
	"DISEASED": "Diseased ",
	"POISON": "Poison ",
	"DEAD": "Dead ",#idk if actually doing anything
	"LIMITED": "Sick ",#1  way worm hole
	"WINTER": "Winter ",
	#"": "",
	#"": "",
	#"": "",
	#"": "",
	#"": "",
	#"": "",
	#"": "",
}
PicRename = {

	"Lumpy Evergreen":"A Lumpy Evergreen",
	"The End is Nigh!":"The End is Nigh",
	"Sandbag":"Sand Bag Structure",
	"Sandbag Held":"Sand Bag",
	"Mangrove":"Mangrove Tree",
	"Mangrove Burnt":"Mangrove Tree Burnt",
	"Basalt":"Basalt1",
	"Walrus Camp":"Walrus Camp Winter",
	"Merm Hut":"Merm House Shipwrecked",
	"Slot Machine":"Slotmachine",
	"Octo Chest":"Octopus Chest Build",
	"Poisonous Hole":"Poison Hole",
	"X Marks the Spot":"X Marks The Spot",
	"Blue Mushtree":"Mushtree",
	"Red Mushtree":"MushtreeRed",
	"Green Mushtree":"MushtreeGreen",
	"Splumonkey Pod":"Monkey Totem",
	"Ancient Statue":"Ancient",
	"Relic":"Relic Chair",
	"Clockwork Rook":"Rook",
	"Damaged Bishop":"Damaged bishop",
	"Damaged Rook":"Damaged Clockwork",
	"Ghost":"Ghost Build",
	"Wee MacTusk":"WeeTusk",
	"Abigail":"Abigail build",
	"Delicious Wobster":"Cooked Wobster",
	"Roasted Coconut":"Cooked Coconut",
	"Roasted Coffee Beans":"Cooked Coffee Beans",
	"Webber's Skull":"Webberskull",
	"Maxwell's Phonograph":"Gramophone",
	"Maxwell's Mosquito Trap":"Minetranspattempt2",
	"Charcoal Boulder":"Rock charcoal",
	"Burnt Ash Tree":"Ash Tree",
	"Deadly Feast":"Meaty Stew",
	"Maxwell's Head":"Maxwell Head",
	"Basic and Improved Farm Growing":"Basic Farm}}{{Pic32|Turbo Farm Plot",#hax
	"Pick/Axe":"PickSlashAxe",
	"Juicy Berry Bush":"Berry bush Juicy",
	"Berry Bush Dug":"Berry Bush Item",
	"Crabbit Den":"Rabbit Hole",
	"Large Ornate Chest":"Ornate Chest",
	"Fishermerm's Hut":"Mermhouse Fisher",
	"Plugged Sinkhole":"Sinkhole",
	"Elephant Cactus":"Withered Elephant Cactus",
	"Prickly Elephant Cactus":"Elephant Cactus",
	"Elephant Cactus Stump":"Elephant Cactus Stump 2",
	"Eye Plant":"Eyeplant",
	"Meat Bulb":"Lureplant",
	"Star-sky":"Star-Sky",
	"Extra-Adorable Lavae":"Lavae",
	"Grass":"Grass Tuft",
	"Telelocator Socket":"Telelocator_Focus",
	"Sea Worther":"Sea worther",
	"Burnt":"",
	"Overheating":"",
	"Freezing":"",
	"Sandbag Held":"Sand Bag",
	"Crock Pot Empty": "Crock Pot",
	"Evergreen Burnt":       "Burnt Evergreen",
	"Lumpy Evergreen Burnt": "Burnt Evergreen",
	"Twiggy Tree": "Twiggy Tree Build",
	"Twiggy Tree Stump":     "Evergreen Stump",
	"Lumpy Evergreen Stump": "Evergreen Stump",
	"Wildbore Head Burnt": "Pig Head Burnt",
	"Merm Head Burnt":     "Pig Head Burnt",
	"Soaked Candle": "Wine Bottle Candle",
	"shadow body":"shadow body collection icon",
	"Juicy Berry Bush Dug": "Dug Juicy Berry Bush",
	"Red Mushroom Picked":   "Mushroom Picked",
	"Green Mushroom Picked": "Mushroom Picked",
	"Blue Mushroom Picked":  "Mushroom Picked",
	"Red Mushroom Sleeping":   "Mushroom Sleeping",
	"Green Mushroom Sleeping": "Mushroom Sleeping",
	"Blue Mushroom Sleeping":  "Mushroom Sleeping",
	"Bee Box No Honey": "Bee Box Level 0",
	"Bee Box Some Honey": "Bee Box Level 1",
	"Bee Box Full Of Honey": "Bee Box Level 3",
	"Piratihatitator Burnt": "Prestihatitator Burnt",
	"Abigail's Flower Stage 1": "Abigail Flower",
	"Abigail's Flower Stage 2": "Abigail Flower2",
	"Abigail's Flower Stage 3": "Abigail Flower2",
	"Abigail's Flower Ready, Held": "Abigail Flower Haunted",
	"Abigail's Flower Ready": "Abigail Flower Haunted",
	"Broken Clockworks": "Broken clockworks",
	"Bernie Broken": "DeadBernie",
	#"": "",
	#"": "",

}
def CreateSkinDict(Source, Character):
	Source = open(Source)
	Character = Character.lower()
	SkinDict = {}
	for line in Source.readlines():
		if line.startswith('msgctxt "STRINGS.SKIN_NAMES.body_' + Character + "_"):
			Entry = line[34+len(Character):-2]
			Name = Entry.replace("_"," ")
			Name = Name.title()+" Set"
			SkinDict[Entry] = Name

	return SkinDict
def CreateSkinQuoteDict(Source, Character):
	if Character == "WIGFRID":
		Character = "WATHGRITHR"
	SkinDict = CreateSkinDict(Source, Character)
	Character = Character.lower()
	Source = open(Source)
	SkinQuoteDict = {}
	Entry = None
	for line in Source.readlines():
		if Entry:
			PicName = Entry + " body"
			for Case in PicRename:
					if PicName == Case:
						PicName = PicRename[Case]
						if Debuging:
							print("Renamed =>", PicName)
						break
			PicName =  Character.title()+" "+PicName
			#if Debuging:
				#print("{}_{} PicName: {}".format(Character,Entry, PicName))
			try:
				SkinQuoteDict[SkinDict[Entry]] = [line[6:-1], PicName]
			except:
				pass
			Entry = None
		elif line.startswith('msgctxt "STRINGS.SKIN_QUOTES.{}'.format(Character)):
			Entry = line[30 + len(Character):-2]
	try:
		del SkinQuoteDict[""]
	except:
		pass
	return SkinQuoteDict

def CreateNameDict(Source):
	Source = open(Source)
	NameDict = {}
	Entry = None
	for line in Source.readlines():
		if Entry:
			Entry = Entry.replace("WORMHOLE_LIMITED_1","WORMHOLE_LIMITED")
			Entry = Entry.replace("SLOW_","")#farms have same quotes
			Entry = Entry.replace("FAST_","")
			NameDict[Entry] = line[7:-2]
			Entry = None

		elif line.startswith('msgctxt "STRINGS.NAMES.'):
			Entry = line[23:-2]
		elif line.startswith('msgctxt "STRINGS.DIRECTIONS.'):
			Entry = line[28:-2]
		elif line.startswith('msgctxt "STRINGS.SKIN_NAMES.body_'):
			Entry = line[28:-2]
	#print(NameDict)
	return NameDict

def CreateQuoteDict(Source, Character):
	if Character == "WILSON": #no Quotes are actually labelled for Wilson, he is the generic.
		Character = "GENERIC"
	elif Character == "WIGFRID":
		Character = "WATHGRITHR"
	NameDict = CreateNameDict(Source)
	#if Debuging:
		#print(NameDict)
	Character = Character.upper()
	Source = open(Source)
	QuoteDict = {}
	Entry = None
	for line in Source.readlines():
		if Entry:
			if Debuging: 
				print ("––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––"), print(), print("Entry:",Entry)
			Prefix = ""
			Affix = ""
			PBase = ""
			ABase = ""
			Dug = False
			PicName = ""

	#––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
			
			if Entry[len(Entry)-7:] == "GENERIC":
				Entry = Entry[:-8]
				if Debuging: 
					print("Entry =>", Entry)

			if Entry.startswith("DESCRIBE"):
				Entry = Entry[9:]
				if Debuging: 
					print("Entry =>", Entry)

			elif Entry.startswith("ANNOUNCE"):
				Entry = Entry[9:]
				if Debuging: 
					print("Entry =>", Entry)
			if Entry.startswith("DUG"):
				Entry = Entry[4:]
				Affix = "held"
				Dug = True#-----distinction from non-Dug verison
				if Debuging: 
					print("Entry =>", Entry)

	#––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
			
			for Case in SpecialAffixes:
				if Entry[len(Entry) - (len(Case) + 1):] == "." + Case or Entry[len(Entry) - (len(Case) + 1):] == "_" + Case: 
					Entry = Entry[:len(Entry) - len(Case)-1]
					Affix += SpecialAffixes[Case]
					ABase = Affix.title()
					if Debuging: 
						print("Affix: {} => {}".format(Case,SpecialAffixes[Case]))
						print("ABase:", ABase)
						print("Entry =>", Entry)
					break

			for Case in SpecialPrefixes:
				if (Entry[len(Entry) - (len(Case) + 1):] == "." + Case or Entry[len(Entry) - (len(Case) + 1):] == "_" + Case) and Entry[:len(Entry) - len(Case)-1] in NameDict:#----------if ends with preffix and without preffix has IGN
					Entry = Entry[:len(Entry) - (len(Case) + 1)]
					Prefix = Prefix + SpecialPrefixes[Case]
					PBase = Prefix.title()
					if Debuging: 
						print("Prefix: {} => {}".format(Case,SpecialPrefixes[Case]))
						print("PBase:", PBase)
						print("Entry =>", Entry)
					break

	#––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
			
			if Entry not in NameDict:
				if Entry.find(".") != -1:#-----NORMAL AFFIX GENERATOR
					i = Entry.find(".")
					Affix += Entry[i+1:]#-----also removes "."
					if Affix not in SpecialAffixes:
						try:
							Affix = NameDict[Affix]
						except KeyError:
							Affix = Affix.lower()
					Entry = Entry[:i]


			if Affix:
				if not ABase:
					ABase = Affix.title()
				Affix = " ({})".format(Affix)
				if Debuging:
					print("Affix:", Affix)
					print("ABase:", ABase)
					print("Entry =>", Entry)

	#––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
			

	#––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
			
			if Entry in NameDict:
				#print(" NameDict[Entry]:",  NameDict[Entry])
				if NameDict[Entry] in SpecialNounChange:
					if Debuging:
						print("SNC-Entry: {} => {}".format(NameDict[Entry], SpecialNounChange[NameDict[Entry]]))
					NameDict[Entry] = SpecialNounChange[NameDict[Entry]]


				if Debuging: 
						print("######In Dictionary######")
						print("IGN:", NameDict[Entry])
	#––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
				if Entry != "COMPASS":
					if ABase:
						if Dug:
							ABase = "Dug"
						elif ABase == "Barren":
							ABase = "Withered"
						PicName = NameDict[Entry] + " " + ABase
						if Debuging:
							print("PicName:", PicName)
						if PicName in PicRename:
							PicName = PicRename[PicName]
							if Debuging:
								print("PicName {} => {}".format(NameDict[Entry] + " " + ABase, PicName))
						elif ABase in PicAffixes:
							pass
						else:
							if NameDict[Entry] in PicRename:
								PicName = PicRename[NameDict[Entry]]
								if Debuging:
									print("PicName:", PicName)	
							else:
								PicName = NameDict[Entry]
							if Debuging:
								print("PicName:", PicName)	
					elif PBase:
						PicName = PBase + NameDict[Entry]
						if Debuging:
							print("PicName:", PicName)
						if PicName in PicRename:
							PicName = PicRename[PicName]
							if Debuging:
								print("PicName {} => {}".format(PBase + NameDict[Entry], PicName))
					else:
						PicName = NameDict[Entry]
						if Debuging:
							print("PicName:", PicName)
						if PicName in PicRename:
							PicName = PicRename[PicName]
							if Debuging:
								print("PicName {} => {}".format(NameDict[Entry], PicName))
	#––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
					QuoteDict[Prefix + NameDict[Entry]+ Affix] = [line[6:-1], PicName]
					if Debuging:
						print("'Pair': [{}|{}|{}]".format(Prefix + NameDict[Entry] + Affix, QuoteDict[Prefix + NameDict[Entry] + Affix][0], QuoteDict[Prefix + NameDict[Entry] + Affix][1]))
						print()
			else:
				if Debuging: 
					print("====Not in Dictionary====")
				Entry = Entry.replace("_"," ")
				Entry = Entry.replace("."," ")
				Entry = Entry.replace("\"","'")
				Entry = Entry.title()
				if Debuging: 
					print("Cleaned Action:", Prefix + Entry + Affix)
				QuoteDict[Prefix + Entry + Affix] = [line[6:-1], PicName]
				if Debuging: 
					print("Pair: [{}|{}]".format(Prefix + Entry + Affix, QuoteDict[Prefix + Entry + Affix][0]))
					print()
			Entry = None
	#––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
		elif line.startswith('msgctxt "STRINGS.CHARACTERS.{}'.format(Character)):#----------sets up for next cycle; quote is on next line not this one
			Entry = line[29 + len(Character):-2]
	#––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
	try:
		del QuoteDict[""]
	except:
		pass
	#print(QuoteDict)
	if Debuging:
		print("************************************************************"), print()
	return QuoteDict
def CreateIcon(PicName):
	return "{}{}{}".format("{{Pic32|", PicName, "}}")
def EnterQuotes(Source, Character, InputFile, OutputFile):

	print("============================================================")
	print("Using Source: {}".format(Source))
	Character = Character.upper()
	if Character == "MAXWELL":
		Character = "WAXWELL"
	QuoteDict = dict(list(CreateQuoteDict(Source, Character).items()) + list(CreateSkinQuoteDict(Source, Character).items()))
	Used = []
	Input = open(InputFile)
	Output = open(OutputFile, "w")
	lIndex = 0
	#––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––	
	if not Debuging:
		print("Creating file", end="",flush=True)
	for line in Input.readlines():
		lIndex += 1
		line = line.replace(" "," ")
		for Case in Cleaning:
			line = line.replace(Case+"-", Cleaning[Case]+"-")
		#print(">>>",line)
		for key in QuoteDict:
			if line.find("*"+key+"-") != -1 or line.find("}"+key+"-") != -1 or line.find("} "+key+"-") != -1 or line.find("]"+key+"-") != -1 or line.find("] "+key+"-") != -1:
				Icon = ""
				temp = QuoteDict[key][0]
				if Character == "WATHGRITHR" or Character == "WIGFRID":
					temp = temp.replace("o", "ö")
					temp = temp.replace("O", "Ö")
				Quote = temp

				PicName = QuoteDict[key][1]
				if PicName:
					Icon = CreateIcon(PicName)
						#print ("Name: {}|Quote: {}|PicName: {}".format(key, Quote, QuoteDict[key][1]))

		#––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
				line = line.replace("*{}-".format(key),"*{}{}-".format(Icon, key))
				if Overwrite:
					if line.find("*{}-".format(key)) != -1 or line.find("] {}-".format(key)) != -1 or line.find("]{}-".format(key)) != -1 or line.find("{} {}-".format("}", key)) != -1 or line.find("{}{}-".format("}", key)) != -1:

						line = "*{}{}- {}\n".format(Icon, key, Quote)
						if Debuging:
								print("––––––––––")
								print()
								print("{}:".format(key))
								print(line)
						break

				elif line.find("] {}-\n".format(key)) != -1 or line.find("]{}-\n".format(key)) != -1 or line.find("] {}- \n".format(key)) != -1 or line.find("]{}- \n".format(key)) != -1 or \
				line.find("{} {}-\n".format("}", key)) != -1 or line.find("{}{}-\n".format("}", key)) != -1 or line.find("{} {}- \n".format("}", key)) != -1 or line.find("{}{}- \n".format("}", key)) != -1 or \
				line.find("*{}-\n".format(key)) != -1 or line.find("*{}- \n".format(key)) != -1:#cant use line.find("{}- \n".format(key)) b/c 'Endothermic Fire' would also trigger 'Fire' etc.

					line = "*{}{}- {}\n".format(Icon, key, Quote)
					if Debuging:
								print("––––––––––")
								print()
								print("{}:".format(key))
								print(line)
					break
				
				elif PicOverwrite:
					if PicName and Icon and line.find("*{}{}-".format(Icon, key)) == -1:
						IconStart = line.find("{{Pic32|")
						IconEnd = line[IconStart:].find("}}")
						if IconStart != -1 and IconEnd != -1:
							CurrentIcon = line[IconStart:IconEnd+IconStart+2]
							CurrentPic = line[IconStart+8:IconEnd+IconStart]
							if Debuging:
								print("––––––––––")
								print()
								print("{}:".format(key))
								print(line)
								print("Icon:", Icon)
								print("CurrentIcon:", line[IconStart:IconEnd+IconStart+2])
							if CurrentPic in QuoteDict or CurrentPic in PicRename.values():
									line = line.replace(CurrentIcon, Icon)
									if Debuging:
										print("Replaced '{}' pic with '{}'".format(CurrentPic, PicName)),print()
										print(line)
									break
							else:
								if Debuging:
									print("{} not found".format(CurrentPic))
									print("Keeping CurrentIcon"),print()

		#––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
		
		Output.write(line)

		if not Debuging and lIndex%100 == 0:#----------the progress "bar"
			print('.', end="",flush=True)
	else:
		if Debuging:
			Unused = open("unused_" + Character.lower() + ".txt", "a")
			Unused.write("––––––––––––––––––––––––––––––––––––––––\n")
			UnusedR = open("unused_" + Character.lower() + ".txt", "r")
									
			for key in QuoteDict:
				if Input.read().find("*{}- {}".format(key, QuoteDict[key])) == -1:
					if UnusedR.read().find("*{}- {}\n".format(key, QuoteDict[key])) == -1:
						Unused.write("*{}- {}\n".format(key, QuoteDict[key]))
		if not Debuging:
			print("Complete")
		print('Exported to "{}"'.format(OutputFile))
		








Character = input("Character (file should also be named Character.txt):")
Start = floor(time())
#EnterQuotes("strings.pot",input("Character DebugSpawn: "), input("Import file (e.x. file.txt) :"), input("Export file (e.x. file.txt) :"))
EnterQuotes("stringsDST.pot",Character, Character + ".txt", Character + "temp.txt")
EnterQuotes("strings.pot",Character, Character + "temp.txt", Character + "_Export.txt")
print("============================================================")
Elapsed = [floor((floor(time())-Start)/60), (floor(time())-Start)%60]
if Debuging:
	print("Completed in {} seconds".format(Elapsed[1]))
print("Done!")

