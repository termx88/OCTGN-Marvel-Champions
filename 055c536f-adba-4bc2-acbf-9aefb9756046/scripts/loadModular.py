#------------------------------------------------------------
# 'Load Encounter' event
#------------------------------------------------------------

def loadEncounter(group, x = 0, y = 0, nbEncounter = 1):
    mute()
    vName = getGlobalVariable("villainSetup")
    if nbEncounter > 0:
        setupChoice = askChoice("Would you like to take on recommended modular encounter set(s) ?", ["Yes", "Let me choose which one(s)", "Oops! Let's start over from the beginning!"]) 
        if setupChoice == 0 or setupChoice == 3:
            deleteAllSharedCards()
            return
        if setupChoice == 1: return recommendedEncounter(group, villainName=vName)
        if setupChoice == 2: return specificEncounter(group, nbModular = nbEncounter)
    elif nbEncounter == 0: return True


def specificEncounter(group, x = 0, y = 0, nbModular = 1):
    mute()
    vName = getGlobalVariable("villainSetup")

    cardsSelected = dialogBox_Setup(setupPile(), "encounter_setup", "Modular encounter selection", "Select at least {} modular(s) encounter(s):".format(nbModular), min = nbModular, max = 50)
    if cardsSelected is None:
        deleteAllSharedCards()
        return
    for card in cardsSelected:
        if vName != 'The Hood':
            createCards(group,sorted(eval(card.Owner).keys()), eval(card.Owner))
        else:
            createCards(specialDeck(),sorted(eval(card.Owner).keys()), eval(card.Owner))
    deleteCards(setupPile())
    return True


def recommendedEncounter(group, x = 0, y = 0, villainName=''):
    if villainName == 'Rhino':
        createCards(group,sorted(bomb_scare.keys()),bomb_scare)
    if villainName == 'Klaw':
        createCards(group,sorted(masters_of_evil.keys()),masters_of_evil)
    if villainName == 'Ultron':
        createCards(group,sorted(under_attack.keys()),under_attack)
    if villainName == 'Green Goblin: Mutagen Formula':
        createCards(group,sorted(goblin_gimmicks.keys()),goblin_gimmicks)
    if villainName == 'Green Goblin: Risky Business':
        createCards(group,sorted(goblin_gimmicks.keys()),goblin_gimmicks)
    if villainName == 'Crossbones':
        createCards(group,sorted(hydra_assault.keys()),hydra_assault)
        createCards(group,sorted(weap_master.keys()),weap_master)
        createCards(group,sorted(legions_of_hydra.keys()),legions_of_hydra)
    if villainName == 'Absorbing Man':
        createCards(group,sorted(hydra_patrol.keys()),hydra_patrol)
    if villainName == 'Taskmaster':
        createCards(group,sorted(weap_master.keys()),weap_master)
    if villainName == 'Zola':
        createCards(group,sorted(under_attack.keys()),under_attack)
    if villainName == 'Red Skull':
        createCards(group,sorted(hydra_assault.keys()),hydra_assault)
        createCards(group,sorted(hydra_patrol.keys()),hydra_patrol)
    if villainName == 'Kang':
        createCards(group,sorted(temporal.keys()),temporal)
    if villainName == 'Drang':
        createCards(group,sorted(band_of_badoon.keys()),band_of_badoon)
    if villainName == 'Collector 1':
        createCards(group,sorted(menagerie_medley.keys()),menagerie_medley)
    if villainName == 'Collector 2':
        createCards(group,sorted(menagerie_medley.keys()),menagerie_medley)
    if villainName == 'Nebula':
        createCards(group,sorted(space_pirates.keys()),space_pirates)
    if villainName == 'Ronan':
        createCards(group,sorted(kree_militant.keys()),kree_militant)
    if villainName == 'Ebony Maw':
        createCards(group,sorted(armies_of_titan.keys()),armies_of_titan)
        createCards(group,sorted(black_order.keys()),black_order)
    if villainName == 'Tower Defense':
        createCards(group,sorted(armies_of_titan.keys()),armies_of_titan)
    if villainName == 'Thanos':
        createCards(group,sorted(black_order.keys()),black_order)
        createCards(group,sorted(children_of_thanos.keys()),children_of_thanos)
    if villainName == 'Hela':
        createCards(group,sorted(legions_of_hel.keys()),legions_of_hel)
        createCards(group,sorted(frost_giants.keys()),frost_giants)
    if villainName == 'Loki':
        createCards(group,sorted(enchantress.keys()),enchantress)
        createCards(group,sorted(frost_giants.keys()),frost_giants)
    if villainName == 'The Hood':
        setupChoice = askChoice("Each encounter sets from The Hood Scenario Pack has been ranked from least to most difficult.", ["Lower difficulty (modular encounter sets ranked 1 to 7)", "Moderate difficulty (modular encounter sets ranked 2 to 8)", "Higher difficulty (modular encounter sets ranked 3 to 9)"]) 
        lower_difficulty = [streets_of_mayhem, brothers_grimm, ransacked_armory, state_of_emergency, beasty_boys, mister_hyde, sinister_syndicate]
        moderate_difficulty = [brothers_grimm, ransacked_armory, state_of_emergency, beasty_boys, mister_hyde, sinister_syndicate, crossfire_crew]
        higher_difficulty = [ransacked_armory, state_of_emergency, beasty_boys, mister_hyde, sinister_syndicate, crossfire_crew, wrecking_crew]
        if setupChoice == 0:
            deleteAllSharedCards()
            return
        if setupChoice == 1:
            for modular in lower_difficulty:
                createCards(specialDeck(), sorted(modular.keys()), modular)
        if setupChoice == 2:
            for modular in moderate_difficulty:
                createCards(specialDeck(), sorted(modular.keys()), modular)
        if setupChoice == 3:
            for modular in higher_difficulty:
                createCards(specialDeck(), sorted(modular.keys()), modular)
    if villainName == 'Sandman':
        createCards(group,sorted(down_to_earth.keys()),down_to_earth)
    if villainName == 'Venom':
        createCards(group,sorted(down_to_earth.keys()),down_to_earth)
    if villainName == 'Mysterio':
        createCards(group,sorted(whispers_of_paranoia.keys()),whispers_of_paranoia)
    if villainName == 'Sinister Six':
        return True
    if villainName == 'Venom Goblin':
        createCards(group,sorted(goblin_gear.keys()),goblin_gear)
    if villainName == 'Sabretooth':
        createCards(group,sorted(brotherhood.keys()),brotherhood)
        createCards(group,sorted(mystique.keys()),mystique)
    if villainName == 'Project Wideawake':
        createCards(group,sorted(sentinels.keys()),sentinels)
    if villainName == 'Master Mold':
        createCards(group,sorted(zero_tolerance.keys()),zero_tolerance)
    if villainName == 'Mansion Attack':
        createCards(group,sorted(mystique.keys()),mystique)
    if villainName == 'Magneto':
        createCards(group,sorted(acolytes.keys()),acolytes)
    return True