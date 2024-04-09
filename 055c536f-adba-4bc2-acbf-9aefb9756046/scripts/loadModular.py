#------------------------------------------------------------
# 'Load Encounter' event
#------------------------------------------------------------

def loadFanmadeEncounter(group, x = 0, y = 0):
    mute()
    specificEncounter(group, nbModular = 1, setupType = "fm_encounter_setup")

def loadEncounter(group, nbModular = 1):
    mute()
    villainName = getGlobalVariable("villainSetup")
    if nbModular > 0:
        setupChoice = askChoice("Would you like to take on recommended modular encounter set(s) ?", ["Yes", "Let me choose which one(s)", "Oops! Let's start over from the beginning!"])
        if setupChoice == 0 or setupChoice == 3:
            deleteAllSharedCards()
            return
        if setupChoice == 1: return recommendedEncounter(group, villainName)
        if setupChoice == 2: return specificEncounter(group, nbModular, "encounter_setup")
    elif nbModular == 0: return True


def recommendedEncounter(group, villainName = ''):
    recommendedModular = getGlobalVariable("recommendedModular")
    if villainName == 'Rhino':
        createCardsFromSet(group, "bomb_scare", "Bomb Scare", True)
    if villainName == 'Klaw':
        createCardsFromSet(group, "masters_of_evil", "Masters of Evil", True)
    if villainName == 'Ultron':
        createCardsFromSet(group, "under_attack", "Under Attack", True)
    if villainName == 'Green Goblin: Mutagen Formula':
        createCardsFromSet(group, "goblin_gimmicks", "Goblin Gimmicks", True)
    if villainName == 'Green Goblin: Risky Business':
        createCardsFromSet(group, "goblin_gimmicks", "Goblin Gimmicks", True)
    if villainName == 'Crossbones':
        createCardsFromSet(group, "hydra_assault", "Hydra Assault", True)
        createCardsFromSet(group, "weap_master", "Weapons Master", True)
        createCardsFromSet(group, "legions_of_hydra", "Legions of Hydra", True)
    if villainName == 'Absorbing Man':
        createCardsFromSet(group, "hydra_patrol", "Hydra Patrol", True)
    if villainName == 'Taskmaster':
        createCardsFromSet(group, "weap_master", "Weapons Master", True)
    if villainName == 'Zola':
        createCardsFromSet(group, "under_attack", "Under Attack", True)
    if villainName == 'Red Skull':
        createCardsFromSet(group, "hydra_assault", "Hydra Assault", True)
        createCardsFromSet(group, "hydra_patrol", "Hydra Patrol", True)
    if villainName == 'Kang':
        createCardsFromSet(group, "temporal", "Temporal", True)
    if villainName == 'Drang':
        createCardsFromSet(group, "band_of_badoon", "Band of Badoon", True)
    if villainName == 'Collector 1':
        createCardsFromSet(group, "menagerie_medley", "Menagerie Medley", True)
    if villainName == 'Collector 2':
        createCardsFromSet(group, "menagerie_medley", "Menagerie Medley", True)
    if villainName == 'Nebula':
        createCardsFromSet(group, "space_pirates", "Space Pirates", True)
    if villainName == 'Ronan':
        createCardsFromSet(group, "kree_militant", "Kree Militant", True)
    if villainName == 'Ebony Maw':
        createCardsFromSet(group, "armies_of_titan", "Armies of Titan", True)
        createCardsFromSet(group, "black_order", "black_order", True)
    if villainName == 'Tower Defense':
        createCardsFromSet(group, "armies_of_titan", "Armies of Titan", True)
    if villainName == 'Thanos':
        createCardsFromSet(group, "black_order", "black_order", True)
        createCardsFromSet(group, "children_of_thanos", "Children of Thanos", True)
    if villainName == 'Hela':
        createCardsFromSet(group, "legions_of_hel", "Legions of Hel", True)
        createCardsFromSet(group, "frost_giants", "Frost Giants", True)
    if villainName == 'Loki':
        createCardsFromSet(group, "enchantress", "Enchantress", True)
        createCardsFromSet(group, "frost_giants", "Frost Giants", True)
    if villainName == 'The Hood':
        setupChoice = askChoice("Each encounter sets from The Hood Scenario Pack has been ranked from least to most difficult.", ["Lower difficulty (modular encounter sets ranked 1 to 7)", "Moderate difficulty (modular encounter sets ranked 2 to 8)", "Higher difficulty (modular encounter sets ranked 3 to 9)"])
        lower_difficulty = ["streets_of_mayhem", "brothers_grimm", "ransacked_armory", "state_of_emergency", "beasty_boys", "mister_hyde", "sinister_syndicate"]
        moderate_difficulty = ["brothers_grimm", "ransacked_armory", "state_of_emergency", "beasty_boys", "mister_hyde", "sinister_syndicate", "crossfire_crew"]
        higher_difficulty = ["ransacked_armory", "state_of_emergency", "beasty_boys", "mister_hyde", "sinister_syndicate", "crossfire_crew", "wrecking_crew_modular"]
        if setupChoice == 0:
            deleteAllSharedCards()
            return
        if setupChoice == 1:
            for modular in lower_difficulty:
                createCardsFromSet(specialDeck(), modular, modular, True)
        if setupChoice == 2:
            for modular in moderate_difficulty:
                createCardsFromSet(specialDeck(), modular, modular, True)
        if setupChoice == 3:
            for modular in higher_difficulty:
                createCardsFromSet(specialDeck(), modular, modular, True)
    if villainName == 'Sandman':
        createCardsFromSet(group, "down_to_earth", "Down to Earth", True)
    if villainName == 'Venom':
        createCardsFromSet(group, "down_to_earth", "Down to Earth", True)
    if villainName == 'Mysterio':
        createCardsFromSet(group, "whispers_of_paranoia", "Whispers of Paranoia", True)
    if villainName == 'Venom Goblin':
        createCardsFromSet(group, "goblin_gear", "Goblin Gear", True)
    if villainName == 'Sabretooth':
        createCardsFromSet(group, "brotherhood", "Brotherhood", True)
        createCardsFromSet(group, "mystique", "Mystique", True)
    if villainName == 'Project Wideawake':
        createCardsFromSet(group, "sentinels", "Sentinels", True)
    if villainName == 'Master Mold':
        createCardsFromSet(group, "zero_tolerance", "Zero Tolerance", True)
    if villainName == 'Mansion Attack':
        createCardsFromSet(group, "mystique", "Mystique", True)
    if villainName == 'Magneto':
        createCardsFromSet(group, "acolytes", "Acolytes", True)
    if villainName == 'MaGog':
        mojoSelectedModular = dialogBox_Setup(specialDeck(), "encounter_setup", ["Crime", "Fantasy", "Horror", "Sci-Fi", "Sitcom", "Western"], "Modular encounter selection", "Select 1 modular encounter:", min = 1, max = 1, isFanmade = False)
        if mojoSelectedModular is None:
            deleteAllSharedCards()
            return
        for card in mojoSelectedModular:
            createCardsFromSet(group, card.Owner, card.name, True)
        deleteCards(specialDeck())
    if villainName == 'Spiral':
        mojoSelectedModular = dialogBox_Setup(specialDeck(), "encounter_setup", ["Crime", "Fantasy", "Horror", "Sci-Fi", "Sitcom", "Western"], "Modular encounter selection", "Select 3 modulars encounters:", min = 3, max = 3, isFanmade = False)
        if mojoSelectedModular is None:
            deleteAllSharedCards()
            return
        for card in mojoSelectedModular:
            createCardsFromSet(group, card.Owner, card.name, True)
        deleteCards(specialDeck())
        for c in sideDeck():
            if c.Type != "environment":
                c.moveTo(encounterDeck())
    if villainName == 'Mojo':
        nbModular = 1 + len(getPlayers())
        mojoSelectedModular = dialogBox_Setup(specialDeck(), "encounter_setup", ["Crime", "Fantasy", "Horror", "Sci-Fi", "Sitcom", "Western"], "Modular encounter selection", "Select {} modulars encounters:".format(nbModular), min = nbModular, max = nbModular, isFanmade = False)
        if mojoSelectedModular is None:
            deleteAllSharedCards()
            return
        for card in mojoSelectedModular:
            createCardsFromSet(group, card.Owner, card.name, True)
        deleteCards(specialDeck())
    if villainName == 'Morlock Siege':
        createCardsFromSet(group, "military_grade", "Military Grade", True)
        createCardsFromSet(group, "mutant_slayers", "Mutant Slayers", True)
    if villainName == 'On the Run':
        createCardsFromSet(group, "military_grade", "Military Grade", True)
        createCardsFromSet(group, "nasty_boys", "Nasty Boys", True)
    if villainName == 'Juggernaut':
        createCardsFromSet(group, "black_tom_cassidy", "Black Tom Cassidy", True)
    if villainName == 'Mister Sinister':
        createCardsFromSet(group, "nasty_boys", "Nasty Boys", True)
    if villainName == 'Stryfe':
        createCardsFromSet(group, "extreme_measures", "Extreme Measures", True)
        createCardsFromSet(group, "mutant_insurrection", "Mutant Insurrection", True)
    elif len(recommendedModular) > 0:
        recommendedModular = eval(recommendedModular)
        for k, i in recommendedModular.items():
            setName = i[0]
            pile = shared.piles[i[1]]
            toShuffle = i[2]
            createCardsFromSet(pile, k, setName, True)
            showGroup(pile, toShuffle)
    return True


