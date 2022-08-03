#------------------------------------------------------------
# 'Load FanMade' events
#------------------------------------------------------------

def loadFanMade_Hero(group, x = 0, y = 0):
    mute()
    if not deckNotLoaded(group, checkGroup = [c for c in me.Deck if not isEncounter([c])]):
        msg = """Cannot generate a deck: You already have cards loaded.\n
Reset the game in order to generate a new deck."""
        askChoice(msg, [], [], ["Close"])
        return

    o8dList = []
    o8dDir = open("data.path", 'r').readline() + "\\GameDatabase\\055c536f-adba-4bc2-acbf-9aefb9756046\\FanMade\\Heroes\\"
    for deck in Directory.GetFiles(o8dDir, "*.o8d"):
         item = Path.GetFileNameWithoutExtension(deck)
         o8dList.append(item)
    if len(o8dList) == 0:
         return

    colorsList = ["#004d99"] * len(o8dList)
    buttons = ["Close"]
    msg = """Choose a deck from the list below !"""
    
    choice = askChoice(msg, o8dList, colorsList, buttons)
    if choice == 0:
         return  
    o8d = o8dDir + o8dList[choice-1] + ".o8d"
    full_dict = o8dLoadAsDict(o8d)

    hero_id = ""
    all_cards = []
    aspect_cards = []

    # 1- Load Hero cards + Nemesis + Special Deck cards
    # Cards without Owner are considered to be Aspect ones
    for section_id, section_elements in full_dict.items():
        if not section_elements["shared"]:
            # Manage in which pile cards will be created: Deck, Special Deck or Nemesis
            destination_pile = me.Deck
            if section_elements["section"] == "Nemesis":
                destination_pile = me.piles["Nemesis"]
            if section_elements["section"] == "Special":
                destination_pile = me.piles["Special Deck"]
            if section_elements["section"] == "Setup":
                destination_pile = me.piles["Setup"]
            
            # Create cards
            for card_id,qty in section_elements["cards"].items():
                cards = destination_pile.create(card_id, qty)
                if qty == 1:
                    all_cards.append(cards)
                    if cards.Type == "hero":
                        hero_id = cards.Owner
                    if cards.Owner == "":
                        aspect_cards.append(cards)
                else:
                    all_cards.extend(cards)
                    if cards[0].Owner == "":
                        aspect_cards.extend(cards)
    changeOwner(all_cards, hero_id)

    # 2- If some aspect cards have been found, let player choose to load them or not
    do_step3 = True
    if len(aspect_cards) > 0:
        choice = askChoice("Do you want to also load the prebuilt hero cards from this .o8d file?", ["Yes", "No"])
        # No answer or 'Yes' have the same effect: we load those cards
        if choice != 2:
            do_step3 = False
        if choice == 2:
            # Remove them from deck as they have already been created
            [c.delete() for c in me.Deck if c in aspect_cards]

    # 3- Load aspect cards from somewhere else if player has chosen to do so or if there were no such cards in the loaded o8d file
    if do_step3:
        choice_step3 = askChoice("Select where to load other aspect cards from:", ["Another .o8d file", "Another marvelcdb deck (URL)", "A Universal Pre-Built deck"])
        if choice_step3 == 0: return
        if choice_step3 == 1:
            other_o8d = openFileDlg('', '', 'o8d Files|*.o8d')
            if other_o8d is None:
                return        
            other_deck = o8dLoadAsDict(other_o8d)

            other_cards = []
            for card_id,qty in other_deck["Cards_False"]["cards"].items():
                cards = me.piles["Setup"].create(card_id, qty)
                if qty == 1 and cards.Owner == "":
                    other_cards.append(cards)
                elif qty > 1 and cards[0].Owner == "":
                    other_cards.extend(cards)
            changeOwner(other_cards, hero_id)
            [c.moveTo(me.Deck) for c in other_cards]
            deleteCards(me.piles["Setup"]) 
        
        if choice_step3 == 2:
            url = askString("Please enter the URL of the deck you wish to load.", "")
            if url == None: return
            if not "view/" in url:
                whisper("Error: Invalid URL.")
                return
            createAPICards(url, True, new_owner=hero_id)
        
        if choice_step3 == 3:
            upb = sorted(universal_prebuilt.keys())
            upb_aggr = [d for d in upb if 'Aggression' in d]
            upb_just = [d for d in upb if 'Justice' in d]
            upb_prot = [d for d in upb if 'Protection' in d]
            upb_lead = [d for d in upb if 'Leadership' in d]
            upb_basic = [d for d in upb if 'Basic' in d]
            colorsList = ["#990000"] * len(upb_aggr) + ["#999400"] * len(upb_just) + ["#059900"] * len(upb_prot) + ["#004d99"] * len(upb_lead) + ["#bbbbbb"] * len(upb_basic)
            buttons = ["Close"]
            msg = """Choose a Universal Pre-built deck from the list below !"""
            pb_choice = askChoice(msg, upb, colorsList, buttons)
            createAPICards("https://marvelcdb.com/deck/view/{}".format(universal_prebuilt[upb[pb_choice-1]]), True, new_owner=hero_id)

    tableSetup()


