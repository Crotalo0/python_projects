class Game:
    zones = {}
    current_zone = None

    def AddZone(key,zone):
        zones[key] = zone
        return zone

    def ChangeZone(key):
        current_zone = zones[key]
        if(current_zone == None): return 

    def OnInput(input):
        current_zone.OnInput(input)


class Zone:
    gameRef = None
    parentRef = None
    inputFn = None
    vars = {}

    def init(self,game,parent,fpointer):
        gameRef = game
        parentRef = parent
        inputFn = fpointer


    def OnInput(input):
        if(inputFn == None): return ""
        return inputFn(self,gameRef,input)

    def SetVar(key,val):
        vars[key] = val

    def GetVar(key):
        v = vars[key]
        if(v == None): return ""
        return v


def cage_logic(zone,game,input):
    if zone.GetVar("NumeroRatti") < 5:
        game.ChangeZone("stage2")


gameObj = new Game()

cage = gameObj.AddZone("cage",new Zone(gameObj,None,cage_logic))
cage.SetVar("NumeroRatti",256)

s2 = gameObj.AddZone("stage2",new Zone(gameObj,None,cage_logic))
cage.SetVar("Visandrix","Dead maybe ?")
cage.SetVar("Veldrin", True)
cage.SetVar("Idium","OmniWizard")

gameObj.OnInput(input)