def specificEncounter(group, nbModular = 1, setupType = "encounter_setup"):
    mute()
    vName = getGlobalVariable("villainSetup")

    if setupType == "fm_encounter_setup":
        fanmade = True
    else:
        fanmade = False
    update()
    cardsSelected = dialogBox_Setup(setupPile(), setupType, None, "Modular encounter selection", "Select at least {} modular(s) encounter(s):".format(nbModular), min = nbModular, max = 50, isFanmade = fanmade)
    if cardsSelected is None:
        deleteAllSharedCards()
        return
    for card in cardsSelected:
        if vName == 'The Hood':
            createCardsFromSet(specialDeck(), card.Owner, card.Name, True)
        else:
            createCardsFromSet(group, card.Owner, card.Name, True)
    deleteCards(setupPile())
    return True


def campaignEncounter(villainSet = '', x = 0, y = 0):
    if villainSet == "crossbones" or villainSet == "absorbing_man" or villainSet == "taskmaster" or villainSet == "zola" or villainSet == "red_skull":
        createCardsFromSet(campaignDeck(), "hydra_camp", "Hydra Campaign", True)
        createCardsFromSet(campaignDeck(), "expcamp", "Expert Campaign", True)

    if villainSet == "brotherhood_of_badoon" or villainSet == "collector1" or villainSet == "collector2" or villainSet == "nebula" or villainSet == "ronan":
        createCardsFromSet(campaignDeck(), "the_market", "The Market", True)
        createCardsFromSet(campaignDeck(), "gmw_campaign_challenge", "Challenge", True)
        createCardsFromSet(campaignDeck(), "badoon_headhunter", "Badoon Headhunter", True)

    if villainSet == "ebony_maw" or villainSet == "tower_defense" or villainSet == "thanos" or villainSet == "hela" or villainSet == "loki":
        createCardsFromSet(campaignDeck(), "mts_campaign", "Mad Titan's Shadow Campaign", True)

    if villainSet == "sandman" or villainSet == "venom" or villainSet == "mysterio" or villainSet == "sinister_six" or villainSet == "venom_goblin":
        createCardsFromSet(campaignDeck(), "bad_publicity", "Bad Publicity", True)
        createCardsFromSet(campaignDeck(), "community_service", "Community Service", True)
        createCardsFromSet(campaignDeck(), "snitches_get_stitches", "Snitches Get Stitches", True)
        createCardsFromSet(campaignDeck(), "shield_tech", "Shield Tech", True)
        campaignDeck().create("f8a7865d-a43d-4b6f-bf29-5c9039b973cc", 1)
        campaignDeck().create("dc32c7e5-bed3-4bc3-a76b-eddd0d7d844a", 4)
        createCardsFromSet(campaignDeck(), "osborn_tech", "Osborn Tech", True)

    if villainSet == "sabretooth" or villainSet == "project_wideawake" or villainSet == "master_mold" or villainSet == "mansion_attack" or villainSet == "magneto":
        createCardsFromSet(campaignDeck(), "future_past", "Future Past", True)
        createCardsFromSet(campaignDeck(), "mut_gen_campaign", "Mutant Genesis Campaign", True)
        createCardsFromSet(campaignDeck(), "brawler", "Brawler", True)
        createCardsFromSet(campaignDeck(), "commander", "Commander", True)
        createCardsFromSet(campaignDeck(), "defender", "Defender", True)
        createCardsFromSet(campaignDeck(), "peacekeeper", "Peacekeeper", True)
        campaignDeck().create("47d34c5d-5319-45a9-a2d6-1fb975032088", 1)
        campaignDeck().create("47d34c5d-5319-45a9-a2d6-1fb975032089", 1)
        campaignDeck().create("47d34c5d-5319-45a9-a2d6-1fb975032090", 1)
        campaignDeck().create("47d34c5d-5319-45a9-a2d6-1fb975032091", 1)
        campaignDeck().create("47d34c5d-5319-45a9-a2d6-1fb975032092", 1)

    if villainSet == "magog" or villainSet == "spiral" or villainSet == "mojo":
        createCardsFromSet(campaignDeck(), "longshot", "Longshot", True)

    if villainSet == "morlock_siege" or villainSet == "on_the_run" or villainSet == "juggernaut" or villainSet == "mister_sinister" or villainSet == "stryfe":
        createCardsFromSet(campaignDeck(), "next_evol_campaign", "NeXt Evolution Campaign", True)