def loadFanMade_Villain(group, x = 0, y = 0):
    mute()
    villainName = ''
    nbModular = 0

    if me._id != 1:
        msg = """You're not the game host\n
Only the host is allowed to load a scenario."""
        askChoice(msg, [], [], ["Close"])
        return

    if not deckNotLoaded(group,0,0,shared.villain):
        msg = """Cannot generate a deck: You already have cards loaded.\n
Reset the game in order to generate a new deck."""
        askChoice(msg, [], [], ["Close"])
        return

    loadDifficulty()
    gameDifficulty = getGlobalVariable("difficulty")
    if gameDifficulty == "1":
        difDir = "Expert\\"
    else:
        difDir = "Standard\\"

    o8dList = []
    o8dDir = open("data.path", 'r').readline() + "\\GameDatabase\\055c536f-adba-4bc2-acbf-9aefb9756046\\FanMade\\Villains\\" + difDir
    for deck in Directory.GetFiles(o8dDir, "*.o8d"):
         item = Path.GetFileNameWithoutExtension(deck)
         o8dList.append(item)
    if len(o8dList) == 0:
         return

    colorsList = ["#6300a8"] * len(o8dList)
    buttons = ["Close"]
    msg = """Choose a scenario from the list below !"""
    
    choice = askChoice(msg, o8dList, colorsList, buttons)
    if choice == 0:
         return  
    o8d = o8dDir + o8dList[choice-1] + ".o8d"
    full_dict = o8dLoadAsDict(o8d)

    all_cards = []
    recommendedChoice = 1
    
    # 1- Load Villain cards + Scheme + Encounter + Side + Special + Campaign + Setup Deck cards
    for section_id, section_elements in full_dict.items():
        if section_elements["shared"]:
            # Manage in which pile cards will be created: Deck, Special Deck or Nemesis
            destination_pile = encounterDeck()
            if section_elements["section"] == "Villain":
                destination_pile = villainDeck()
            if section_elements["section"] == "Scheme":
                destination_pile = mainSchemeDeck()
            if section_elements["section"] == "Side":
                destination_pile = sideDeck()
            if section_elements["section"] == "Special":
                destination_pile = specialDeck()
            if section_elements["section"] == "Campaign":
                destination_pile = campaignDeck()
            if section_elements["section"] == "Setup":
                destination_pile = setupPile()
            if section_elements["section"] == "Recommended":
                destination_pile = setupPile()
                recommendedChoice = askChoice("Do you want to also load the Recommended Modular ?", ["Yes", "No, I want to load another modular encounter"])
              
            # Create cards
            for card_id,qty in sorted(section_elements["cards"].items()):
                if section_elements["section"] != "Recommended" or (section_elements["section"] == "Recommended" and recommendedChoice != 2):
                    destination_pile.create(card_id, qty)

    # 2- Create modular cards from Setup Pile to Encounter Deck.
    for card in setupPile():
        if card.Type == "encounter_setup":
            createCards(encounterDeck(),sorted(eval(card.Owner).keys()), eval(card.Owner))
        else:
            card.moveTo(encounterDeck())

    # 3- If cards found in Recommended_Modular 
    if recommendedChoice == 2:
        cardsSelected = dialogBox_Setup(setupPile(), "encounter_setup", "Modular encounter selection", "Select at least {} modular(s) encounter(s):".format(nbModular), min = 1, max = 50)
        for card in cardsSelected:
            createCards(encounterDeck(),sorted(eval(card.Owner).keys()), eval(card.Owner))       


    deleteCards(setupPile())

    update()

    # Move cards from Villain Deck to Encounter and Scheme Decks
    mainSchemeCards = [c for c in mainSchemeDeck()]
    villainCards = [c for c in villainDeck()]

    mainSchemeCards[0].moveToTable(tableLocations['mainScheme'][0],tableLocations['mainScheme'][1])
    villainCards[0].moveToTable(villainX(1,0),tableLocations['villain'][1])

    villainName = villainCards[0].Name
    setGlobalVariable("villainSetup",str(villainName))
    vName = getGlobalVariable("villainSetup")   
    shared.encounter.shuffle()
    notify('{} loaded {}, Good Luck!'.format(me, villainName))


def loadFanMade_Modular(group, x = 0, y = 0):
    mute()

    o8dList = []
    o8dDir = open("data.path", 'r').readline() + "\\GameDatabase\\055c536f-adba-4bc2-acbf-9aefb9756046\\FanMade\\Modulars\\"
    for deck in Directory.GetFiles(o8dDir, "*.o8d"):
         item = Path.GetFileNameWithoutExtension(deck)
         o8dList.append(item)
    if len(o8dList) == 0:
         return

    colorsList = ["#004d99"] * len(o8dList)
    buttons = ["Close"]
    msg = """Choose a scenario from the list below !"""
    
    choice = askChoice(msg, o8dList, colorsList, buttons)
    if choice == 0:
         return  
    o8d = o8dDir + o8dList[choice-1] + ".o8d"    
    full_dict = o8dLoadAsDict(o8d)
    playerPilesList = [p for p in me.piles]
    sharedPilesList = [p for p in shared.piles]

    # 1- Load cards in sections where shared = False
    for section_id, section_elements in full_dict.items():
        if not section_elements["shared"] and len(section_elements["cards"].items()) > 0:
            # Manage in which pile cards will be created: Deck, Special Deck or Nemesis
            destination_pile_choice = askChoice("In which pile do you want to load cards from {} section ?".format(section_id), playerPilesList)
            destination_pile = me.piles[playerPilesList[destination_pile_choice-1]]
            
            # Create cards
            for card_id,qty in section_elements["cards"].items():
                cards = destination_pile.create(card_id, qty)

    # 2- Load cards in sections where shared = True
    for section_id, section_elements in full_dict.items():
        if section_elements["shared"] and len(section_elements["cards"].items()) > 0:
            # Manage in which pile cards will be created: Deck, Special Deck or Nemesis
            destination_pile_choice = askChoice("In which pile do you want to load cards from {} section ?".format(section_id), sharedPilesList)
            destination_pile = shared.piles[sharedPilesList[destination_pile_choice-1]]
            
            # Create cards
            for card_id,qty in section_elements["cards"].items():
                cards = destination_pile.create(card_id, qty)