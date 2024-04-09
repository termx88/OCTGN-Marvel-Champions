orientation = {
        0: Rot0,
        1: Rot90,
        2: Rot180,
        3: Rot270
    }


def deserializeTable(tbl):
    if len(tbl) == 0:
        return
    for cardData in tbl:
        deserializeCard(cardData)


def serializePlayer(player):
    plData = {'_id':None, 'name': None, 'counters':None, 'piles': {}}
    plData['_id'] = player._id
    plData['name'] = player.name
    plData['counters'] = serializeCounters(player.counters)
                
    # serialize player's piles
    for k,v in player.piles.items():
        if len(v) == 0:
            continue
        plData['piles'].update({k: [serializeCard(c) for c in v]})

    return plData

def deserializePlayer(plData):
    if plData is None or len(plData) == 0:
        return
        
    players = [x for x in getPlayers() if x._id == plData['_id'] ]
    if players == None or len(players) == 0:
        return
        
    player = players[0]
    
    if player is None:
        return

    player.setGlobalVariable("playerID", str(plData['_id']))
    
    deserializeCounters(plData['counters'], player)
        
    if plData['piles'] is not None and len(plData['piles']) > 0:
        for k in plData['piles'].Keys:
            if k not in player.piles:
                continue
            deserializePile(plData['piles'][k], player.piles[k], player)


def deserializePile(pileData, group, who = me):
    if pileData is None or len(pileData) == 0:
        return
    if group != shared and who != me and group.controller != me:
        remoteCall(who, "deserializePile", [pileData, group, who])
    else:
        for c in pileData:
            card = group.create(c['model'])


def serializeCard(card):
    cardData = {'model':'', 'markers':{}, 'orientation':0, 'position':[], 'isFaceUp':False, 'highlight':None}
    cardData['model'] = card.model
    cardData['orientation'] = card.orientation
    cardData['markers'] = serializeCardMarkers(card)
    cardData['position'] = card.position
    cardData['isFaceUp'] = card.isFaceUp
    cardData['alternate'] = card.alternate
    cardData['anchor'] = card.anchor
    cardData['highlight'] = card.highlight
    #notify("cardData {}".format(str(cardData)))
    return cardData

def deserializeCard(cardData):
    card = table.create(cardData['model'], cardData['position'][0], cardData['position'][1], 1, True)
    if 'markers' in cardData and cardData['markers'] is not None and len(cardData['markers']) > 0:
        for key, qty in {(i['name'], i['model']): i['qty'] for i in cardData['markers']}.items():
            card.markers[key] = qty
    if 'orientation' in cardData:
        card.orientation = orientation.get(cardData['orientation'], 0)
    if 'isFaceUp' in cardData and cardData['isFaceUp'] is not None:
        card.isFaceUp = cardData['isFaceUp']
    if 'alternate' in cardData:
        card.alternate = cardData['alternate']
    if 'anchor' in cardData:
        card.anchor = cardData['anchor']
    if 'highlight' in cardData:
        card.highlight = cardData['highlight']
    return card


def serializeCounters(counters):
    if len(counters) == 0:
        return None 
    return {k: counters[k].value for k in counters}

def deserializeCounters(counters, player):
    if counters is None or len(counters) == 0:
        return
    for k in counters.Keys:
        player.counters[k].value = counters[k]


def serializeCardMarkers(card):
    if len(card.markers) == 0:
        return None
    markers = []
    for id in card.markers:
        markers.append({'name': id[0], 'model': id[1], 'qty': card.markers[id]})
    return markers
    
def serializeGlobalVariable():
    globalVariable = {'difficulty':None, 'playerList':None, 'heroesPlayed':None, 'firstPlayer':None, 'lock':None, 'game':None, 'playersSetup':None, 'villainSetup':None, 'done':None, 'phase':None, 'deckLocked':None}
    globalVariable['difficulty'] = getGlobalVariable("difficulty")
    globalVariable['playerList'] = getGlobalVariable("playerList")
    globalVariable['heroesPlayed'] = getGlobalVariable("heroesPlayed")
    globalVariable['firstPlayer'] = getGlobalVariable("firstPlayer")
    globalVariable['lock'] = getGlobalVariable("lock")
    globalVariable['game'] = getGlobalVariable("game")
    globalVariable['playersSetup'] = getGlobalVariable("playersSetup")
    globalVariable['villainSetup'] = getGlobalVariable("villainSetup")
    globalVariable['done'] = getGlobalVariable("done")
    globalVariable['phase'] = getGlobalVariable("phase")
    globalVariable['deckLocked'] = getGlobalVariable("deckLocked")
    return globalVariable

def deserializeGlobalVariable(gvKey, gvValue):
    setGlobalVariable(gvKey, gvValue)


def getSection(sections, card):
    if card.Type is not None and card.Type in sections:
        return card.Type
    if card.Subtype is not None:
        if card.Subtype in sections:
            return card.Subtype
    return None