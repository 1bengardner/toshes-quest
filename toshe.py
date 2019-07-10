#-------------------------------------------------------------------------------
import sys
sys.setrecursionlimit(1333337) #this gets around recursion depth error
import warnings
warnings.filterwarnings("ignore")
from Tkinter import *
import random
import time
class Game(object):
    "Toshe's Quest V. 1.24"

    def __init__(self):
    #initializes the game
        self.StartingStats()
        self.HPBar()
        self.NRGBar()
        self.bVisit = 1
        self.bShopVisit = 1
        self.bDojoVisit = 1
        self.shopNo = 0
        self.carMsg = 0
        self.wild = 0
        self.bought = 0
        self.dwOpen = 0
        self.demonKilled = 0
        self.q1 = 0
        self.q2 = 0
        self.ticket = 0
        self.ready = 10
        self.killZain = 0
        self.zainKilled = 0
        self.sBattleCounter = 0
        self.hb = 0
        self.maxHPtemp = 0
        self.maxNRGtemp = 0
        self.chosenWeapon = 0
        self.chosenAbility = 0
        self.autoKillChance = 0
        self.enemyList = []

    """Game Functions"""
    "Stats Section" 
    def StartingStats(self):    #these are the player's stats at the beginning of game
        self.name = "You"
        self.exp = 0
        self.expPrev = 0
        self.level = 1
        self.maxHP = 100
        self.HP = 100
        self.maxNRG = 100
        self.NRG = 100
        #
        self.strength = 5
        self.technique = 5
        self.SP = 0 #stat points
        #
        self.WA = 0 #weapon attack
        self.weaponAttribute = "none"
        #
        self.weapons = ["You have no weapons!",]
        self.abilities = ["Macedonian Anthem",]
        self.euros = 1
        
    def ShowStats(self):    #displays stats
        self.chosenWeapon = 0
        self.chosenAbility = 0
        self.HPBar()
        self.NRGBar()
        self.LevelUp()
        self.EXPBar()
        self.WeaponLookUp()
        self.AbilityLookUp()
        
        self.masterStats = Tk()
        self.masterStats.title(self.name+"'s Stats")
        #
        fStats = Frame(self.masterStats, border=2, relief="ridge")
        fStats.grid()
        #
        lLevel = Label(fStats, bg="black", fg="white", text="Level\n"+str
            (self.level),relief="groove").grid(column=2, row=0, rowspan=2, sticky=W+E+N+S)
        #help button
        self.helpWindow = "stats"
        bHelp = Button(fStats, bitmap="question", bg="white", command=self.Helper)
        bHelp.grid(row=0, column=2,rowspan=2, sticky=NE)
        #
        lExp = Label(fStats, justify="center", bg="black", fg="white", text="EXP: "+str
            (self.exp)+"/"+str(self.expNeeded)).grid(column=2, row=2,sticky=W+E+N+S)
        l2Exp = Label(fStats, justify="center", bg="black", fg="cyan", font="courier",
                      text=self.EXPbarpic).grid(column=2, row=3,sticky=W+E+N+S)
        lHealth = Label(fStats, justify="center", bg="green", text="Health: "+str
            (self.HP)+"/"+str(self.maxHP)).grid(column=0, row=0, sticky=W+E)
        l2Health = Label(fStats, justify="center", bg="green", font="courier",
                         text=self.HPbarpic).grid(column=0, row=1, sticky=W+E)
        lEnergy = Label(fStats, justify="center", bg="yellow", text="Energy: "+str
            (self.NRG)+"/"+str(self.maxNRG)).grid(column=0, row=2, sticky=W+E)
        l2Energy = Label(fStats, justify="center", bg="yellow", text=self.NRGbarpic,
                         font="courier").grid(column=0, row=3, sticky=W+E)
        lStrength = Label(fStats, bg="red", text="Strength: "+str
            (self.strength)).grid(column=0, row=4, sticky=W+E+N+S)
        lTechnique = Label(fStats, bg="red", text="Technique: "+str
            (self.technique)).grid(column=0, row=5, sticky=W+E+N+S)
        lWP = Label(fStats, bg="orange", fg="black", text=
            "Weapon Power: "+str(self.WA)).grid(column=2, row=4, sticky=N+S+W+E)
        lWA = Label(fStats, bg="orange", fg="black", text=
            "Attribute: "+str(self.weaponAttribute.capitalize())).grid(column=2, row=5, sticky=N+S+W+E)
        lAD = Label(fStats, bg="orange", fg="blue", relief="sunken", text=
            "Attack Power: "+str(self.WA*self.strength/2)).grid(column=2, row=6, sticky=N+S+W+E)
        lAP = Label(fStats, bg="blue", fg="orange", relief="sunken", text=
            "Ability Power: "+str(self.abilityDmg)).grid(column=2, row=7, sticky=N+S+W+E)
        lEuros = Label(fStats, justify="center", bg="lightgreen", fg="brown", text=
            "Euros: "+str(self.euros)).grid(column=0, columnspan=2, row=7, sticky=W+E)
        lPoints = Label(fStats, justify="right", bg="white", fg="black", text=
            "Stat Points Remaining").grid(column=0, columnspan=2, row=6, sticky=W+E)
        self.lPointsT = Text(fStats, height=1, width=2)
        self.lPointsT.grid(column=0, columnspan=2, row=6, sticky=E)
        self.lPointsT.insert(0.0, self.SP)
        if self.SP > 0:
            lHealthPlus = Button(fStats, justify="left", bg="red", command=self.AddHealth,
                                 text="+", height=0).grid(column=1, row=0, rowspan=2, sticky=N+S+E+W)
            lEnergyPlus = Button(fStats, justify="left", bg="red", command=self.AddEnergy,
                                 text="+", height=0).grid(column=1, row=2, rowspan=2, sticky=N+S+E+W)
            lStrengthPlus = Button(fStats, justify="left", bg="red", command=self.AddStrength,
                                   text="+", height=0).grid(column=1, row=4, sticky=N+S+E+W)
            lTechniquePlus = Button(fStats, justify="left", bg="red", command=self.AddTechnique,
                                    text="+", height=0).grid(column=1, row=5, sticky=N+S+E+W)
        else:
            pass
        bClose = Button(fStats, bg="darkred", fg="white", command=self.masterStats.destroy,
                        text="CLOSE", height=2)
        bClose.grid(column=0, columnspan=3, row=9, sticky=W+E)
        self.masterStats.mainloop()

    # - command of ShowStats
    def AddHealth(self):
        if self.SP > 0:
            self.maxHP += 15
            self.SP -= 1
            print "\nYour maximum health has increased by 15."
            self.SPChange()
        else:
            self.NoSP()

    # - command of ShowStats
    def AddEnergy(self):
        if self.SP > 0:
            self.maxNRG += 20
            self.SP -= 1
            print "\nYour maximum energy has increased by 20."
            self.SPChange()
        else:
            self.NoSP()

    # - command of ShowStats
    def AddStrength(self):
        if self.SP > 0:
            self.strength += 1
            self.SP -= 1
            print "\nYour strength has increased by 1."
            self.SPChange()
        else:
            self.NoSP()

    # - command of ShowStats
    def AddTechnique(self):
        if self.SP > 0:
            self.technique += 1
            self.SP -= 1
            print "\nYour technique has increased by 1."
            self.SPChange()
        else:
            self.NoSP()

    def SPChange(self):
        self.lPointsT.delete(0.0, END)
        self.lPointsT.insert(0.0, self.SP)

    def NoSP(self):
        print "\nYou have run out of stat points."
        self.masterStats.destroy()
        self.ShowStats()
        
    def HPBar(self):   #picture of character hitpoints(health) bar
        if self.HP == self.maxHP:
            self.HPbarpic ="(====================)"
        else:
            self.HPbarpic = "["
            for i in range(self.HP*100, 0, int(round(self.maxHP*-0.05,0)*100)):
                self.HPbarpic += "="
            for i in range(self.HPbarpic.count("="), 20, 1):
                self.HPbarpic += " "
            self.HPbarpic += "]"

    def NRGBar(self):  #picture of energy bar
        if self.NRG == self.maxNRG:
            self.NRGbarpic = "(====================)"
        else:
            self.NRGbarpic = "["
            for i in range(0, self.NRG, int(round(self.maxNRG*0.05,0))):
                self.NRGbarpic += "="
            for i in range(self.NRGbarpic.count("="), 20, 1):
                self.NRGbarpic += " "
            self.NRGbarpic += "]"

    def EXPBar(self):   #picture of experience bar
        self.EXPbarpic = "<"
        for i in range(0, self.exp-self.expPrev, int(round(self.expNeeded*0.1,0))):
            self.EXPbarpic += "-"
        for i in range(self.EXPbarpic.count("-"), 10, 1):
            self.EXPbarpic += " "
        self.EXPbarpic += ">"

    def LevelUp(self):
        self.expNeeded = self.level**2*20
        if self.exp >= self.expNeeded:
            self.expPrev = self.expNeeded
            self.level += 1
            self.SP += 5
            self.HP = self.maxHP
            self.NRG = self.maxNRG
            print "\nCongratulations! You have leveled up and received 5 stat points."
            time.sleep(0.5)
            print "You are now level",str(self.level)+"."
            try:
                import winsound
                winsound.Beep(int(1175),430)
                time.sleep(0.02)
                winsound.Beep(int(1175),150)
                winsound.Beep(int(1760),600)
            except ImportError:
                pass
            self.expNeeded = self.level**2*20
            print "You need",self.expNeeded,"experience points to level up."
            time.sleep(2)

###
###
###

    "Help Function Section"
    def Helper(self):   #help window that pops up upon clicking the "?" bitmap
    #WINDOW
        print "\nA help window has opened."
        if self.helpWindow == "button":
            masterHelp = Tk()
            masterHelp.title("Help")
            #
            fHelp = Frame(masterHelp, border=2, relief="ridge")
            fHelp.grid()
            #
            lHelp = Label(fHelp, justify=LEFT, text="""Help:
The window displays options which are in the form of clickable buttons.
 - (e.g. "yes", "no", "shop")
Each button relates to the question asked or command stated at the top of the window.
 - (e.g. "Where would you like to go?", "Choose a weapon.")
Click on a button to perform the action that is labeled on the button.""")
        elif self.helpWindow == "entry":
            masterHelp = Tk()
            masterHelp.title("Help")
            #
            fHelp = Frame(masterHelp, border=2, relief="ridge")
            fHelp.grid()
            #
            lHelp = Label(fHelp, justify=LEFT, text="""Help:
The window contains a text entry box for you to enter information.
 - (e.g. a name)
Press the submit button to submit the data you typed in the entry box.""")

        elif self.helpWindow == "battle":
            masterHelp = Tk()
            masterHelp.title("Help")
            #
            fHelp = Frame(masterHelp, border=2, relief="ridge")
            fHelp.grid()
            #
            lHelp = Label(fHelp, justify=LEFT, text="""Help:
This is the battle window.
Each image is a clickable button that performs a different action.
 - Sword: Attacks your opponent.
 - Axe: Deals a lucky strike, increasing your chance of a critical hit while sacrificing your health.
 - Checkboxes: Choose one before you click the dragon to pick your ability.
 - Dragon: Uses your ability of choice.
 - Shield: Do nothing for this turn.
 - Boots: Click on this to run away, risking a fraction of your euros in the process.
""")
        elif self.helpWindow == "stats":
            masterHelp = Tk()
            masterHelp.title("Help")
            #
            fHelp = Frame(masterHelp, border=2, relief="ridge")
            fHelp.grid()
            #
            lHelp = Label(fHelp, justify=LEFT, text="""Help:
This is the stat window, displaying all the character's statistics.
 -
Weapon Power is the base attack of the weapon. Attack Power is the average damage
done with a normal attack using the given weapon. Ability Power is the damage done
or healing done when using the first ability in your ability list.
 -
When you level up, "+" will appear beside health, energy, strength, and technique.
Click on the + to spend a stat point on the selected attribute. When used on:
Health, it will increase by 15
Energy, it will increase by 20
Strength, it will increase by 1.
Technique, it will increase by 1.
""")
        lHelp.grid()
        #
        bHelp = Button(fHelp, bg="red", text="Return",
                       width = 15, height = 1, command=masterHelp.destroy)
        bHelp.grid(padx = 15, pady = 2)
        #
        mainloop()
        ###

###
###
###

    "Look-up + Dictionary Section"
    def WeaponLookUp(self): #looks up stats of your weapon when looking at stats, selling, or using in battle
        if self.weapons[self.chosenWeapon] == "Rusty Knife":
            self.WA = 1
            self.sWeaponValue = 1
            self.weaponAttribute = "normal"
        elif self.weapons[self.chosenWeapon] == "Hand Axe":
            self.WA = 2
            self.sWeaponValue = 3
            self.weaponAttribute = "normal"
        elif self.weapons[self.chosenWeapon] == "Javelin":
            self.WA = 3
            self.sWeaponValue = 4
            self.weaponAttribute = "normal"
        elif self.weapons[self.chosenWeapon] == "Mace":
            self.WA = 4
            self.sWeaponValue = 6
            self.weaponAttribute = "critical"
        elif self.weapons[self.chosenWeapon] == "Sword":
            self.WA = 4
            self.sWeaponValue = 5
            self.weaponAttribute = "normal"
        elif self.weapons[self.chosenWeapon] == "Spear":
            self.WA = 9
            self.sWeaponValue = 7
            self.weaponAttribute = "slow"
        elif self.weapons[self.chosenWeapon] == "Rapier":
            self.WA = 6
            self.sWeaponValue = 12
            self.weaponAttribute = "normal"
        elif self.weapons[self.chosenWeapon] == "Espadon":
            self.WA = 8
            self.sWeaponValue = 25
            self.weaponAttribute = "normal"
        elif self.weapons[self.chosenWeapon] == "Claymore":
            self.WA = 20
            self.sWeaponValue = 35
            self.weaponAttribute = "slow"
        elif self.weapons[self.chosenWeapon] == "Battle Axe":
            self.WA = 22
            self.sWeaponValue = 50
            self.weaponAttribute = "slow"
        elif self.weapons[self.chosenWeapon] == "Ketchup Packet":
            self.WA = 0
            self.sWeaponValue = 1
            self.weaponAttribute = "fast"
        elif self.weapons[self.chosenWeapon] == "Root of all Evil":
            self.WA = 2
            self.sWeaponValue = 12
            self.weaponAttribute = "slow"
        elif self.weapons[self.chosenWeapon] == "Bone":
            self.WA = 1
            self.sWeaponValue = 5
            self.weaponAttribute = "critical"
        elif self.weapons[self.chosenWeapon] == "Flametongue":
            self.WA = 6
            self.sWeaponValue = 100
            self.weaponAttribute = "fast"
        elif self.weapons[self.chosenWeapon] == "Morning Star":
            self.WA = 9
            self.sWeaponValue = 50
            self.weaponAttribute = "critical"
            
    def BuyWeaponLookUp(self):    #looks up stats of weapon when buying or using dictionary
        if self.buyWeapon == "Rusty Knife":
            self.bWA = 1
            self.bWeaponValue = 4
            self.bWeaponAttribute = "normal"
            self.weaponType = "sword.gif"
        elif self.buyWeapon == "Hand Axe":
            self.bWA = 2
            self.bWeaponValue = 12
            self.bWeaponAttribute = "normal"
            self.weaponType = "axe.gif"
        elif self.buyWeapon == "Javelin":
            self.bWA = 3
            self.bWeaponValue = 16
            self.bWeaponAttribute = "normal"
            self.weaponType = "spear.gif"
        elif self.buyWeapon == "Mace":
            self.bWA = 4
            self.bWeaponValue = 24
            self.bWeaponAttribute = "critical"
            self.weaponType = "mace.gif"
        elif self.buyWeapon == "Sword":
            self.bWA = 4
            self.bWeaponValue = 20
            self.bWeaponAttribute = "normal"
            self.weaponType = "sword.gif"
        elif self.buyWeapon == "Spear":
            self.bWA = 9
            self.bWeaponValue = 28
            self.bWeaponAttribute = "slow"
            self.weaponType = "spear.gif"
        elif self.buyWeapon == "Rapier":
            self.bWA = 6
            self.bWeaponValue = 48
            self.bWeaponAttribute = "normal"
            self.weaponType = "sword.gif"
        elif self.buyWeapon == "Espadon":
            self.bWA = 8
            self.bWeaponValue = 100
            self.bWeaponAttribute = "normal"
            self.weaponType = "sword.gif"
        elif self.buyWeapon == "Claymore":
            self.bWA = 20
            self.bWeaponValue = 140
            self.bWeaponAttribute = "slow"
            self.weaponType = "sword.gif"
        elif self.buyWeapon == "Battle Axe":
            self.bWA = 22
            self.bWeaponValue = 200
            self.bWeaponAttribute = "slow"
            self.weaponType = "axe.gif"
        elif self.buyWeapon == "Ketchup Packet":
            self.bWA = 0
            self.bWeaponValue = 0
            self.bWeaponAttribute = "fast"
            self.weaponType = "ketchup.gif"
        elif self.buyWeapon == "Root of all Evil":
            self.bWA = 2
            self.bWeaponValue = 0
            self.bWeaponAttribute = "slow"
            self.weaponType = "spear.gif"
        elif self.buyWeapon == "Bone":
            self.bWA = 1
            self.bWeaponValue = 0
            self.bWeaponAttribute = "critical"
            self.weaponType = "mace.gif"
        elif self.buyWeapon == "Flametongue":
            self.bWA = 6
            self.bWeaponValue = 0
            self.bWeaponAttribute = "fast"
            self.weaponType = "sword.gif"
        elif self.buyWeapon == "Morning Star":
            self.bWA = 9
            self.bWeaponValue = 0
            self.bWeaponAttribute = "critical"
            self.weaponType = "mace.gif"
        else:
            try:
                del self.bWA
                del self.bWeaponValue
                del self.bWeaponAttribute
            except AttributeError:
                pass
    "-----"            
    def WeaponDict(self): #weapon dictionary, tells stats of any weapon
        ###
        self.masterDict = Tk()
        self.masterDict.title("Weapon Look-up")
        #
        fDict = Frame(self.masterDict, border=2)
        fDict.grid()
        #
        l2Dict = Label(fDict, border=2, text="""Weapon Dictionary:
Enter the name of a weapon you would like to look up.""")
        l2Dict.grid(row=0, column=0)
        #
        self.buyWeaponSearch = Entry(fDict)
        self.buyWeaponSearch.grid(row=1, columnspan=2, pady=2)
        #
        bDict = Button(fDict, border=2, bg="green", text="Search",
                       width = 8, height = 1, command=self.WeaponDefine)
        bDict.grid(row=2, columnspan=2, pady = 2)
        #
        #help window
        self.helpWindow = "entry"
        bDict2 = Button(fDict, border=2, bg="white", bitmap="question", command=self.Helper)
        bDict2.grid(row=0, column=1, sticky=E)
        #
        mainloop()
        ###

        
        
    # - command of WeaponDict   
    def WeaponDefine(self):   #brings up information when user presses "search" in dictionary
        self.buyWeapon = self.buyWeaponSearch.get()
        self.masterDict.destroy()
        self.BuyWeaponLookUp()
        try:
            self.bWA
            print "\n",self.buyWeapon,"has",self.bWA,"attack and",self.bWeaponAttribute,"""speed.
It costs""",self.bWeaponValue,"euros in the store."
        except AttributeError:
            print "\nInvalid weapon.  Try again.\n(Example: Gauntlet of Legends - remember capital letters)"

###        
###
###

    "Ability Look-up"
    def AbilityLookUp(self): #looks up stats of your ability when looking at stats or using in battle
        if self.abilities[self.chosenAbility] == "Macedonian Anthem":
            self.abilityAttribute = "nationalistic"
            self.abilityDesc = "This ability does 0 damage."
            self.abilityDmg = "0"
        
        elif self.abilities[self.chosenAbility] == "Bloody Socket":
            self.abilityAttribute = "special"
            self.abilityDesc = "This ability damages the enemy for half their\n\
remaining health."
            self.abilityDmg = "1/2 Enemy HP"
        
        elif self.abilities[self.chosenAbility] == "Reciprocal":
            self.abilityAttribute = "special"
            self.abilityDesc = "This ability attacks the opponent for the damage\n\
done by their previous attack times two."
            self.abilityDmg = "Enemy Dmg"
        
        elif self.abilities[self.chosenAbility] == "Thrust":
            self.abilityAttribute = "damage"
            self.abilityDesc = "This ability does 200% base damage."
            self.abilityDmg = str(int(round(self.WA*self.strength,0)))

        elif self.abilities[self.chosenAbility] == "Ragnarok":
            self.abilityAttribute = "damage"
            self.abilityDesc = "This ability is an ancient maneuver that does\n\
400% of your base damage."
            self.abilityDmg = str(int(round(self.WA*self.strength*2,0)))

        elif self.abilities[self.chosenAbility] == "Justice":
            self.abilityAttribute = "damage"
            self.abilityDesc = "This ability is a devastating blow, maiming \n\
the enemy for 1000% of your base damage."
            self.abilityDmg = str(int(round(self.WA*self.strength*5,0)))

        elif self.abilities[self.chosenAbility] == "\"Terry's\" Backhand Slap":
            self.abilityAttribute = "technique"
            self.abilityDesc = "\"PAH!\"\nThis ability does 300% of your strength as damage."
            self.abilityDmg = str(int(round(self.strength*2,0)))

        elif self.abilities[self.chosenAbility] == "Windmill":
            self.abilityAttribute = "strength"
            self.abilityDesc = "This ability does 400% of your strength as damage."
            self.abilityDmg = str(int(round(self.strength*4,0)))
            
        elif self.abilities[self.chosenAbility] == "Recovery":
            self.abilityAttribute = "heal"
            self.abilityDesc = "This ability heals 10% of your total health."
            self.abilityDmg = str(int(round(self.maxHP*0.1,0)))+" (heal)"

        elif self.abilities[self.chosenAbility] == "Rejuvenation":
            self.abilityAttribute = "heal"
            self.abilityDesc = "This ability heals 30% of your total health."
            self.abilityDmg = str(int(round(self.maxHP*0.3,0)))+" (heal)"

        elif self.abilities[self.chosenAbility] == "Restoration":
            self.abilityAttribute = "heal"
            self.abilityDesc = "This ability heals 50% of your total health."
            self.abilityDmg = str(int(round(self.maxHP*0.5,0)))+" (heal)"

        elif self.abilities[self.chosenAbility] == "Heal":
            self.abilityAttribute = "heal"
            self.abilityDesc = "This ability heals 10 base health."
            self.abilityDmg = str(int(round(self.technique*2,0)))+" (heal)"

        elif self.abilities[self.chosenAbility] == "Magic Heal":
            self.abilityAttribute = "heal"
            self.abilityDesc = "This ability heals 30 base health."
            self.abilityDmg = str(int(round(self.technique*6,0)))+" (heal)"

        elif self.abilities[self.chosenAbility] == "Ultimate Heal":
            self.abilityAttribute = "heal"
            self.abilityDesc = "This ability heals 50 base health."
            self.abilityDmg = str(int(round(self.technique*10,0)))+" (heal)"
            
        elif self.abilities[self.chosenAbility] == "Hyper Body":
            self.abilityAttribute = "enhancement"
            self.abilityDesc = "This ability increases your HP and NRG by 100% for the battle."
            self.abilityDmg = str("+ "+str(self.maxHP)+"HP & "+str(self.maxNRG)+"NRG")

        elif self.abilities[self.chosenAbility] == "Cutting Edge":
            self.abilityAttribute = "technique"
            self.abilityDesc = "This ability slices the opponent with a summoned blade,\n\
causing 1000% of your technique as damage."
            self.abilityDmg = str(int(round(self.technique*10,0)))

        elif self.abilities[self.chosenAbility] == "BFG":
            self.abilityAttribute = "technique"
            self.abilityDesc = "This ability shoots a giant beam of power at the enemy,\n\
dealing 5000% technique damage."
            self.abilityDmg = str(int(round(self.technique*50,0)))

        elif self.abilities[self.chosenAbility] == "Blast":
            self.abilityAttribute = "technique"
            self.abilityDesc = "This ability explodes your opponent, doing a damage of\n\
400% of your technique."
            self.abilityDmg = str(int(round(self.technique*4,0)))

        elif self.abilities[self.chosenAbility] == "Summoned Skull":
            self.abilityAttribute = "technique"
            self.abilityDesc = "This ability summons a giant skull that blasts your enemy,\n\
doing a damage of 3000% of your technique."
            self.abilityDmg = str(int(round(self.technique*30,0)))

        elif self.abilities[self.chosenAbility] == "Eruption":
            self.babilityAttribute = "technique"
            self.bAbilityDesc = "This ability creates an erupting volcano beneath your opponent,\n\
doing 10,000% of your technique as damage."
            self.abilityDmg = str(int(round(self.technique*100,0)))

        elif self.abilities[self.chosenAbility] == "Mass Destruction":
            self.abilityAttribute = "technique"
            self.abilityDesc = "Your opponent will be annihilated by this ability."
            self.abilityDmg = str(int(round(self.technique*1000,0)))
            
    def BuyAbilityLookUp(self):    #looks up stats of ability when buying   
        if self.buyAbility == "Bloody Socket":
            self.bAbilityValue = 250
            self.bAbilityAttribute = "special"
            self.bAbilityDesc = "This ability damages the enemy for half their\n\
remaining health."
            self.abilityType = "physical.gif"
            
        elif self.buyAbility == "Reciprocal":
            self.bAbilityValue = 80
            self.bAbilityAttribute = "special"
            self.bAbilityDesc = "This ability attacks the opponent for the damage\n\
done by their previous attack times two."
            self.abilityType = "physical.gif"
            
        elif self.buyAbility == "Thrust":
            self.bAbilityValue = 20
            self.bAbilityAttribute = "damage"
            self.bAbilityDesc = "This ability does 200% base damage."
            self.abilityType = "physical.gif"

        elif self.buyAbility == "Justice":
            self.bAbilityValue = 600
            self.bAbilityAttribute = "damage"
            self.bAbilityDesc = "This ability is a devastating blow, maiming\n\
the enemy for 1000% of your base damage."
            self.abilityType = "physical.gif"

        elif self.buyAbility == "\"Terry's\" Backhand Slap":
            self.bAbilityValue = 5
            self.bAbilityAttribute = "strength"
            self.bAbilityDesc = "\"PAH!\"\nThis ability does 300% of your strength as damage."
            self.abilityType = "hand.gif"

        elif self.buyAbility == "Windmill":
            self.bAbilityValue = 20
            self.bAbilityAttribute = "strength"
            self.bAbilityDesc = "This ability does 400% of your strength as damage."
            self.abilityType = "hand.gif"

        elif self.buyAbility == "Recovery":
            self.bAbilityValue = 15
            self.bAbilityAttribute = "heal"
            self.bAbilityDesc = "This ability heals 10% of your total health."
            self.abilityType = "medi.gif"

        elif self.buyAbility == "Rejuvenation":
            self.bAbilityValue = 50
            self.bAbilityAttribute = "heal"
            self.bAbilityDesc = "This ability heals 30% of your total health."
            self.abilityType = "medi.gif"

        elif self.buyAbility == "Restoration":
            self.bAbilityValue = 200
            self.bAbilityAttribute = "heal"
            self.bAbilityDesc = "This ability heals 50% of your total health."
            self.abilityType = "medi.gif"

        elif self.buyAbility == "Heal":
            self.bAbilityValue = 20
            self.bAbilityAttribute = "heal"
            self.bAbilityDesc = "This ability heals 10 base health."
            self.abilityType = "medi.gif"

        elif self.buyAbility == "Magic Heal":
            self.bAbilityValue = 50
            self.bAbilityAttribute = "heal"
            self.bAbilityDesc = "This ability heals 30 base health."
            self.abilityType = "medi.gif"

        elif self.buyAbility == "Ultimate Heal":
            self.bAbilityValue = 140
            self.bAbilityAttribute = "heal"
            self.bAbilityDesc = "This ability heals 50 base health."
            self.abilityType = "medi.gif"

        elif self.buyAbility == "Ragnarok":
            self.bAbilityValue = 180
            self.bAbilityAttribute = "damage"
            self.bAbilityDesc = "This ability does 400% base damage."
            self.abilityType = "physical.gif"

        elif self.buyAbility == "Hyper Body":
            self.bAbilityValue = 100
            self.bAbilityAttribute = "enhancement"
            self.bAbilityDesc = "This ability increases your HP and NRG by 100% for the battle."
            self.abilityType = "medi.gif"

        elif self.buyAbility == "Cutting Edge":
            self.bAbilityValue = 80
            self.bAbilityAttribute = "technique"
            self.bAbilityDesc = "This ability slices the opponent with a summoned blade,\n\
causing 1000% of your technique as damage."
            self.abilityType = "magic.gif"

        elif self.buyAbility == "BFG":
            self.bAbilityValue = 500
            self.bAbilityAttribute = "technique"
            self.bAbilityDesc = "This ability shoots a giant beam of power at the enemy,\n\
dealing 5000% technique damage."
            self.abilityType = "magic.gif"
            
        elif self.buyAbility == "Blast":
            self.bAbilityValue = 35
            self.bAbilityAttribute = "technique"
            self.bAbilityDesc = "This ability explodes your opponent, doing a damage of\n\
400% of your technique."
            self.abilityType = "magic.gif"
            
        elif self.buyAbility == "Summoned Skull":
            self.bAbilityValue = 300
            self.bAbilityAttribute = "technique"
            self.bAbilityDesc = "This ability summons a giant skull that blasts your enemy,\n\
doing a damage of 3000% of your technique."
            self.abilityType = "magic.gif"

        elif self.buyAbility == "Eruption":
            self.bAbilityValue = 1338
            self.bAbilityAttribute = "technique"
            self.bAbilityDesc = "This ability creates an erupting volcano beneath your opponent,\n\
doing 10,000% of your technique as damage."
            self.abilityType = "magic.gif"

        elif self.buyAbility == "Mass Destruction":
            self.bAbilityValue = 2000
            self.bAbilityAttribute = "technique"
            self.bAbilityDesc = "Your opponent will be annihilated by this ability."
            self.abilityType = "magic.gif"
            
        else:
            try:
                del self.bAbilityValue
                del self.bAbilityAttribute
            except AttributeError:
                pass

###
###
###

    "Re-usable Game Window Section"
    def Crossroads(self):   #opens a window containing a menu of places to go
                            #this crossroads method can be used multiple times
    #WINDOW
        self.masterCR = Tk()

        self.masterCR.title(self.crName+" Crossroads")
        #
        fCR = Frame(self.masterCR, border=2, relief="raised")

        fCR.grid(sticky=W+E)
        #
        crImage = PhotoImage(file="crossroads.gif")
        #
        lCR = Label(fCR, image=crImage, relief="sunken")
        lCR.grid(row=1, column=1, rowspan=5)

        l2CR = Label(fCR, text=self.crName.upper()+"\nChoose your destination.")
        l2CR.grid(row=0, column=0, columnspan=3)
        #
        if self.SP > 0: statsBG = "gold"
        else: statsBG = "green"
        #
        bCR = Button(fCR, text="View Stats", bg=statsBG, command=self.ShowStats
                     , width=21)
        bCR.grid(column=1, row=6, padx=1, pady=2)

        b2CR = Button(fCR, text="Choose Weapon", bg="green", command=self.ShowWeapons
                      , width=21)
        b2CR.grid(column=1, row=7, padx=1, pady=2)

        b4CR = Button(fCR, text="Choose Ability", bg="green", command=self.AbilityMenu
                      , width=21)
        b4CR.grid(column=1, row=8, padx=1, pady=2)
        
        b3CR = Button(fCR, text=self.shopText, command=self.curShop, width=10)
        b3CR.grid(column=0, row=1, padx=1, pady=2)

        b5CR = Button(fCR, text=self.dojoText, command=self.curDojo, width=10)
        b5CR.grid(column=2, row=2, padx=1, pady=2)

        b6CR = Button(fCR, text=self.wildText, command=self.curBattle, width=10)
        b6CR.grid(column=0, row=3, padx=1, pady=2)

        b7CR = Button(fCR, text=self.tavernText, command=self.curTavern, width=10)
        b7CR.grid(column=2, row=4, padx=1, pady=2)

        b8CR = Button(fCR, text=self.innText, command=self.curInn, width=10)
        b8CR.grid(column=0, row=5, padx=1, pady=2)
        #
        #help button
        self.helpWindow = "button"
        bHelp = Button(fCR, bitmap="question", bg="white", command=self.Helper)
        bHelp.grid(row=0, column=2, sticky=NE)
        #
        mainloop()

    def Shop(self): #opens a window containing a menu of weapons to buy
                    #this shop method can be used multiple times
    #WINDOW
        self.masterS = Tk()

        self.masterS.title(self.shopTitle)
        #
        f3S = Frame(self.masterS, border=2, relief="raised")
        f2S = Frame(self.masterS, border=2, relief="sunken")
        fS = Frame(self.masterS, border=2, relief="raised")

        f3S.grid(row=0, sticky=E+W)
        f2S.grid(row=1, sticky=E+W)
        fS.grid(row=2, sticky=E+W)
        #
        curShopKeeper = PhotoImage(file=self.shopKeeper)
        #
        bS = Button(f3S, width = 25, height = 1, text=self.weapon1,
                          command=self.BuyWeapon1, bg="green")
        bS.grid(row=1, padx = 15, pady = 2, columnspan = 4, column=1)
        
        b2S = Button(f3S, width = 25, height = 1, text=self.weapon2,
                          command=self.BuyWeapon2, bg="green")
        b2S.grid(row=2, padx = 15, pady = 2, columnspan = 4, column=1)
        
        b3S = Button(f3S, width = 25, height = 1, text=self.weapon3,
                          command=self.BuyWeapon3, bg="green")
        b3S.grid(row=3, padx = 15, pady = 2, columnspan = 4, column=1)
        
        b4S = Button(f3S, width = 25, height = 1, text=self.weapon4,
                          command=self.BuyWeapon4, bg="green")
        b4S.grid(row=4, padx = 15, pady = 2, columnspan = 4, column=1)
        
        b5S = Button(f3S, width = 25, height = 1, text=self.weapon5,
                          command=self.BuyWeapon5, bg="green")
        b5S.grid(row=5, padx = 15, pady = 2, columnspan = 4, column=1)
        
        b6S = Button(f3S, width = 25, height = 1, text=self.weapon6,
                          command=self.BuyWeapon6, bg="green")
        b6S.grid(row=6, padx = 15, pady = 2, columnspan = 4, column=1)
        
        b7S = Button(f3S, width = 15, height = 1, text="Return",
                          command=self.DeleteGoBack, bg="red")
        b7S.grid(row=10, padx = 15, pady = 2, columnspan = 4, column=1)
        #
        l2S = Label(f3S, text=self.shopMessage1)
        l2S.grid(row=7, columnspan = 4, column=1)
        lS = Label(f3S, image=curShopKeeper, relief="sunken")
        lS.grid(row = 9, columnspan=4, column=1)
        #    
        bSell = Button(f3S, width = 15, height = 1, text="Sell",
                           command=self.SellWeapon, bg="yellow")
        bSell.grid(row=8, padx = 15, pady = 2, columnspan = 4, column=1)

        #dictionary
        self.helpWindow = "button"
        bHelp = Button(f3S, bitmap="info", bg="white", command=self.WeaponDict)
        bHelp.grid(rowspan = 2, row=1, column=4, sticky=NE, padx=25)
        #help button
        bDict = Button(f3S, bitmap="question", bg="white", command=self.Helper)
        bDict.grid(rowspan = 2, row=1, column=4, sticky=NE)
        #
        mainloop()

    def Dojo(self): #opens a window containing a menu of abilities to learn
                         #this abilities method can be used multiple times
    #WINDOW
        self.masterS = Tk()

        self.masterS.title(self.dojoTitle)
        #
        f3D = Frame(self.masterS, border=2, relief="raised")

        f3D.grid(row=0, sticky=E+W)
        #
        curDojoMaster = PhotoImage(file=self.dojoMaster)
        #
        b12D = Label(f3D, text="Choose an ability to learn.", relief="groove").grid(column=1, columnspan=5, row = 0, pady=2)

        if self.level < self.levelReq1 - 3:
            firstBg = "red"
        elif self.level >= self.levelReq1:
            firstBg = "green"
        else:
            firstBg = "orange"
        if self.level < self.levelReq2 - 3:
            secondBg = "red"
        elif self.level >= self.levelReq2:
            secondBg = "green"
        else:
            secondBg = "orange"
        if self.level < self.levelReq3 - 3:
            thirdBg = "red"
        elif self.level >= self.levelReq3:
            thirdBg = "green"
        else:
            thirdBg = "orange"
        
        l3D = Label(f3D, text="Level "+str(self.levelReq1), relief="raised")
        l3D.grid(row=1, rowspan=1, column=1, pady=2)
        
        bD = Button(f3D, width = 25, height = 1, text=self.ability1,
                          command=self.BuyAbility1, bg=firstBg)
        bD.grid(row=2, padx = 15, pady = 2, column=1)
        
        b2D = Button(f3D, width = 25, height = 1, text=self.ability2,
                          command=self.BuyAbility2, bg=firstBg)
        b2D.grid(row=3, padx = 15, pady = 2, column=1)
        
        b3D = Button(f3D, width = 25, height = 1, text=self.ability3,
                          command=self.BuyAbility3, bg=firstBg)
        b3D.grid(row=4, padx = 15, pady = 2, column=1)
        
        b4D = Button(f3D, width = 25, height = 1, text=self.ability4,
                          command=self.BuyAbility4, bg=firstBg)
        b4D.grid(row=5, padx = 15, pady = 2, column=1)
        
        b5D = Button(f3D, width = 25, height = 1, text=self.ability5,
                          command=self.BuyAbility5, bg=firstBg)
        b5D.grid(row=6, padx = 15, pady = 2, column=1)

        l4D = Label(f3D, text="Level "+str(self.levelReq2), relief="raised")
        l4D.grid(row=1, column=2, columnspan=3, pady=2)
        
        b6D = Button(f3D, width = 25, height = 1, text=self.ability6,
                          command=self.BuyAbility6, bg=secondBg)
        b6D.grid(row=2, padx = 15, pady = 2, columnspan = 3, column=2)
                
        b7D = Button(f3D, width = 25, height = 1, text=self.ability7,
                          command=self.BuyAbility7, bg=secondBg)
        b7D.grid(row=3, padx = 15, pady = 2, columnspan = 3, column=2)
        
        b8D = Button(f3D, width = 25, height = 1, text=self.ability8,
                          command=self.BuyAbility8, bg=secondBg)
        b8D.grid(row=4, padx = 15, pady = 2, columnspan = 3, column=2)

        l5D = Label(f3D, text="Level "+str(self.levelReq3), relief="raised")
        l5D.grid(row=5, column=2, columnspan=3,pady=2)
        
        b9D = Button(f3D, width = 25, height = 1, text=self.ability9,
                          command=self.BuyAbility9, bg=thirdBg)
        b9D.grid(row=6, padx = 15, pady = 2, columnspan = 3, column=2)

        b10D = Button(f3D, width = 25, height = 1, text=self.ability10,
                      command = self.BuyAbility10, bg=thirdBg)
        b10D.grid(row=7, padx=15, pady=2, columnspan = 3, column = 2)
        
        b11D = Button(f3D, width = 15, height = 1, text="Return",
                          command=self.DeleteGoBack, bg="red")
        b11D.grid(row=10, padx = 15, pady = 2, columnspan = 5, column=1)
        #
        l2D = Label(f3D, text=self.dojoMessage)
        l2D.grid(row=8, columnspan = 5, column=1)
        lD = Label(f3D, image=curDojoMaster, relief="sunken")
        lD.grid(row = 9, columnspan=5, column=1)
        #help button
        bDict = Button(f3D, bitmap="question", bg="white", command=self.Helper)
        bDict.grid(rowspan = 2, row=0, column=5, sticky=NE)
        #
        mainloop()

    # - command of shop
    def DeleteGoBack(self):
        self.masterS.destroy()
        self.goBackC()

###
###
###
        
    "Weapon Menu and Preceding Value-Assigning Methods"
    def ShowWeapons(self):  #preps weaponmenu window with variables relating to equipping
        self.menuTitle = "Weapon Inventory"
        self.equipOrSell = "equip"
        self.WeaponCommand0 = self.WeaponSwap0
        self.WeaponCommand1 = self.WeaponSwap1
        self.WeaponCommand2 = self.WeaponSwap2
        self.WeaponCommand3 = self.WeaponSwap3
        self.WeaponCommand4 = self.WeaponSwap4
        self.WeaponCommand5 = self.WeaponSwap5
        self.WeaponMenu()

    def SellWeapon(self):   #preps weaponmenu window with variables relating to selling
        self.menuTitle = "Sell Weapon"
        self.equipOrSell = "sell"
        self.WeaponCommand0 = self.WeaponSell0
        self.WeaponCommand1 = self.WeaponSell1
        self.WeaponCommand2 = self.WeaponSell2
        self.WeaponCommand3 = self.WeaponSell3
        self.WeaponCommand4 = self.WeaponSell4
        self.WeaponCommand5 = self.WeaponSell5
        self.WeaponMenu()

    # - command of ShowWeapons and SellWeapon
    def WeaponMenu(self):  #brings up a window displaying weapons and lets user equip one
    #WINDOW
        weaponNumber = len(self.weapons)
        self.masterSW = Tk()
        self.masterSW.title(self.menuTitle)
        f2SW = Frame(self.masterSW, border=2, relief="groove")
        f2SW.grid(sticky=W+E)
        fSW = Frame(self.masterSW, border=2, relief="ridge")
        fSW.grid(sticky=W+E)
        lSW = Label(f2SW, text="Choose the weapon you would like to "+self.equipOrSell+".")
        lSW.grid(row=0, column=0)
        if self.equipOrSell == "sell" and len(self.weapons) == 1:
            b0SW = Button(fSW, width = 25, height=1, bg="red", fg="yellow", text="You must have a weapon!", command=self.masterSW.destroy)
            b0SW.grid(pady=2)
        else:
            b1SW = Button(fSW, width = 25, height=1, bg="blue", fg="yellow", text=self.weapons[0],command=self.WeaponCommand0)
            b1SW.grid(pady=2, sticky=NSEW)
            if len(self.weapons) >= 2:
                b2SW = Button(fSW, width = 25, height = 1, bg="yellow", text=self.weapons[1], command=self.WeaponCommand1)
                b2SW.grid(pady=2)
            if len(self.weapons) >= 3:
                b3SW = Button(fSW, width = 25, height = 1, bg="yellow", text=self.weapons[2], command=self.WeaponCommand2)
                b3SW.grid(pady=2)
            if len(self.weapons) >= 4:
                b4SW = Button(fSW, width = 25, height = 1, bg="yellow", text=self.weapons[3], command=self.WeaponCommand3)
                b4SW.grid(pady=2)
            if len(self.weapons) >= 5:
                b5SW = Button(fSW, width = 25, height = 1, bg="yellow", text=self.weapons[4], command=self.WeaponCommand4)
                b5SW.grid(pady=2)
            if len(self.weapons) == 6:
                b6SW = Button(fSW, width = 25, height = 1, bg="yellow", text=self.weapons[5], command=self.WeaponCommand5)
                b6SW.grid(pady=2)
            else:
                pass

        #help window
        self.helpWindow = "button"
        b7SW = Button(f2SW, bg="white", bitmap="question", command=self.Helper)
        b7SW.grid(row=0, column=1, sticky=E)
        
        mainloop()

###
###
###

    "Weapon Swap Section"
    # - command of WeaponMenu
    def WeaponSwap0(self):  #these methods are called depending on which weapon the user equips
        self.removedIndex = 0
        self.WeaponSwapMain()

    def WeaponSwap1(self):
        self.removedIndex = 1
        self.WeaponSwapMain()

    def WeaponSwap2(self):
        self.removedIndex = 2
        self.WeaponSwapMain()
        
    def WeaponSwap3(self):
        self.removedIndex = 3
        self.WeaponSwapMain()
        
    def WeaponSwap4(self):
        self.removedIndex = 4
        self.WeaponSwapMain()
        
    def WeaponSwap5(self):
        self.removedIndex = 5
        self.WeaponSwapMain()
        
    def WeaponSwapMain(self):   #all methods lead to this; this is the bulk of the weapon swapping method, so i made a separate method for it
        self.masterSW.destroy()
        firstWeapon = self.weapons[0] #identifies first weapon in list as firstWeapon
        removedWeapon = self.weapons[self.removedIndex]
        #^Removes the weapon from the list that the user wants to wield
        if firstWeapon == removedWeapon:    #if the first and to-be-wielded weapons are equal...
            if len(self.weapons) == 1:
                pass
            else:
                firstWeapon = self.weapons[1] #...the first weapon becomes the second
        else:
            pass
        #
        self.weapons.remove(removedWeapon)    #removes the weapon that is to be wielded
        self.weapons.append(removedWeapon)    #adds the to-be-wielded weapon to the end
        self.weapons[0] = self.weapons[-1]  #the first weapon becomes the same as the last weapon
        del self.weapons[-1]    #the last weapon is deleted, as it is a duplicate
        #
        self.weapons.append(firstWeapon)  #adds the first weapon back
        self.chosenWeapon = 0

###
###
###

    "Weapon Sell Section"
    # - command of WeaponMenu
    def WeaponSell0(self):  #these methods are called depending on which weapon the user sells
        self.sellIndex = 0
        self.SellWeaponMain()

    def WeaponSell1(self):
        self.sellIndex = 1
        self.SellWeaponMain()

    def WeaponSell2(self):
        self.sellIndex = 2
        self.SellWeaponMain()
        
    def WeaponSell3(self):
        self.sellIndex = 3
        self.SellWeaponMain()
        
    def WeaponSell4(self):
        self.sellIndex = 4
        self.SellWeaponMain()
        
    def WeaponSell5(self):
        self.sellIndex = 5
        self.SellWeaponMain()

    # - command of WeaponSellX
    def SellWeaponMain(self):   #goes here after user chooses weapon to sell from menu
        self.masterS.destroy()
        self.masterSW.destroy()
        self.buyOrSell = "sell"
        self.soldWeapon = self.weapons[self.sellIndex]
        self.chosenWeapon = self.sellIndex
        self.WeaponLookUp()
        self.buyOrSellWeapon = self.soldWeapon
        self.ConfirmCommand = self.SellWeaponMainCont
        self.WeaponConfirm()

    # - command of WeaponConfirm
    def SellWeaponMainCont(self):   #goes here after confirm window; a continuation of SellWeaponMain
        self.masterConfirm.destroy()
        self.Sold_Weapon()

    # - command of SellWeaponMainCont
    def Sold_Weapon(self):   #goes to this window if user successfully sells weapon
    #WINDOW
        self.masterSold = Tk()
        self.masterSold.title("Sold Weapon")
        #
        fSold = Frame(self.masterSold, border=2, relief="raised")
        f2Sold = Frame(self.masterSold, border=2, relief="sunken")
        f2Sold.grid(row=0)
        fSold.grid(row=1, sticky=W+E)
        #
        eurosImage = PhotoImage(file="euros.gif", master=self.masterSold)
        #
        lSold = Label(f2Sold, image=eurosImage)
        lSold.grid(column = 0)

        l2Sold = Label(fSold, text="You have just sold the weapon: "+self.soldWeapon+".")
        l2Sold.grid(row = 1, column=0)
        #
        bSold = Button(fSold, width=8, text="Return", bg="Green", command=self.SoldGoBack)
        bSold.grid(padx = 15, pady = 2, column=0, row=2)
        #
        bSold.photo = eurosImage    #saves memory or something

        mainloop()

    # - command of Sold_Weapon
    def SoldGoBack(self):
        self.masterSold.destroy()
        del self.weapons[self.sellIndex]
        self.euros += self.sWeaponValue
        print "\nYou now have",self.euros,"euros after selling your "+self.soldWeapon+"."
        self.goBack()

###
###
###

    "Weapon Buy Section"
    def BuyWeapon1(self): #these are called when user chooses a weapon from shop
        self.buyWeapon = self.weapon1
        self.BuyWeaponMain()

    def BuyWeapon2(self):
        self.buyWeapon = self.weapon2
        self.BuyWeaponMain()

    def BuyWeapon3(self):
        self.buyWeapon = self.weapon3
        self.BuyWeaponMain()

    def BuyWeapon4(self):
        self.buyWeapon = self.weapon4
        self.BuyWeaponMain()

    def BuyWeapon5(self):
        self.buyWeapon = self.weapon5
        self.BuyWeaponMain()

    def BuyWeapon6(self):
        self.buyWeapon = self.weapon6
        self.BuyWeaponMain()

    # - command of BuyWeaponX
    def BuyWeaponMain(self):  #since there are 3 lines that all BuyWeaponX methods have, it has own func
        self.masterS.destroy()
        time.sleep(1)
        if self.buyWeapon == "Zain":
            print "\nZain: \"You fudging idiot. Are you dumb?\""
            time.sleep(2)
            self.enemyList = ["Zain","Zain","Zain"]
            self.goBack = self.ShipPlaces
            self.Battle()
        else:
            self.BuyWeaponLookUp()
            if self.euros >= self.bWeaponValue:
                self.buyOrSell = "buy"
                self.buyOrSellWeapon = self.buyWeapon
                self.ConfirmCommand = self.BuyWeaponMainCont
                self.WeaponConfirm()
            else:
                print "You don't have enough euros for this! \
You still need",str(self.bWeaponValue-self.euros),"more."
                time.sleep(1)
                self.goBack()

    # - command of WeaponConfirm
    def BuyWeaponMainCont(self):    #continuation of BuyWeaponMain
        self.masterConfirm.destroy()
        self.bought = 1
        self.newWeapon = self.buyWeapon
        self.New_Weapon()

    "New Weapon Subsection"
    # - command of BuyWeaponMainCont
    def New_Weapon(self):   #go to this method if a new weapon is obtained
        if len(self.weapons) == 6:
            self.Drop_Weapon()
        else:
            self.Get_Weapon()

    # command of New_Weapon
    def Drop_Weapon(self):  #new_weapon goes to this if user has 2 many weaps
    #WINDOW
        self.dwOpen = 1
        print """\nYou have too many weapons!
Which one would you like to drop?"""
        self.masterDW = Tk()
        self.masterDW.title("Drop Weapon")
        #
        f2DW = Frame(self.masterDW, border=2, relief="groove")
        f2DW.pack(fill=X)
        fDW = Frame(self.masterDW, border=2, relief="ridge")
        fDW.pack(fill=X)
        #
        lDW = Label(f2DW, text="Choose a weapon to discard.")
        lDW.pack()
        # 
        b1DW = Button(fDW, width = 25, height = 1, text=self.weapons[0], fg="yellow", bg="black",\
                      command=self.Drop_Weapon0)
        b1DW.pack(padx = 1, pady = 2)
        
        b2DW = Button(fDW, width = 25, height = 1, text=self.weapons[1], fg="red", bg="black",\
                      command=self.Drop_Weapon1)
        b2DW.pack(padx = 1, pady = 2)
        
        b3DW = Button(fDW, width = 25, height = 1, text=self.weapons[2], fg="red", bg="black",\
                      command=self.Drop_Weapon2)
        b3DW.pack(padx = 1, pady = 2)
        
        b4DW = Button(fDW, width = 25, height = 1, text=self.weapons[3], fg="red", bg="black",\
                      command=self.Drop_Weapon3)
        b4DW.pack(padx = 1, pady = 2)
        
        b5DW = Button(fDW, width = 25, height = 1, text=self.weapons[4], fg="red", bg="black",\
                      command=self.Drop_Weapon4)
        b5DW.pack(padx = 1, pady = 2)
        
        b6DW = Button(fDW, width = 25, height = 1, text=self.weapons[5], fg="red", bg="black",\
                      command=self.Drop_Weapon5)
        b6DW.pack(padx = 1, pady = 2)
        
        b7DW = Button(fDW, text="Abort", bg="red", command=self.GoBackFunction)
        b7DW.pack(side="bottom", padx = 1, pady = 2)
        #
        mainloop()

    # - command of Drop_Weapon
    def Drop_Weapon0(self): #after drop_weapon, goes to one of these methods depending on weapon dropped
        self.weaponDropIndex = 0
        self.Drop_WeaponMain()
        
    def Drop_Weapon1(self):
        self.weaponDropIndex = 1
        self.Drop_WeaponMain()
        
    def Drop_Weapon2(self):
        self.weaponDropIndex = 2
        self.Drop_WeaponMain()
        
    def Drop_Weapon3(self):
        self.weaponDropIndex = 3        
        self.Drop_WeaponMain()
        
    def Drop_Weapon4(self):
        self.weaponDropIndex = 4
        self.Drop_WeaponMain()
        
    def Drop_Weapon5(self):
        self.weaponDropIndex = 5
        self.Drop_WeaponMain()

    # - command of Drop_WeaponX
    def Drop_WeaponMain(self):
        self.weapons.pop(self.weaponDropIndex)
        self.masterDW.destroy()
        self.dwOpen = 0
        self.New_Weapon()

    # - command of New_Weapon
    def Get_Weapon(self):   #goes to this window if user successfully gets weapon
    #WINDOW
        try:
            import winsound
            winsound.Beep(int(880),200)
            time.sleep(0.4)
            winsound.Beep(int(880),180)
            time.sleep(0.02)
            winsound.Beep(int(880),200)
            winsound.Beep(int(784),200)
            winsound.Beep(int(880),600)
        except ImportError: pass
        self.masterNW = Tk()
        self.masterNW.title("New Weapon")
        #
        fNW = Frame(self.masterNW, border=2, relief="raised")
        f2NW = Frame(self.masterNW, border=2, relief="sunken")
        f2NW.grid(row=0)
        fNW.grid(row=1, sticky=W+E)
        #
        weaponImage = PhotoImage(file=self.weaponType, master=self.masterNW)
        #
        lNW = Label(f2NW, image=weaponImage)
        lNW.grid()
        
        if self.bShopVisit == 1:
            obtainMsg = "You have just obtained the weapon: "+self.newWeapon+"!"
        else:
            obtainMsg = "You have just obtained the weapon: "+self.newWeapon+"""!
Would you like to equip it now?"""
            
        l2NW = Label(fNW, text=obtainMsg)
        l2NW.grid(row = 0, columnspan=2, column=0)
        #
        if self.bShopVisit == 1:
            bNW = Button(fNW, width=8, text="OK", bg="Green", command=self.EquipGoBack)
            bNW.grid(padx = 15, pady = 2, columnspan=2, column=0, row=1)
        else:
            bNW = Button(fNW, width=8, text="Yes", bg="Green", command=self.EquipGoBack)
            bNW.grid(padx = 15, pady = 2, column=0, row=1)
            b2NW = Button(fNW, width=8, text="No", bg="Red", command=self.GoBackFunction)
            b2NW.grid(padx = 15, pady = 2, column=1, row=1)
            bNW.grid(padx = 15, pady = 2, column=0, row=1)
        #
        bNW.photo = weaponImage    #saves memory or something

        mainloop()

    # - command of Get_Weapon
    def EquipGoBack(self):  #goes to this method after weapon obtained and equipped
        self.masterNW.destroy()
        ##
        firstWeapon = self.weapons[0]
        #
        self.weapons.append(self.newWeapon)
        self.weapons[0] = self.weapons[-1]
        del self.weapons[-1]
        #
        self.weapons.append(firstWeapon)
        ##
        self.chosenWeapon = 0
        self.WeaponLookUp()
        print "\nThe",self.weapons[0],"you have just equipped has an attack \
power of",str(self.WA)+"."
        if self.weaponAttribute == "normal" or self.weaponAttribute == "slow" or self.weaponAttribute == "fast":
            print "It has a",self.weaponAttribute,"attack speed."
        else:
            print "It improves your critical strike rating."
        
        if self.bought == 1:
            self.euros -= self.bWeaponValue
            print "You now have",self.euros,"euros."
            self.bought = 0
        else:
            pass
        
        self.goBack()

    # - command of Get_Weapon
    def GoBackFunction(self):   #goes to this method if weapon received but not equipped
        if len(self.weapons) == 6:
            self.bought = 0
        else:
            self.weapons.append(self.newWeapon)
            self.masterNW.destroy()
            self.chosenWeapon = -1
            self.WeaponLookUp()
            print "\nThe",self.weapons[-1],"you have just obtained has an attack \
power of",str(self.WA)+"."
            if self.weaponAttribute == "normal" or self.weaponAttribute == "slow" or self.weaponAttribute == "fast":
                print "It has a",self.weaponAttribute,"attack speed."
            else:
                print "It improves your critical strike rating."
            
        if self.dwOpen == 1:
            self.masterDW.destroy()
        else:
            pass
        
        if self.bought == 1:
            self.euros -= self.bWeaponValue
            print "You now have",self.euros,"euros."
            self.bought = 0
        else:
            pass

        self.chosenWeapon = 0
        self.goBack()

###
###
###

    "Weapon Confirmation Section"
    # - command of SellWeaponMain and BuyWeaponMain
    def WeaponConfirm(self):   #this is a buying confirmation window
    #WINDOW
        self.masterConfirm = Tk()
        self.masterConfirm.title("Confirm")
        #
        fConfirm = Frame(self.masterConfirm, border=2, relief="groove")
        fConfirm.grid()
        #
        lConfirm = Label(fConfirm, text="Are you sure you want to "+self.buyOrSell+" the weapon: "\
                            +self.buyOrSellWeapon+"?")
        lConfirm.grid(row=0, columnspan=2)
        #
        if self.buyOrSell == "sell":
            l2Confirm = Label(fConfirm, text="The shopkeeper will buy it for "\
                              +str(self.sWeaponValue)+" euros.")
            l2Confirm.grid(row=1, columnspan=2)
        elif self.buyOrSell == "buy":
            if self.bWeaponAttribute == "normal" or self.bWeaponAttribute == "slow" or self.bWeaponAttribute == "fast":
                middleSentence = "It has a "+str(self.bWeaponAttribute)+" speed."
            else:
                middleSentence = "It improves your critical strike rating."
            l2Confirm = Label(fConfirm, text="It has "+str(self.bWA)+" attack power."+\
            "\n"+middleSentence+"\n"+\
            "It costs "+str(self.bWeaponValue)+" euros.")
            l2Confirm.grid(row=1, columnspan=2)
        else:
            pass
        bConfirm = Button(fConfirm, text="Yes", bg="Green", width = 8, command=self.ConfirmCommand)
        bConfirm.grid(row=2, column=0, padx = 15, pady = 2)

        b2Confirm = Button(fConfirm, text="No", bg="Red", width = 8, command=self.ConfirmNo)
        b2Confirm.grid(row=2, column=1, padx = 15, pady = 2)

        mainloop()

    # - command of WeaponConfirm
    def ConfirmNo(self):    #if the user chooses "no" on confirm window
        self.masterConfirm.destroy()
        self.chosenWeapon = 0
        self.goBack()

###
###
###

    "Ability Menu and Preceding Value-Assigning Methods"
    def AbilityMenu(self):  #brings up a window displaying abilities for user to choose
    #WINDOW
        self.masterSA = Tk()
        self.masterSA.title(self.name+"'s Abilities")
        f2SA = Frame(self.masterSA, border=2, relief="groove")
        f2SA.grid(sticky=W+E)
        fSA = Frame(self.masterSA, border=2, relief="ridge")
        fSA.grid(sticky=W+E)
        lSA = Label(f2SA, text="Select an ability to place it as your first ability on the list.")
        lSA.grid(row=0, column=0)
        b1SA = Button(fSA, width = 25, height=1, bg="blue", fg="cyan", text=self.abilities[0], command=self.AbilitySwap0)
        b1SA.grid(pady=2, sticky=NSEW)
        if len(self.abilities) >= 2:
            b2SA = Button(fSA, width = 25, height = 1, bg="cyan", text=self.abilities[1], command=self.AbilitySwap1)
            b2SA.grid(pady=2)
        if len(self.abilities) >= 3:
            b3SA = Button(fSA, width = 25, height = 1, bg="cyan", text=self.abilities[2], command=self.AbilitySwap2)
            b3SA.grid(pady=2)
        if len(self.abilities) >= 4:
            b4SA = Button(fSA, width = 25, height = 1, bg="cyan", text=self.abilities[3], command=self.AbilitySwap3)
            b4SA.grid(pady=2)
        else:
            pass

        #help window
        self.helpWindow = "button"
        b7SA = Button(f2SA, bg="white", bitmap="question", command=self.Helper)
        b7SA.grid(row=0, column=1, sticky=E)
        
        mainloop()

    "Ability Swap Section"
    # - command of AbilityMenu
    def AbilitySwap0(self):  #these methods are called depending on which ability the user swaps
        self.removedIndex = 0
        self.AbilitySwapMain()

    def AbilitySwap1(self):
        self.removedIndex = 1
        self.AbilitySwapMain()

    def AbilitySwap2(self):
        self.removedIndex = 2
        self.AbilitySwapMain()
        
    def AbilitySwap3(self):
        self.removedIndex = 3
        self.AbilitySwapMain()        
        
    def AbilitySwapMain(self):   #all methods lead to this; this is the bulk of the ability swapping method, so i made a separate method for it
        self.masterSA.destroy()
        firstAbility = self.abilities[0] #identifies first ability in list as firstAbility
        removedAbility = self.abilities[self.removedIndex]
        #^Removes the ability from the list that the user wants to wield
        if firstAbility == removedAbility:    #if the first and to-be-wielded abilities are equal...
            if len(self.abilities) == 1:
                pass
            else:
                firstAbility = self.abilities[1] #...the first ability becomes the second
        else:
            pass
        #
        self.abilities.remove(removedAbility)    #removes the ability that is to be wielded
        self.abilities.append(removedAbility)    #adds the to-be-wielded ability to the end
        self.abilities[0] = self.abilities[-1]  #the first ability becomes the same as the last ability
        del self.abilities[-1]    #the last ability is deleted, as it is a duplicate
        #
        self.abilities.append(firstAbility)  #adds the first ability back
        self.chosenAbility = 0

###
###
###
        
    "Ability Buy Section"
    # - command of Dojo
    def BuyAbility1(self): #these are called when user chooses a ability from dojo
        self.buyAbility = self.ability1
        self.levelCheck1()

    def BuyAbility2(self):
        self.buyAbility = self.ability2
        self.levelCheck1()

    def BuyAbility3(self):
        self.buyAbility = self.ability3
        self.levelCheck1()

    def BuyAbility4(self):
        self.buyAbility = self.ability4
        self.levelCheck1()

    def BuyAbility5(self):
        self.buyAbility = self.ability5
        self.levelCheck1()

    def BuyAbility6(self):
        self.buyAbility = self.ability6
        self.levelCheck2()

    def BuyAbility7(self):
        self.buyAbility = self.ability7
        self.levelCheck2()

    def BuyAbility8(self):
        self.buyAbility = self.ability8
        self.levelCheck2()

    def BuyAbility9(self):
        self.buyAbility = self.ability9
        self.levelCheck3()

    def BuyAbility10(self):
        self.buyAbility = self.ability10
        self.levelCheck3()

    # - command of BuyAbility1-5
    def levelCheck1(self):
        if self.level < self.levelReq1:
            self.levelBad()
        else:
            self.BuyAbilityMain()

    # - command of BuyAbility6-8
    def levelCheck2(self):
        if self.level < self.levelReq2:
            self.levelBad()
        else:
            self.BuyAbilityMain()

    # - command of BuyAbility9-10
    def levelCheck3(self):
        if self.level < self.levelReq3:
            self.levelBad()
        else:
            self.BuyAbilityMain()

    # - command of levelCheckX
    def levelBad(self): #goes here if level is too low; saves a few lines
        self.masterS.destroy()
        print "Your level is too low to learn this ability."
        time.sleep(1)
        self.goBack()

    # - command of levelCheckX
    def BuyAbilityMain(self):  #since there are 3 lines that all BuyAbilityX methods have, it has own method
        self.masterS.destroy()
        self.BuyAbilityLookUp()
        if self.buyAbility in self.abilities:
            print "You already have learned this ability."
            time.sleep(1)
            self.goBack()
        else:
            pass
        if self.euros >= self.bAbilityValue:
            self.AbilityConfirm()
        else:
            print "You don't have enough euros for this! \
You still need",str(self.bAbilityValue-self.euros),"more."
            time.sleep(1)
            self.goBack()

    # - command of AbilityConfirm
    def BuyAbilityMainCont(self):    #continuation of BuyAbilityMain
        self.masterConfirm.destroy()
        self.bought = 1
        self.newAbility = self.buyAbility
        self.New_Ability()

    "New Ability Subsection"
    # - command of BuyAbilityMainCont
    def New_Ability(self):   #go to this method if a new ability is obtained
        if len(self.abilities) == 4:
            self.Unlearn_Ability()
        else:
            self.Get_Ability()

    # command of New_Ability
    def Unlearn_Ability(self):  #new_ability goes to this if user has 2 many weaps
    #WINDOW
        self.uaOpen = 1
        print "\nYou have too many abilities for "+self.name+"""'s low brain capacity!
Which ability would you like to forget?"""
        self.masterUA = Tk()
        self.masterUA.title("Unlearn Ability")
        #
        f2UA = Frame(self.masterUA, border=2, relief="groove")
        f2UA.pack(fill=X)
        fUA = Frame(self.masterUA, border=2, relief="ridge")
        fUA.pack(fill=X)
        #
        lUA = Label(f2UA, text="Choose an ability to unlearn.")
        lUA.pack()
        # 
        b1UA = Button(fUA, width = 25, height = 1, text=self.abilities[0], fg="cyan", bg="black",\
                      command=self.Drop_Ability0)
        b1UA.pack(padx = 1, pady = 2)
        
        b2UA = Button(fUA, width = 25, height = 1, text=self.abilities[1], fg="cyan", bg="black",\
                      command=self.Drop_Ability1)
        b2UA.pack(padx = 1, pady = 2)
        
        b3UA = Button(fUA, width = 25, height = 1, text=self.abilities[2], fg="cyan", bg="black",\
                      command=self.Drop_Ability2)
        b3UA.pack(padx = 1, pady = 2)
        
        b4UA = Button(fUA, width = 25, height = 1, text=self.abilities[3], fg="cyan", bg="black",\
                      command=self.Drop_Ability3)
        b4UA.pack(padx = 1, pady = 2)

        b7UA = Button(fUA, text="Abort", bg="red", command=self.AbilityGoBack)
        b7UA.pack(side="bottom", padx = 1, pady = 2)
        #
        mainloop()

    # - command of Drop_Ability
    def Drop_Ability0(self): #after drop_ability, goes to one of these methods depending on ability dropped
        self.abilityDropIndex = 0
        self.Drop_AbilityMain()
        
    def Drop_Ability1(self):
        self.abilityDropIndex = 1
        self.Drop_AbilityMain()
        
    def Drop_Ability2(self):
        self.abilityDropIndex = 2
        self.Drop_AbilityMain()
        
    def Drop_Ability3(self):
        self.abilityDropIndex = 3        
        self.Drop_AbilityMain()

    # - command of Drop_AbilityX
    def Drop_AbilityMain(self):
        self.abilities.pop(self.abilityDropIndex)
        self.masterUA.destroy()
        self.uaOpen = 0
        self.New_Ability()

    # - command of New_Ability
    def Get_Ability(self):   #goes to this window if user successfully gets ability
    #WINDOW
        self.masterNA = Tk()
        self.masterNA.title("New Ability")
        #
        fNA = Frame(self.masterNA, border=2, relief="raised")
        f2NA = Frame(self.masterNA, border=2, relief="sunken")
        f2NA.grid(row=0, column=0)
        fNA.grid(row=1, column=0, sticky=W+E)
        #
        abilityImage = PhotoImage(file=self.abilityType, master=self.masterNA)
        #
        lNA = Label(f2NA, image=abilityImage)
        lNA.grid()

        l2NA = Label(fNA, text="You have just learned the ability: "+self.newAbility+"!")
        l2NA.grid(row = 0, column=0, sticky=E+W)
        #
        bNA = Button(fNA, width=8, text="Continue", bg="Green", command=self.AbilityGoBack)
        bNA.grid(padx = 15, pady = 2, column=0, row=1, sticky=E+W)
        #
        bNA.photo = abilityImage    #saves memory or something

        mainloop()

    # - command of Get_Ability
    def AbilityGoBack(self):  #goes to this method after ability obtained and equipped
        if len(self.abilities) == 4:
            self.masterUA.destroy()
        else:
            self.masterNA.destroy()
            ##
            firstAbility = self.abilities[0]
            #
            self.abilities.append(self.newAbility)
            self.abilities[0] = self.abilities[-1]
            del self.abilities[-1]
            #
            self.abilities.append(firstAbility)
            ##
            self.chosenAbility = 0
            self.AbilityLookUp()

            print "\n",self.abilities[0],"is a",self.abilityAttribute+"-type ability."
        
            self.euros -= self.bAbilityValue
            print "You now have",self.euros,"euros."
            self.bought = 0
        
        self.goBack()

###
###
###

    "Ability Confirmation Section"
    # - command of SellAbilityMain and BuyAbilityMain
    def AbilityConfirm(self):   #this is a buying confirmation window
    #WINDOW
        self.masterConfirm = Tk()
        self.masterConfirm.title("Confirm")
        #
        fConfirm = Frame(self.masterConfirm, border=2, relief="groove")
        fConfirm.grid()
        #
        lConfirm = Label(fConfirm, text="Are you sure you want to buy the ability: "\
                            +self.buyAbility+"?")
        lConfirm.grid(row=0, columnspan=2)
        #
        l3Confirm = Label(fConfirm, text="Description: "+self.bAbilityDesc).grid(row=1, columnspan=2)
        #
        l2Confirm = Label(fConfirm, text="It is a "+str(self.bAbilityAttribute)+"""-type ability.
It costs """+str(self.bAbilityValue)+" euros to learn.")
        l2Confirm.grid(row=2, columnspan=2)

        bConfirm = Button(fConfirm, text="Yes", bg="Green", width = 8, command=self.BuyAbilityMainCont)
        bConfirm.grid(row=3, column=0, padx = 15, pady = 2)

        b2Confirm = Button(fConfirm, text="No", bg="Red", width = 8, command=self.ConfirmNo)
        b2Confirm.grid(row=3, column=1, padx = 15, pady = 2)

        mainloop()

    # - command of AbilityConfirm
    def ConfirmNo(self):    #if the user chooses "no" on confirm window
        self.masterConfirm.destroy()
        self.chosenAbility = 0
        self.goBack()

###
###
###

    """Gameplay Section"""
    "Bologna"
    def Beginning(self):    #beginning of the game
        try:
            import winsound
            print"      ****           *                         *                            "
            winsound.Beep(int(440),300)

            print"     *  *************                        **                             "
            winsound.Beep(int(523),300)

            print"    *     *********                          **                             "
            winsound.Beep(int(659),300)

            print"    *     *  *                               **                             "
            winsound.Beep(int(880.0),300)

            print"     **  *  **            ****       ****    **                     ****    "
            winsound.Beep(int(415.30469758),80)
            winsound.Beep(int(987.766602512),220)

            print"        *  ***           * ***  *   * **** * **  ***      ***      * **** * "
            winsound.Beep(int(659),300)

            print"       **   **          *   ****   **  ****  ** * ***    * ***    **  ****  "
            winsound.Beep(int(523),300)

            print"       **   **         **    **   ****       ***   ***  *   ***  ****       "
            winsound.Beep(int(987.766602512),300)

            print"       **   **         **    **     ***      **     ** **    ***   ***      "
            winsound.Beep(int(392),80)
            winsound.Beep(int(1046.5022612),220)

            print"       **   **         **    **       ***    **     ** ********      ***    "
            winsound.Beep(int(659),300)

            print"        **  **         **    **         ***  **     ** *******         ***  "
            winsound.Beep(int(523),300)

            print"         ** *      *   **    **    ****  **  **     ** **         ****  **  "
            winsound.Beep(int(1046.5022612),300)

            print"          ***     *     ******    * **** *   **     ** ****    * * **** *   "
            winsound.Beep(int(369.994422712),80)
            winsound.Beep(int(739.988845423),220)

            print"           *******       ****        ****    **     **  *******     ****    "
            winsound.Beep(int(587.329535835),300)

            print"             ***                              **    **   *****              "
            winsound.Beep(int(440),300)

            print"                                                    *                       "
            winsound.Beep(int(739.988845423),300)

            print"                                                   *                        "
            winsound.Beep(int(349),80)
            winsound.Beep(int(659),220)

            print"                                                  *                         "
            winsound.Beep(int(523),300)

            print"                                                 *                          "
            winsound.Beep(int(440),300)

            print"                                                                         "   
            winsound.Beep(int(523),300)

            print"                                                                      "
            time.sleep(0.3)

            print"                * ***                                                 "
            winsound.Beep(int(659),300)

            print"              *  ****                                           *     "
            winsound.Beep(int(523),300)

            print"             *  *  ***                                         **     "
            winsound.Beep(int(440),300)

            print"            *  **   ***                                        **     "
            winsound.Beep(int(392),80)
            winsound.Beep(int(783.990871963),220)
            
            print"           *  ***    *** **   ****                  ****     ******** "
            winsound.Beep(int(440),80)
            winsound.Beep(int(880),220)

            print"          **   **     **  **    ***  *    ***      * **** * ********  "
            winsound.Beep(int(440),80)
            winsound.Beep(int(880),220)

            print"          **   **     **  **     ****    * ***    **  ****     **     "
            time.sleep(0.3)
            
            print"          **   **     **  **      **    *   ***  ****          **     "
            time.sleep(0.3)

            print"          **   **     **  **      **   **    ***   ***         **     "
            time.sleep(0.3)

            print"          **   **     **  **      **   ********      ***       **     "
            time.sleep(0.3)

            print"           **  ** *** **  **      **   *******         ***     **     "
            time.sleep(0.3)

            print"            ** *   ****   **      **   **         ****  **     **     "
            winsound.Beep(int(195.997717991),300)

            print"             ***     ***   ******* **  ****    * * **** *      **     "
            winsound.Beep(int(220.0),300)

            print"              ******* **    *****   **  *******     ****        **    "
            winsound.Beep(int(220.0),300)

            print"                ***   **                 *****                        "
            time.sleep(0.3)

            print"                      **                                              "
            time.sleep(0.3)

            print"                      *                                               "
            time.sleep(0.3)

            print"                     *                                                "
            time.sleep(0.3)
            
            print"                    *                                                 "
            time.sleep(0.3)
            
        except ImportError:
            print"      ****           *                         *                            "
            time.sleep(0.1)

            print"     *  *************                        **                             "
            time.sleep(0.1)

            print"    *     *********                          **                             "
            time.sleep(0.1)

            print"    *     *  *                               **                             "
            time.sleep(0.1)

            print"     **  *  **            ****       ****    **                     ****    "
            time.sleep(0.1)

            print"        *  ***           * ***  *   * **** * **  ***      ***      * **** * "
            time.sleep(0.1)

            print"       **   **          *   ****   **  ****  ** * ***    * ***    **  ****  "
            time.sleep(0.1)

            print"       **   **         **    **   ****       ***   ***  *   ***  ****       "
            time.sleep(0.1)

            print"       **   **         **    **     ***      **     ** **    ***   ***      "
            time.sleep(0.1)

            print"       **   **         **    **       ***    **     ** ********      ***    "
            time.sleep(0.1)

            print"        **  **         **    **         ***  **     ** *******         ***  "
            time.sleep(0.1)

            print"         ** *      *   **    **    ****  **  **     ** **         ****  **  "
            time.sleep(0.1)

            print"          ***     *     ******    * **** *   **     ** ****    * * **** *   "
            time.sleep(0.1)

            print"           *******       ****        ****    **     **  *******     ****    "
            time.sleep(0.1)

            print"             ***                              **    **   *****              "
            time.sleep(0.1)

            print"                                                    *                       "
            time.sleep(0.1)

            print"                                                   *                        "
            time.sleep(0.1)

            print"                                                  *                         "
            time.sleep(0.1)

            print"                                                 *                          "
            time.sleep(0.1)

            print"                                                                         "   
            time.sleep(0.1)

            print"                                                                      "
            time.sleep(0.1)

            print"                * ***                                                 "
            time.sleep(0.1)

            print"              *  ****                                           *     "
            time.sleep(0.1)

            print"             *  *  ***                                         **     "
            time.sleep(0.1)

            print"            *  **   ***                                        **     "
            time.sleep(0.1)

            print"           *  ***    *** **   ****                  ****     ******** "
            time.sleep(0.1)

            print"          **   **     **  **    ***  *    ***      * **** * ********  "
            time.sleep(0.1)

            print"          **   **     **  **     ****    * ***    **  ****     **     "
            time.sleep(0.1)
            
            print"          **   **     **  **      **    *   ***  ****          **     "
            time.sleep(0.1)

            print"          **   **     **  **      **   **    ***   ***         **     "
            time.sleep(0.1)

            print"          **   **     **  **      **   ********      ***       **     "
            time.sleep(0.1)

            print"           **  ** *** **  **      **   *******         ***     **     "
            time.sleep(0.1)

            print"            ** *   ****   **      **   **         ****  **     **     "
            time.sleep(0.1)

            print"             ***     ***   ******* **  ****    * * **** *      **     "
            time.sleep(0.1)

            print"              ******* **    *****   **  *******     ****        **    "
            time.sleep(0.1)

            print"                ***   **                 *****                        "
            time.sleep(0.1)

            print"                      **                                              "
            time.sleep(0.1)

            print"                      *                                               "
            time.sleep(0.1)

            print"                     *                                                "
            time.sleep(0.1)
            
            print"                    *                                                 "
            time.sleep(0.1)
        time.sleep(4)
        print """Welcome to Toshe's Quest. Please do not use the X at the top of the window to
close any pop-up windows in the game. Use only the buttons inside the window."""
        time.sleep(1.5)
        raw_input("[Press 'Enter' to continue]")
        print "\n~T*Q~"
        print "\nIn the distance, you hear loud voices and old ship bells ringing.\n[Please wait...]"
        time.sleep(2.2)
        print "\n\"Montenegro!\""
        time.sleep(1)
        print "\"Montenegro!\""
        time.sleep(1)
        print "\"Last call for Montenegro!\""
        time.sleep(2)
        raw_input ("\n"+self.name+": \"Huh? Where am I?\" [Enter]")
        raw_input ("""\n\"Montenegro, glorious Montenegro! Half price tickets to Montenegro!
Far from the dangers of Macedonia!\" [Enter]""")
        raw_input ("\n"+self.name+": \"Hey, what's wrong with Macedonia!?\" [Enter]")
        print "\nA dockworker emerges from the crowd."
        time.sleep(1)
        raw_input ("""\nDockworker: \"Don't you know?
Macedonia is brimming with odd mutated beings,
and nobody wants to get near them.\" [Enter]""")
        raw_input ("\n"+self.name+": \"But I need to return to Macedonia!\" [Enter]")
        raw_input ("""\nDockworker: \"What do you think you are, a hero?
The creatures somehow managed to board the final ship leaving from
Macedonia to here, and since then they have spread all across Italy!
If you want to see another day, you'd best come on this ship!\" [Enter]""")
        raw_input ("\n"+self.name+": \"No! I must honour my homeland!\" [Enter]")
        raw_input ("""\nDockworker: \"Suit yourself.
The President of Macedonia has sealed up the entire country and
thrown away the Key, so you won't be able to get in anyway.\" [Enter]""")
        raw_input ("\n"+self.name+": ... [Enter]")
        time.sleep(1)
        raw_input ("\nDockworker: \"So, what's your name, son?\" [Enter]")
        print "\nChoose an option in the new window."
        self.NameWindow()

    def NameWindow(self):
    #WINDOW
        ###this section opens a box for user to enter a name
        self.masterBeginning = Tk()
        self.masterBeginning.title("Name Entry")
        #
        fBeginning = Frame(self.masterBeginning, border=2, relief="ridge")
        fBeginning.grid()
        #
        lBeginning = Label(fBeginning, text="Enter a name.")
        lBeginning.grid(row=0, column=0)
        #
        self.nameEntry = Entry(fBeginning)
        self.nameEntry.grid(row=1, column=0)
        #
        bBeginning = Button(fBeginning, bg="green", text="Submit", command=self.GetName)
        bBeginning.grid(row=2, column=0, padx = 15, pady = 2)
        #
        #help window
        self.helpWindow = "entry"
        bBeginning2 = Button(fBeginning, bg="white", bitmap="question", command=self.Helper)
        bBeginning2.grid(row=0, column=0, sticky=E)
        #
        mainloop()
        ###
            
    def GetName(self):  #gets the name and turns into a value of a variable
        self.name = self.nameEntry.get()
        self.masterBeginning.destroy()
        self.BeginningCont()

    def BeginningCont(self):    #a continuation of the game, since name entry must access GetName() before the intro is complete
        if self.name.lower() == "":
            raw_input ("""\nDockworker: \"I couldn't hear what you said!
I'll just name you after the local dojo, \"Toshe\".\" [Enter]""")
            self.name = "Toshe"
        else:
            pass
        raw_input ("""\nDockworker: \"I'm Matsamot.
But everyone calls me Mat for short.\" [Enter]""")
        raw_input ("\n"+self.name+": \"Ok, so can you take me to Montenegro?\" [Enter]")
        raw_input ("""\nDockworker Matsamot: \"You'll need 200 Euros to get on this ship.
Good luck getting a job, Bologna is in a recession right now!\" [Enter]""")
        print "\nMatsamot returns to the crowd of people waiting to get on the ships."
        time.sleep(2.5)
        print "\nYou scratch your head. Some white flakes drift to the ground."
        time.sleep(2)
        raw_input ("\n"+self.name+": \"Well, I guess it's time to start moving.\" [Enter]")
        print "\n~T*Q~"
        self.Bologna()

    def Bologna(self):  #this is just a fancy lead-in to the crossroads window,
                        #needed so I can give values to the variables in the Crossroads that correspond to the specific city (Bologna)
        #
        if self.bVisit == 1:
            print "\nYou depart from the dock and enter a large city. You see a sign that reads:"
        else:
            Breturn = random.randrange(1,4)
            if Breturn == 1:
                bolognaAdj = "busy"
            elif Breturn == 2:
                bolognaAdj = "overly-crowded"
            elif Breturn == 3:
                bolognaAdj = "buzzing"
            print "\nYou return to the",bolognaAdj,"city of Bologna."
        #
        print """~Bologna, Italy - Population: 384,015
Welcome!"""
        time.sleep(1)
        if self.ready == 10:
            if self.euros > 199 or self.ticket == 1:
                time.sleep(1)
                raw_input("\nMatsamot: \"Hey there! So do you have enough now?\" [Enter]")
                if self.ticket == 1:
                    raw_input("""Mat: \"Ha-ha! Don't even try to fool me!
I can see that bright ticket from here!\" [Enter]""")
                elif self.euros > 199:
                    raw_input("""Mat: \"Ha-ha! You can't fool me.
I can see your overloaded pockets from here!\" [Enter]""")
                    self.euros -= 200
                raw_input("""Mat: \"Listen, there's been some monster warnings lately, and I don't know
if we can make it for sure.\" [Enter]""")
                raw_input("""Mat: \"But word's got out recently that you're a pretty decent fighter.
I'm sure you can give those critters a whooping.\" [Enter]""")
                shipAskLoop = 1
                while shipAskLoop == 1:
                    shipAsk = raw_input("""Mat: \"So, do you think you're up to the ship ride?\"
['(y)es' or '(n)o'] -> """)
                    if shipAsk.lower() == "y" or shipAsk.lower() == "yes":
                        raw_input ("Mat: \"Anchors away!\" [Enter]")
                        shipAskLoop = 0
                        self.Ship()
                    elif shipAsk.lower() == "n" or shipAsk.lower() == "no":
                        raw_input ("Mat: \"What a pansy you are. I'll be back!\" [Enter]")
                        self.ready = 0
                        self.euros += 200
                        self.Bologna()
                    else:
                        print "*invalid answer"
            else:
                self.BolognaCont()
        else:
            self.BolognaCont()

    def BolognaCont(self):
        if self.ready != 10:
            self.ready += 1
        if self.bVisit == 1:
            raw_input ("\n"+self.name+": *Wow! There's a lot of people here for such a small place.* [Enter]")
            self.bVisit = 0
        else:
            pass
        raw_input ("\n"+self.name+": *Where should I go now?* [Enter]")
        print "\nChoose an option in the new window."
        self.crName = "Bologna"
        self.shopText = "Shop"
        self.dojoText = "Dojo"
        self.wildText = "Wilderness"
        self.tavernText = "Tavern"
        self.innText = "Well"
        self.curShop = self.BShop
        self.curDojo = self.BDojo
        self.curBattle = self.BBattle
        self.curTavern = self.BTavern
        self.curInn = self.BWell
        self.goBackC = self.Bologna
        self.Crossroads()

    def BShop(self):    #again, fancy intro to shop
        if self.wild == 0:
            self.masterCR.destroy()
        else:
            pass
        print "\n~Bologna Toolshop"
        raw_input ("You enter the shop and are greeted by a Bolognese Shopkeeper\
\nwith a Scottish Accent. [Enter]")
        lameJoke = random.randrange(1,12)
        if 4 > lameJoke > 0:
            raw_input ("Bolognese Shopkeeper: \"Oi, did ye know I make a mean sauce?\" [Enter]")   #this is run second-most often
        elif lameJoke == 4:
            raw_input ("""Bolognese Shopkeeper: \"They even named a dog after me. You know, the bolognese
dog? No? Never mind...\" [Enter]""")   #tied for last with following joke
        elif lameJoke == 5:
            raw_input ("Bolognese Shopkeeper: \"Nay, I won't sell ye any meat...\" [Enter]")    #tied for last
        else:
            raw_input ("Bolognese Shopkeeper: \"Welcome to me shop.\" [Enter]") #this is run the most often
        if self.bShopVisit == 1:
            raw_input ("""
Bolognese Shopkeeper: \"Oi, ye seem like a sturdy figure;
I'll bet ye aren't 'ere for some rakes 'n' butter knives.
Tell ye what, ye don't tell nobody, an' I'll show ye what a real weapon is!\"
[Enter]""")
            print "\nChoose an option in the new window."
            self.BShopyesno()
        else:
            print "\nChoose an option in the new window."
            self.shopTitle="Bologna Shop"
            self.shopKeeper="crazyoldman.gif"
            self.shopMessage1="Bolognese Shopkeeper: \"What would ye like today?\""
            self.weapon1 = "Hand Axe"
            self.weapon2 = "Javelin"
            self.weapon3 = "Sword"
            self.weapon4 = "Mace"
            self.weapon5 = "Spear"
            self.weapon6 = "Rapier"
            self.goBack = self.Shop
        
            self.Shop()

    def BShopyesno(self):   #opens window asking user if they accept Bolognese Shopkeeper's offer
        self.masterBSyesno = Tk()

        self.masterBSyesno.title("Bologna Shop")
        #
        f2BSyesno = Frame(self.masterBSyesno)
        fBSyesno = Frame(self.masterBSyesno, border=2, relief="raised")

        f2BSyesno.grid(row = 1, sticky=W+E)
        fBSyesno.grid(row = 2)
        #
        bShopKeeper = PhotoImage(file="crazyoldman.gif")
        #
        lBSyesno = Label(fBSyesno, image=bShopKeeper, relief="sunken")
        lBSyesno.grid(row=0, column=0, columnspan=2)
        
        l2BSyesno = Label(fBSyesno, text="Bolognese Shopkeeper: \"What do ye think?\"")
        l2BSyesno.grid(row=1, column=0, columnspan=2)
        #
        bBSyesno = Button(fBSyesno, width = 8, height = 1, text="Yes",
                          command=self.BShopYes, bg="green")
        bBSyesno.grid(row=2, column=0, padx = 15, pady = 2)
        
        b2BSyesno = Button(fBSyesno, width = 8, height = 1, text="No",
                           command=self.BShopNo, bg="red")
        b2BSyesno.grid(row=2, column=1, padx = 15, pady = 2)

        #help button
        self.helpWindow = "button"
        b3BSyesno = Button(fBSyesno, bitmap="question", bg="white", command=self.Helper)
        b3BSyesno.grid(row=0, column=1, sticky=NE)
        #

        #
        mainloop()  

    def BShopNo(self):  #this occurs when a user presses the "no" button
        self.masterBSyesno.destroy()
        self.shopNo += 1
        if self.shopNo == 4:
            print "Bolognese Shopkeeper: \"Damn ye!\""
            self.shopNo = 0
            self.Bologna()
        print "Bolognese Shopkeeper: \"I won't take no for an answer!\""
        time.sleep(1)
        self.BShopyesno()

    def BShopYes(self): #occurs when user presses "yes"
        self.goBack = self.BShopYesCont
        self.masterBSyesno.destroy()
        print "Bolognese Shopkeeper: \"Atta boy!\""
        time.sleep(1)
        raw_input ("Bolognese Shopkeeper: \"Take this as a little \"sample\" from me. Heh heh.\" [Enter]")
        raw_input ("The Bolognese Shopkeeper hands you a rusted knife! [Enter]")
        self.newWeapon = "Rusty Knife"
        self.weaponType = "sword.gif"
        self.New_Weapon()
        
    def BShopYesCont(self): #continuation, since BShopYes hops to another method half-way through
        self.weapons.remove("You have no weapons!") #this is to prevent the user from having the placeholder weapon, "You have no weapons!"
        self.wild = 0
        self.bShopVisit = 0
        raw_input ("\nSo you come back 'ere if you need anything! [Enter]")
        raw_input (self.name+": Ok. Thanks man. [Enter]")
        self.Bologna()

    def BDojo(self):    #intro to dojo
        self.masterCR.destroy()
        print "\n~Toshe's Practice House"
        raw_input ("You leave Bologna and visit the local Dojo. [Enter]")
        if self.bDojoVisit == 1:
            raw_input ("""Master Chu: You have come for the training? Right place here.
You can learn the skill for use in the battle.
Remember only four! [Enter]""")
            self.bDojoVisit = 0
        else: pass
        if self.bDojoVisit == 0:
            raw_input ("""Master Chu: This dojo is owned by great sensei Toshe.
Maybe one day he teach you. [Enter]""")
        if self.bShopVisit == 1:
            raw_input ("""Master Chu: Remember! Great warrior is only as good as his weapon.
Maybe want to buy weapon at weapon shop first. [Enter]""")
        else: pass

        print "\nChoose an option in the new window."
        self.dojoTitle="Toshe's Practice House"
        self.dojoMaster="chineseman.gif"
        if self.carMsg == 1:
            self.dojoMessage = "Master Chu: Man who run behind car get exhausted."
            self.carMsg = 0
        else:
            mChuMsgChooser = random.randrange(1,3)
            if mChuMsgChooser == 1:
                self.dojoMessage="Master Chu: Man who run in front of car get tired."
                self.carMsg = 1
            elif mChuMsgChooser == 2:
                self.dojoMessage="Master Chu: Crowded elevator smell different to midget."

        self.levelReq1 = 1
        self.levelReq2 = 3
        self.levelReq3 = 5
                
        self.ability1 = "\"Terry's\" Backhand Slap"
        self.ability2 = "Thrust"
        self.ability3 = "Blast"
        self.ability4 = "Recovery"
        self.ability5 = "Heal"
        self.ability6 = "Reciprocal"
        self.ability7 = "Rejuvenation"
        self.ability8 = "Magic Heal"
        self.ability9 = "Ragnarok"
        self.ability10 = "Hyper Body"
        self.goBack = self.Dojo
        
        self.Dojo()

    def BWell(self):    #can gain health here
        self.masterCR.destroy()
        passersby = 0
        print "\nYou approach a well in the centre of Bologna. Nobody is watching."
        time.sleep(1)
        sipLoop = 1
        sipQ = 1
        while sipLoop == 1:
            if sipQ == 2:
                print "You sit for a while."
                self.NRG += 2
                time.sleep(1)
                sip = raw_input ("Do you want to take another sip? ['(y)es' or '(n)o'] -> ")
            elif sipQ == 1:
                sip = raw_input ("Would you like to take a sip from it? ['(y)es' or '(n)o'] -> ")
            sip = sip.lower()
            if sip == "yes" or sip == "y":
                sipEffect = random.randrange(1,6)
                if sipEffect == 1:
                    raw_input ("You feel better after drinking and have restored health and energy. [Enter]")
                    self.HP += 25
                    self.NRG += 20
                    if self.HP > self.maxHP:
                        self.HP = self.maxHP
                    else:
                        pass
                elif sipEffect == 2:
                    raw_input ("You weren't all that thirsty and did not gain anything from drinking. [Enter]")
                elif sipEffect == 3:
                    raw_input ("You feel sick after drinking. [Enter]")
                    self.HP -= 3
                elif sipEffect == 4:
                    raw_input ("You notice some passersby. You walk away. [Enter]")
                    sipLoop = 0
                elif sipEffect == 5:
                    raw_input ("You feel slightly re-energized after sipping the water. [Enter]")
                    self.NRG += 10
                    
                if self.HP <= 0:
                    time.sleep(1)
                    try:
                        import winsound
                        winsound.Beep(int(329.627556913),800)
                        winsound.Beep(int(311.126983722),800)
                        winsound.Beep(int(294),800)
                    except ImportError:
                        pass
                    print "\nYou have died from bad water. Toshe's Quest ends here."
                    time.sleep(10)
                    sys.exit()
                    sipLoop = 0

                elif sipLoop == 0:
                    if self.NRG > self.maxNRG: self.NRG = self.maxNRG
                    else: pass
                    self.Bologna()

                elif sipLoop == 1:
                    sipQ = 2
                    
            elif sip == "n" or sip == "no":
                sipLoop = 0
                if self.NRG > self.maxNRG: self.NRG = self.maxNRG
                else: pass
                self.Bologna()
            else:
                sipQ = 1
                print "*invalid answer"
                
    def BTavern(self):
        self.masterCR.destroy()
        greeting = 1
        print """\nYou enter the tavern and are greeted by a large and happy, but slightly
worried-looking, bartender."""
        time.sleep(1)
        if self.q1 == 2:
            raw_input("Bartender: \"You've completed my task? Thank you!\" [Enter]")
            self.q1 = 3
            raw_input("The bartender hands you 20 euros and pats you on the back. [Enter]")
            self.euros += 20
            self.Bologna()
        elif self.q2 == 1 and "Sword" in self.weapons and self.weapons[0] != "Sword":
            raw_input("Bartender: \"Wow! This MUST be a Rumadan sword!\" [Enter]")
            raw_input("Bartender: \"Here, take this ship ticket.\" [Enter]")
            raw_input("The bartender gives you a ticket to board the boat from Bologna to Montenegro!\n[Enter]")
            self.weapons.remove("Sword")
            self.ticket = 1
            self.q2 = 3
            self.Bologna()
        else:
            barAskLoop = 1
            while barAskLoop == 1:
                if greeting == 1:
                    barAsk = raw_input("""Bartender: \"Hello, what would you like today?\"
[Type '(a)dvice', '(b)eer' (2 euros), '(k)ersal' (45 euros), or '(l)eave'] -> """)
                elif greeting == 2:
                    barAsk = raw_input("""\nBartender: \"Anything else?\"
[Type '(a)dvice', '(b)eer', '(k)ersal', or '(l)eave'] -> """)
                barAsk = barAsk.lower()
                if barAsk == "beer" or barAsk == "b":
                    raw_input("Bartender: \"Well why didn't you say so? That'll be 2 euros.\" [Enter]")
                    if self.euros < 2:
                        raw_input ("Bartender: \"Looks like you don't have enough. Come back later.\" [Enter]")
                        barAskLoop = 0
                        barAskLoop2 = 0
                        self.Bologna()
                    else:
                        self.euros -= 2
                        print "The bartender accepts 2 euros and passes you a mug of ale."
                        time.sleep(1)
                        raw_input("Bartender: \"Enjoy.\" [Enter]")
                        if self.q1 == 0:
                            raw_input("Bartender: \"Psst, hey, listen to me. I have a favour to ask of you.\" [Enter]")
                            raw_input("""Bartender: \"The Rumada clan, they're vicious I'm telling you.
They keep stealing my alcohol, threatening me with their weapons.
We need to keep Bologna safe, and I need your help.\" [Enter]""")
                            barAskLoop2 = 1
                            while barAskLoop2 == 1:
                                q1A = raw_input("""Bartender: \"Please! Kill 2 Rumadan men! Will you do it?\"
['(y)es' or '(n)o'] -> """)
                                if q1A.lower() == "y" or q1A.lower() == "yes":
                                    raw_input("Bartender: \"Thank god! Come to me when you've finished.\" [Enter]")
                                    self.q1 = 1
                                    self.killCount = 0
                                    barAskLoop = 0
                                    barAskLoop2 = 0
                                    self.Bologna()
                                elif q1A.lower() == "n" or q1A.lower() == "no":
                                    raw_input("Bartender: \"Please, re-consider this.\" [Enter]")
                                    barAskLoop = 0
                                    barAskLoop2 = 0
                                    self.Bologna()
                                else:
                                    print "*invalid answer"
                        elif self.q2 == 0 and self.q1 == 3:
                            q2A = raw_input("""Bartender: \"The other day I was just minding my own business, then suddenly
a Rumadan warrior appeared from nowhere! It scared the living daylights
out of me. So, you might have guessed, I have a another assignment for you.
If you think you're up to it, could you kill a Rumadan warrior and take his
blade?\" ['(y)es' or '(n)o'] -> """)
                            barAskLoop2 = 1
                            while barAskLoop2 == 1:
                                if q2A.lower() == "y" or q2A.lower() == "yes":
                                    raw_input("Bartender: \"Thank god! Come to me when you've finished.\" [Enter]")
                                    self.q2 = 1
                                    barAskLoop = 0
                                    barAskLoop2 = 0
                                    self.Bologna()
                                elif q2A.lower() == "n" or q2A.lower() == "no":
                                    raw_input("Bartender: \"Please, re-consider this.\" [Enter]")
                                    barAskLoop = 0
                                    barAskLoop2 = 0
                                    self.Bologna()
                                else:
                                    print "*invalid answer"
                        else:
                            self.Bologna()
                elif barAsk == "advice" or barAsk == "a":
                    adviceNum = random.randrange(1,15)
                    if adviceNum == 1:
                        raw_input( """\nBartender: \"In my opinion, having a good weapon is more important than
learning good abilities.\" [Enter]""")
                        raw_input("You use your attack more than your abilities, so invest in weapons! [Enter]")
                    elif adviceNum == 2:
                        raw_input( """\nBartender: \"You probably won't find many of this kind of weapon, but if you use
a weapon with a critical hit bonus, using lucky strike will make your chance
to strike a critical blow significantly higher than normally possible.\" [Enter]""")
                        raw_input( "You will have a high chance of causing big damage!\" [Enter]")
                    elif adviceNum == 3:
                        raw_input( """\nBartender: \"Keep an eye on your experience.
As you level up, stronger creatures will confront you, and you will be able to
use powerful abilities taught by Master Chu at the dojo.\" [Enter]""")
                    elif adviceNum == 4:
                        raw_input( """\nBartender: \"Use the well if you're feeling weak. It can be helpful,
but keep in mind that it can also harm you.\" [Enter]""")
                    elif adviceNum == 5:
                        raw_input( "\nBartender: \"Press the ? button to get help.\" [Enter]")
                    elif adviceNum == 6:
                        raw_input( "\nBartender: \"Use your stat points in one or a couple of areas. [Enter]")
                        raw_input( "Spending them willy-nilly won't make you very strong. [Enter]")
                        raw_input( """I like to spend mine on strength and health so I can make,
and take, a beating!\" [Enter]""")
                    elif adviceNum == 7:
                        raw_input( """\nBartender: \"If an enemy is too tough you can run away. Be wary of your
euros though, you can lose a lot if you carry a lot with you!\" [Enter]""")
                    elif adviceNum == 8:
                        raw_input( "\nBartender: \"Never order Molson Dry. It's just garbage.\" [Enter]")
                    elif adviceNum == 9:
                        raw_input( "\nBartender: \"Remember that you can only re-sell weapons, not abilities.\" [Enter]")
                    elif adviceNum == 10:
                        raw_input( """\nBartender: \"Technical abilities that require mental power drain your energy
more than strength-type and damage-type abilities do.\" [Enter]""")
                    else:
                        raw_input( """\nBartender: \"I can give you a nice reward for completing all the tasks
I give you. Just buy a beer and we can talk about some quests.\" [Enter]""")
                    greeting = 2
                elif barAsk == "kersal" or barAsk == "k":
                    raw_input("Bartender: \"You want my Kersal special? That'll be 45 euros.\" [Enter]")
                    if self.euros < 45:
                        raw_input ("Bartender: \"Looks like you don't have enough. Come back later.\" [Enter]")
                        barAskLoop = 0
                        barAskLoop2 = 0
                        self.Bologna()
                    else:
                        self.euros -= 45
                        print "The bartender happily takes your 45 euros and hands you a massive tankard."
                        time.sleep(1)
                        randStatGain = random.randrange(1,5)
                        if randStatGain == 1:
                            self.maxHP += 5
                            raw_input ("You drink up and gain 5 maximum health! [Enter]")
                        elif randStatGain == 2:
                            self.maxNRG += 5
                            raw_input ("You drink up and gain 5 maximum energy! [Enter]")
                        elif randStatGain == 3:
                            self.strength += 1
                            raw_input ("You drink up and gain one point of strength! [Enter]")
                        elif randStatGain == 4:
                            self.technique += 1
                            raw_input ("You drink up and gain one technique point! [Enter]")
                        raw_input("Bartender: \"Cheers!\" [Enter]")   
                        barAskLoop = 0
                        barAskLoop2 = 0
                        self.Bologna()
                elif barAsk == "leave" or barAsk == "l":
                    self.Bologna()
                else:
                    print "*invalid answer"

    def BBattle(self):
        try:
            self.masterCR.destroy()
        except:
            pass
        if self.bShopVisit == 1:
            print "\nMan: Oi! It's dangerous to go out in the tall grasses!"
            time.sleep(1.5)
            print "Man: Aye, come with me."
            time.sleep(1)
            raw_input("You travel to a shop with the Bolognese man. [Enter]")
            self.wild = 1
            self.BShop()
        else:
            self.BBattleCont()
        
            
    def BBattleCont(self):
        self.goBack = self.BBattle
        print """\nYou come to a small clearing after a short hike up a hill.
You notice little creatures and odd men gathered around.  Some look over at you.
Perhaps you can get some euros off of them.
What would you like to do: confront the animals, explore deeper, or leave?"""
        whereAskLoop = 1
        while whereAskLoop == 1:
            where = raw_input("['(c)onfront (or [Enter])', '(e)xplore', or '(l)eave'] -> ")
            where = where.lower()
            if where == "c" or where == "confront" or where == "":
                print "\nYou are under attack!"
                whereAskLoop = 0
                self.enemyList = ["Mutated_Tree","Rumadan_Man",\
                "Sean_Anderson","Goblin","Blue_Snail","Green_Goblin","Rumadan_Warrior"]
                self.Battle()
            elif where == "e" or where == "explore":
                dangerAskLoop = 1
                while dangerAskLoop == 1:
                    danger = raw_input("It's very dangerous. Are you sure? ['(y)es' or '(n)o'] ->")
                    if danger == "y" or danger == "yes":
                        dangerAskLoop = 0
                        if self.level < 4:
                            print "\nOn second thought, you decide to stay where you are.\nThe wilderness looks too dangerous for you right now."
                            print "What would you like to do?"
                        else:
                            if self.demonKilled == 1:
                                print "\nThere's nothing here. You travel back to the hill."
                                print "Where would you like to go?"
                            else:
                                print "\nYou travel deep into the wilderness."
                                time.sleep(2)
                                demon = random.randrange(1,6)
                                if demon == 1:
                                    self.enemyList = ["Wildy_PKer","Lesser_Demon"]
                                    print "\nYou are attacked by an extraordinary foe!"
                                    self.demonKilled = 1
                                    whereAskLoop = 0
                                    self.Battle()
                                elif demon == 2:
                                    jackpot = random.randrange(70,131)
                                    self.euros += int(jackpot)
                                    print "\nJackpot!",
                                    time.sleep(1)
                                    raw_input ("You found a gigantic treasure chest containing "+str(jackpot)+" euros! [Enter]")
                                    print "You travel back to the hill. Where would you like to go next?"
                                else:
                                    raw_input("\nYou find nothing of interest. [Enter]")
                                    print "You travel back to the hill. What would you like to do?"
                    elif danger == "n" or danger == "no":
                        dangerAskLoop = 0
                        print "\nYou go back to the hill. What would you like to do?"
                    else:
                        print "*invalid answer"

                    
            elif where == "l" or where == "leave" or where == "bologna":
                whereAskLoop = 0
                self.Bologna()
            else:
                print "*invalid answer"

    "Ship"
    def Ship(self):
        print "\n~T*Q~"
        print "\n..."
        time.sleep(3)
        raw_input("""\nAnnouncer: \"Welcome aboard the S.S. Pakistan.
We hope you enjoy your cruise.\" [Enter]""")
        raw_input("""\nMat: \"Oh yeah, did I forget to tell you?
This is the most luxurious ship in Italy!\" [Enter]""")
        raw_input("""\nMat: \"Well I'm gonna have a little snooze.
Why don't you make use of yourself and help downstairs.\" [Enter]""")
        print "\nMatsamot makes a gesture towards you and promptly falls asleep."
        time.sleep(1)
        print "\n"+self.name+": *I'm bored...*"
        time.sleep(1)
        self.ShipPlaces()
        
    def ShipPlaces(self):
        print "\nYou see a sign that lists all the nearby places on the ship."
        print "\nChoose an option in the new window."
        self.crName = "S. S. Pakistan"
        self.shopText = "Vendor"
        self.dojoText = "Little Mosque"
        self.tavernText = "Inn"
        self.wildText = "1st Level"
        self.innText = "Restaurant"
        self.curShop = self.SShop
        self.curDojo = self.SDojo
        self.curTavern = self.SInn
        self.curBattle = self.SBattle
        self.curInn = self.SRest
        self.goBackC = self.ShipPlaces
        self.Crossroads()

    def SShop(self):
        self.masterCR.destroy()
        print "\n~Pakistan Weapons"
        print "Zain the Vendor: \"Howdy y'all.\""
        time.sleep(1)
        print "\nChoose an option in the new window."
        self.shopTitle="S.S.P. Vendor"
        self.shopKeeper="zain.gif"
        self.shopMessage1="Zain: \"Sup bra?\""
        self.weapon1 = "Sword"
        self.weapon2 = "Rapier"
        self.weapon3 = "Espadon"
        self.weapon4 = "Claymore"
        self.weapon5 = "Battle Axe"
        self.weapon6 = "Zain"
        self.goBack = self.Shop
    
        self.Shop()

    def SDojo(self):
        self.masterCR.destroy()
        print "\n~Moose's Dojo"
        print "Moose: \"I can teach you some pretty cool stuff.\""
        time.sleep(2)

        self.levelReq1 = 5
        self.levelReq2 = 7
        self.levelReq3 = 3
                
        self.ability1 = "Summoned Skull"
        self.ability2 = "Hyper Body"
        self.ability3 = "Restoration"
        self.ability4 = "Ultimate Heal"
        self.ability5 = "BFG"
        self.ability6 = "Eruption"
        self.ability7 = "Justice"
        self.ability8 = "Bloody Socket"
        self.ability9 = "Cutting Edge"
        self.ability10 = "Reciprocal"
        self.goBack = self.Dojo

        self.dojoTitle="Master Memon"
        self.dojoMaster="ravi.gif"
        
        if self.killZain == 0:
            self.dojoMessage = "Hey, can you kill Zain for me? That would be SO joeks."
            self.killZain = 1
        elif self.zainKilled == 1:
            self.dojoMessage = "Wow, that's so jokes."
            self.killZain = 0
        
        self.Dojo()

    def SInn(self):
        self.masterCR.destroy()
        print "\n~Ship Inn"
        print "At the inn, you are greeted by a young lady."
        time.sleep(1.5)
        innAskLoop = 1
        while innAskLoop == 1:
            stay = raw_input ("""Lady: \"Welcome to the inn. Would you like a room? It's 40 euros a night.\"
['(y)es' or '(n)o'] -> """)
            stay = stay.lower()
            if stay == "y" or stay == "yes":
                raw_input ("Lady: \"I'm sure you will be just full of energy by tomorrow.\" [Enter]")
                print "You awaken feeling fully energized."
                self.euros -= 40
                self.NRG = self.maxNRG
                innAskLoop = 0
                time.sleep(1)
                self.ShipPlaces()
            elif stay == "n" or stay == "no":
                raw_input ("Lady: \"Enjoy your stay on the S. S. Pakistan.\" [Enter]")
                innAskLoop = 0
                self.ShipPlaces()
            else:
                print "*invalid answer"

    def SRest(self):
        self.masterCR.destroy()
        self.goBack = self.SRest
        print "\n~Sikh Shack"
        raw_input("Jagvinder: \"Welcome to the Sikh Shack. Our food is healthy and is even known to cure disease.\nCan I take your order?\" [Enter]")
        self.masterS = Tk()
        self.masterS.title("Sikh Shack")
        jagPic = PhotoImage(file="jag.gif")
        l1R = Label(self.masterS, image=jagPic).grid(row=4)
        l2R = Label(self.masterS, text="These items increase your health.").grid(row=0)
        b1R = Button(self.masterS, text="Roti", command=self.buyRoti, width=25).grid(row=1, pady=5)
        b2R = Button(self.masterS, text="Naan",command=self.buyNaan, width=25).grid(row=2, pady=5)
        b3R = Button(self.masterS, text="Samosas",command=self.buySamosas, width=25).grid(row=3, pady=5)
        b4R = Button(self.masterS, text="Return", bg="red", command=self.DeleteGoBack, width=15).grid(row=5, pady=5)
        self.masterS.mainloop()

    # - command of SRest
    def buyRoti(self):
        self.foodItem = "roti"
        self.foodHP = 30
        self.foodPrice = 40
        self.foodConfirm()

    # - command of SRest
    def buyNaan(self):
        self.foodItem = "naan"
        self.foodHP = 50
        self.foodPrice = 60
        self.foodConfirm()

    # - command of SRest
    def buySamosas(self):
        self.foodItem = "samosas"
        self.foodHP = 100
        self.foodPrice = 110
        self.foodConfirm()

    # - ^
    def foodConfirm(self):
        self.masterConfirm = Tk()
        self.masterConfirm.title("Confirm")
        #
        fConfirm = Frame(self.masterConfirm, border=2, relief="groove")
        fConfirm.grid()
        #
        lConfirm = Label(fConfirm, text="Are you sure you want to buy "+self.foodItem+"""?
It costs """+str(self.foodPrice)+" euros.")
        lConfirm.grid(row=0, columnspan=2)
        
        bConfirm = Button(fConfirm, text="Yes", bg="Green", width = 8, command=self.foodYes)
        bConfirm.grid(row=3, column=0, padx = 15, pady = 2)

        b2Confirm = Button(fConfirm, text="No", bg="Red", width = 8, command=self.foodNo)
        b2Confirm.grid(row=3, column=1, padx = 15, pady = 2)

        self.masterConfirm.mainloop()

    def foodYes(self):
        if self.foodPrice > self.euros:
            print "\nYou don't have enough money to buy this."
            self.masterConfirm.destroy()
        else:
            self.masterS.destroy()
            self.masterConfirm.destroy()
            self.HP += self.foodHP
            if self.HP > self.maxHP:
                self.HP = self.maxHP
            else:
                pass
            self.euros -= self.foodPrice
            print "\nThe "+self.foodItem+" healed "+str(self.foodHP)+" health."
            time.sleep(1)
            self.goBackC()

    def foodNo(self):
        self.masterS.destroy()
        self.masterConfirm.destroy()
        self.goBackC()

    def SBattle(self):
        self.masterCR.destroy()
        print "\n~First Level of the Ship"
        if self.sBattleCounter == 15:
            self.FindSeaman()
        else:
            self.goBack = self.ShipPlaces
            raw_input("\nSeaman 1: \"G'day mate. Good onya for helpin' us out here.\" [Enter]")
            raw_input("Seaman 2: \"Greetings. How many more leagues until we reach Montenegro?\"\n[Enter]")
            raw_input("Seaman 1: \"About "+str(15-self.sBattleCounter)+" left.\" [Enter]")
            raw_input("Seaman 2: \"Hey Steve, look over there!\" [Enter]")
            raw_input("Seaman 1: \"Crikey!\" [Enter]")
            self.sBattleCounter += 1
            print "A creature boards the ship and rushes towards the crew!"
            time.sleep(1)
            self.enemyList = ["Goblin","Green_Goblin","Squig","Satanic_Bear","Fire_Goblin","Kraken","Goblin_King"]
            self.Battle()

    def FindSeaman(self):
        print "It's night-time."
        time.sleep(1)
        raw_input("\nSeaman 2: \"Phew. Finally. I think that'll be all the beasts for now.\" [Enter]")
        raw_input("\nSeaman 3: \"Hey, look at that! We've reached land!\" [Enter]")
        raw_input("\nSeaman 2: \"I didn't know there was a 3rd seaman...\" [Enter]")
        print "\nThe 2nd seaman has a puzzled look on his face."
        time.sleep(2)
        raw_input ("\nYou try to see who the third seaman is, but he vanishes quickly. [Enter]")
        raw_input ("\n"+self.name+": *I'm going to investigate...* [Enter]")
        print "\nYou noticed he went into a nearby cabin. You enter the cabin."
        print "The seaman's not around, do you want to look under the table or exit the cabin?"
        self.Where1()

    def Where1(self):
        whereFind = raw_input("\n['(t)able' or '(e)xit'] -> ")
        whereFind = whereFind.lower()
        if whereFind == "t" or whereFind == "table":
            print "\nA creature pops out from under the table!"
            time.sleep(1)
            self.enemyList = ["Squig","Squig","Squig"]
            self.goBack = self.Where1
            self.Battle()
        elif whereFind == "e" or whereFind == "exit":
            self.Where2()
        else:
            print "*invalid answer"
            self.Where1()

    def Where2(self):
        print """\nYou see the seaman climbing a rope. He went out the back door of the cabin!
Will you shout at him or run towards him?\""""
        whereFind = raw_input("['(s)hout' or '(r)un'] -> ")
        whereFind = whereFind.lower()
        if whereFind == "s" or whereFind == "shout":
            print "\nYou've woken up an angry passenger!"
            self.enemyList = ["Rumadan_Man","Sean_Anderson","Zain"]
            time.sleep(1)
            self.goBack = self.Where2
            self.Battle()
        elif whereFind == "r" or whereFind == "run":
            self.Where3()
        else:
            print "*invalid answer"
            self.Where2()

    def Where3(self):
        raw_input ("\nYou notice the seaman jump from the rope as you run towards him. [Enter]")
        time.sleep(1)
        raw_input("He landed back inside the cabin! [Enter]")
        print "Will you chase him back to the cabin or wait cautiously outside?"
        whereFind = raw_input("['(c)hase' or '(w)ait'] -> ")
        whereFind = whereFind.lower()
        if whereFind == "c" or whereFind == "chase":
            print "\nThe seaman's not around, do you want to look under the table or exit the cabin?"
            self.Where1()
        elif whereFind == "w" or whereFind == "wait":
            self.Where4()
        else:
            print "*invalid answer"
            self.Where3()

    def Where4(self):
        print "The figure slowly opens the cabin door."
        time.sleep(1)
        print ".",
        time.sleep(1)
        print ".",
        time.sleep(1)
        print "."
        time.sleep(1)
        print "You examine the 3rd seaman more closely..."
        time.sleep(3)
        print "...and suddenly you are filled with rage."
        time.sleep(1.5)
        print "\n\"TOMAS!\""
        time.sleep(1)
        print "\"TOMAS!\""
        time.sleep(1)
        print "\"TOMAS! YOU!\""
        time.sleep(1)
        raw_input("""\nTomas Tam: \"Ha-ha-ha! Yes! It is I! Your Macedonian brother!
I've come to take care of things here.\" [Enter]""")
        raw_input("\n"+self.name+""": \"You've already done enough by taking mom and dad's souls.
What more do you want!?\" [Enter]""")
        raw_input("\nTomas Tam: \"Hah hah. Why do you think there are so many creatures around?\"\n[Enter]")
        print "\n"+self.name+" takes a time-out to think."
        time.sleep(3)
        raw_input("\nTomas Tam: \"Those are the people whose souls I have taken, you fool!\" [Enter]")
        raw_input("\n"+self.name+": \"Yeah... I knew that...\" [Enter]")
        raw_input("""\nTomas Tam: \"And now, now that I have all these minions at my disposal, I can
conquer Macedonia once and for all!\"""")
        raw_input("\n"+self.name+": \"No! I won't let you!\" [Enter]")
        raw_input("""\nTomas Tam: \"Just like that time you \"didn't let me\" steal Darko's soul?
HA-HA-HA!\" [Enter]""")
        raw_input("\n"+self.name+""": \"How dare you bring that up!
(Although I did make a lot of money selling his runescape account to Chris...)\"""")
        raw_input("""\nTomas Tam: \"Anyway, I just wanted to let you know that Macedonia is no more.
I have the key stashed away somewhere on this boat, now all I need to do is
release the souls of these creatures so the people of Macedonia no longer need
be afraid to live there. They will love me! I will be the king! Ha-ha!
And remember... the only reason I'm not inclined to hurt you is because I still
appreciate that you picked me as your brother from the adoption center!
Ha-ha! I bet you regret that one!\" [Enter]""")
        print "\n"+self.name+": ..."
        time.sleep(1)
        print self.name+": \"I've had enough of you Tomas Tam!\""
        time.sleep(1)
        print self.name+": \"Let's settle this once and for all! FOR MACEDONIA!"
        time.sleep(1)
        self.enemyList = ["Tomas_Tam","Tomas_Tam","Tomas_Tam"]
        self.Battle()
        self.goBack = self.EndGame

    "Battle Section"    
    def Battle(self):   #main battle settings
        self.enemyDamage = 0
        self.chosenWeapon = 0
        self.firstRound = 1
        enemyCry = 0
        self.luckyEffect = 0
        self.WeaponLookUp()
        if self.weaponAttribute == "critical":
            self.baseCrit = 18
        else:
            self.baseCrit = 21
        self.AbilityLookUp()
        self.trialCounter = 0
        if self.weaponAttribute == "slow":
            self.turn = 1
        elif self.weaponAttribute == "fast":
            self.turn = 4
        else:
            self.turn = 2
        self.Start()
        
    "Calculators Section"
    def NormalAttack(self): #these are different atk types
        self.damage = self.WA * self.strength / 2
        self.damageLow = int(round(self.damage * 0.8,0))
        self.damageHigh = int(round(self.damage * 1.2,0))
        self.dmgMsg = ""
        self.Attack()

    def StrengthAttack(self):
        self.damage = int(round(self.strength*self.strMultiplier,0))
        self.damageLow = int(round(self.damage * 0.8,0))
        self.damageHigh = int(round(self.damage * 1.2,0))
        self.Attack()

    def TechAttack(self):
        self.damage = int(round(self.technique*self.techMultiplier,0))
        self.damageLow = int(round(self.damage * 0.8,0))
        self.damageHigh = int(round(self.damage * 1.2,0))
        self.Attack()

    def DmgAttack(self):
        self.damage = int(round(self.WA*self.strength*self.dmgMultiplier/2,0))
        self.damageLow = int(round(self.damage * 0.8,0))
        self.damageHigh = int(round(self.damage * 1.2,0))
        self.Attack()

    def HealAttack(self):
        if self.healType == "percent":
            healAmt = int(round(self.maxHP*self.healMultiplier,0))
        else:
            healAmt = int(round(self.technique*self.healMultiplier,0))
        self.HP += healAmt
        self.attackMsg = self.name+" healed "+str(healAmt)+" health."
        if self.HP > self.maxHP:
            self.HP = self.maxHP
        else:
            pass
        self.MainBattle()

    def AbilAttack(self):
        reps = {" ":"_","\"":"","'":""} 
        abilChoice = self.v.get()
        if abilChoice=="0":
            abilMethod = "self."+self.abilities[0]+"()"
            exec self.replace_all(abilMethod,reps)
        elif abilChoice=="1":
            abilMethod = "self."+self.abilities[1]+"()"
            exec self.replace_all(abilMethod,reps)
        elif abilChoice=="2":
            abilMethod = "self."+self.abilities[2]+"()"
            exec self.replace_all(abilMethod,reps)
        elif abilChoice=="3":
            abilMethod = "self."+self.abilities[3]+"()"
            exec self.replace_all(abilMethod,reps)
        else:
            print "\nChoose an ability."

    def replace_all(self, text, dic):   
        for i, j in dic.iteritems():   
            text = text.replace(i, j)  
        return text
###
###
###
    "Ability Section"
#miscellaneous abilities
    def Macedonian_Anthem(self):
        if self.NRG < 1:
            print "You don't have enough energy to use this."
        else:
            self.NRG -= 1
            self.autoKillChance = random.randrange(1,101)
            self.damage = 0
            self.damageLow = 0
            self.damageHigh = 0
            maceAnthem = random.randrange(1,5)
            if maceAnthem == 1:
                self.dmgMsg = "Denes nad Makedonija se ragja~...\n"
            elif maceAnthem == 2:
                self.dmgMsg = "...novo sonce na slobodata~\n"
            elif maceAnthem == 3:
                self.dmgMsg = "Makedoncite se borat~...\n"
            elif maceAnthem == 4:
                self.dmgMsg = "...za svoite pravdini!~\n"
            self.Attack()

    def Reciprocal(self):
        if self.NRG < 15:
            print "You don't have enough energy to use this."
        else:
            self.NRG -= 15
            self.damage = int(self.enemyDamage*2)
            try:
                self.damageLow = round(self.damage * 0.8,0)
                self.damageHigh = round(self.damage * 1.2,0)
            except:
                self.damageLow = 0
                self.damageHigh = 0
            self.dmgMsg = "ReCiPrOcAl! "
            self.Attack()

    def Bloody_Socket(self):
        if self.NRG < 30:
            print "You don't have enough energy to use this."
        else:
            self.NRG -= 30
            self.damage = self.enemyHP/2
            self.damageLow = round(self.damage * 0.8,0)
            self.damageHigh = round(self.damage * 1.2,0)
            self.dmgMsg = "Bloodyyyyyyyyyy SOCKET! "
            self.Attack()

    def Hyper_Body(self):
        if self.hb == 1:
            print "You can't use this ability again."
        else:
            if self.NRG < 30:
                print "You don't have enough energy to use this."
            else:
                self.NRG -= 30
                self.hb = 1
                self.maxHPtemp = self.maxHP
                self.maxNRGtemp = self.maxNRG
                self.maxHP *= 2
                self.maxNRG *= 2
                self.attackMsg = self.name+" used Hyper Body!"
                self.MainBattle()
#strength abilities
    def Terrys_Backhand_Slap(self):
        if self.NRG < 2:
            print "You don't have enough energy to use this."
        else:
            self.NRG -= 2
            self.strMultiplier = 3
            self.dmgMsg = self.name+": \"PAH!\" "
            self.StrengthAttack()

    def Windmill(self):
        if self.NRG < 5:
            print "You don't have enough energy to use this."
        else:
            self.NRG -= 5
            self.strMultiplier = 4
            self.dmgMsg = "Windmill kick! "
            self.StrengthAttack()
#damage abilities
    def Thrust(self):
        if self.NRG < 5:
            print "You don't have enough energy to use this."
        else:
            self.NRG -= 5
            self.dmgMultiplier = 2
            self.dmgMsg = "Thrust! "
            self.DmgAttack()

    def Ragnarok(self):
        if self.NRG < 9:
            print "You don't have enough energy to use this."
        else:
            self.NRG -= 9
            self.dmgMultiplier = 4
            self.dmgMsg = "Ragnarok! "
            self.DmgAttack()

    def Justice(self):
        if self.NRG < 20:
            print "You don't have enough energy to use this."
        else:
            self.NRG -= 20
            self.dmgMultiplier = 10
            self.dmgMsg = "Justice! "
            self.DmgAttack()
#technique abilities
    def Blast(self):
        if self.NRG < 5:
            print "You don't have enough energy to use this."
        else:
            self.NRG -= 5
            self.techMultiplier = 4
            self.dmgMsg = "Blast! "
            self.TechAttack()

    def Cutting_Edge(self):
        if self.NRG < 12:
            print "You don't have enough energy to use this."
        else:
            self.NRG -= 12
            self.techMultiplier = 10
            self.dmgMsg = "Cutting Edge! "
            self.TechAttack()

    def Summoned_Skull(self):
        if self.NRG < 30:
            print "You don't have enough energy to use this."
        else:
            self.NRG -= 30
            self.techMultiplier = 30
            self.dmgMsg = "Summoned Skull! "
            self.TechAttack()

    def BFG(self):
        if self.NRG < 40:
            print "You don't have enough energy to use this."
        else:
            self.NRG -= 40
            self.techMultiplier = 50
            self.dmgMsg = "B... F... G...! "
            self.TechAttack()

    def Eruption(self):
        if self.NRG < 50:
            print "You don't have enough energy to use this."
        else:
            self.NRG -= 50
            self.techMultiplier = 100
            self.dmgMsg = "\"Garet casts ERUPTION!\" "
            self.TechAttack()

    def Mass_Destruction(self):
        if self.NRG < self.maxNRG:
            print "You don't have enough energy to use this."
        else:
            self.NRG = 0
            self.techMultiplier = 1000
            self.dmgMsg = "\"MACEDONIA!\" "
            self.TechAttack()
#healing abilities            
    def Recovery(self):
        if self.NRG < 10:
            print "You don't have enough energy to use this."
        else:
            self.NRG -= 10
            self.healType = "percent"
            self.healMultiplier = 0.1
            self.HealAttack()

    def Rejuvenation(self):
        if self.NRG < 20:
            print "You don't have enough energy to use this."
        else:
            self.NRG -= 20
            self.healType = "percent"
            self.healMultiplier = 0.3
            self.HealAttack()

    def Restoration(self):
        if self.NRG < 30:
            print "You don't have enough energy to use this."
        else:
            self.NRG -= 30
            self.healType = "percent"
            self.healMultiplier = 0.5
            self.HealAttack()

    def Heal(self):
        if self.NRG < 10:
            print "You don't have enough energy to use this."
        else:
            self.NRG -= 10
            self.healType = "int"
            self.healMultiplier = 2
            self.HealAttack()

    def Magic_Heal(self):
        if self.NRG < 20:
            print "You don't have enough energy to use this."
        else:
            self.NRG -= 20
            self.healType = "int"
            self.healMultiplier = 6
            self.HealAttack()

    def Ultimate_Heal(self):
        if self.NRG < 30:
            print "You don't have enough energy to use this."
        else:
            self.NRG -= 30
            self.healType = "int"
            self.healMultiplier = 10
            self.HealAttack()

    "Main Battle Section"
    def Attack(self):   #main attack window
        if self.luckyEffect == 1:
            maxCrit = self.baseCrit - 15
        else:
            maxCrit = self.baseCrit
        critDmg = int(round(self.damage*2,0))
        if self.damageLow == self.damageHigh:
            normDmg = self.damageLow
        else:
            normDmg = random.randrange(round(self.damageLow,0),\
                                       round(self.damageHigh,0)+1)
        criticalChooser = random.randrange(1,maxCrit)
        if criticalChooser == maxCrit - 1:
            randDmg = int(critDmg)
            self.dmgMsg += "CRITICAL HIT! "
            dmgPunc = "!"
        else:
            randDmg = int(normDmg)
            self.dmgMsg += ""
            dmgPunc = "."
        self.enemyHP -= randDmg
        self.attackMsg = self.dmgMsg+self.name+" attacked "+self.enemyName+", doing "\
                         +str(randDmg)+" damage"+dmgPunc
        self.luckyEffect = 0
        maxCrit = self.baseCrit
        self.MainBattle()

    def LuckyStrike(self):
        self.damage = round(self.WA * self.strength / 2,0)
        self.damageLow = round(self.damage * 0.8,0)
        self.damageHigh = round(self.damage * 1.2,0)
        sacrifice = random.randrange(round(self.maxHP/50,0),\
                                          round(self.maxHP/10,0)+1)
        self.HP -= sacrifice
        print "\n|"+self.name,"performed a lucky strike, sacrificing",sacrifice,"health.\
\n|"+self.name+"'s odds of scoring a critical strike are greatly improved."
        critDmg = int(round(self.damage*2,0))
        self.luckyEffect = 1
        self.dmgMsg = ""
        self.Attack()
    
    def EnemyAttack(self):
        if len(self.enemyStats) == 10:
            enemyAtkRange = 12
        elif len(self.enemyStats) == 12:
            enemyAtkRange = 13
        elif len(self.enemyStats) == 14:
            enemyAtkRange = 14
        enemyAttack = random.randrange(5,enemyAtkRange)
        #
        if enemyAttack == 11:
            enemyCry = self.enemyStats[-2]
            enemyAtkChoice = 7

        elif enemyAttack == 12:
            enemyCry = self.enemyStats[-3]
            enemyAtkChoice = 8

        elif enemyAttack == 13:
            enemyCry = self.enemyStats[-4]
            enemyAtkChoice = 9
            
        else:
            enemyCry = "attacks you"
            enemyAtkChoice = 6
        #  
        enemyDmgRand = self.enemyStats[enemyAtkChoice]
        enemyDmgLow = round(enemyDmgRand*0.8,0)
        enemyDmgHigh = round(enemyDmgRand*1.2,0)
        if enemyDmgLow == enemyDmgHigh:
            self.enemyDamage = enemyDmgLow
        else:
            self.enemyDamage = random.randrange(enemyDmgLow,enemyDmgHigh+1)
        self.enemyDamage = int(round(self.enemyDamage,0))
        self.HP -= self.enemyDamage

        self.enemyMsg = self.enemyName.replace("the","The")+" "+enemyCry+", doing "\
                        +str(self.enemyDamage)+" damage."
    
    #level, name, hp, exp, euros, damage, special damage, description
    def Blue_Snail(self):
        self.enemyStats = [1, "the Blue Snail", 8, 1, 0,\
                "bluesnail.gif",1, 2, "makes you slip on its goo", 0]
    
    def Rumadan_Man(self):
        self.enemyStats = [2, "the Rumadan Man", 15, 1, 1,\
                "rumadanman.gif",1, 3, "flings cow dung at you", 0]

    def Rumadan_Warrior(self):
        self.enemyStats = [2, "the Rumadan Warrior", 15, 4, 1,\
                "rumadanwarrior.gif",3, 5, "thrusts his sword at you", "Sword"]
    
    def Goblin(self):
        self.enemyStats = [2, "the Goblin", 20, 3, 3,\
                "goblin.gif",2, 4, "swings its little rusty knife wildly at you", "Rusty Knife"]
        
    def Sean_Anderson(self):
        self.enemyStats = [2, "Sean Anderson", 80, 0, 10,\
                "sean.gif",1, 0, 2,0,"sits down","gives you a purple nurple", "squirts ketchup on you", "Ketchup Packet"]
    
    def Green_Goblin(self):
        self.enemyStats = [3, "the Green Goblin", 40, 6, 6,\
                "greengoblin.gif",4, 8, "crushes you with its bone", "Bone"]

    def Mutated_Tree(self):
        self.enemyStats = [3, "the Mutated tree", 50, 8, 0,\
                "mtree.gif",3, 10, "stabs you with its evil root", "Root of all Evil"]

    def Squig(self):
        self.enemyStats = [5, "the Squig", 150, 20, 10,\
                "squig.gif",10,12,"chomps you savagely",0]
        
    def Fire_Goblin(self):
        self.enemyStats = [6, "the Fire Goblin", 80, 12, 12,\
                "firegoblin.gif",8,16,24,"casts eruption","blasts you with its fireball","Flametongue"]
        
    def Satanic_Bear(self):
        self.enemyStats = [6, "the Satanic Bear", 300, 32, 20,\
                "satanicbear.gif",5,25,20,"claws you savagely","clubs you with its deadly mace","Morning Star"]

    def Goblin_King(self):
        self.enemyStats = [7, "the Goblin King", 300, 1, 150,\
                "goblinking.gif",10,1,"laughs demonically at you",0]

    def Kraken(self):
        self.enemyStats = [7, "the Kraken", 500, 40, 0,\
                "kraken.gif",7,18,"batters you with its tentacles",0]

    def Wildy_PKer(self):
        self.enemyStats = [8, "WiLdY_PKer_272", 999, 60, 20,\
                "rs.gif",10,0,20,"says: \"I p00n all n00bz with ma R2H\"","eats a lobby","Rapier"]

    def Lesser_Demon(self):
        self.enemyStats = [8, "the Lesser Demon", 1100, 80, 20,\
                "rs2.gif",7,50,"rakes you with its claws","Flametongue"]

    def Tomas_Tam(self):
        self.enemyStats = [10, "Tomas Tam, Remover of Souls", 8000, 250, 500,\
                "tomastam.gif",15,30,99,40,"crushes you with his psychic power","casts N. blast","slashes you with his N. blade",0]
        
    def Zain(self):
        self.enemyStats = [16, "Zain", 500, 8, 50,\
                "zain.gif",3,30,15,"sneaks behind you and stabs you with his bony finger","says \"KOBE!\" and hurls you into the air", "Bone"]
    
    def Astrobus(self):
        self.enemyStats = [69, "Astrobus", 600, 200, 0,\
                "astrobus.gif",5, 1337, "runs you over", 0]
        
    def Start(self):
        length = len(self.enemyList)
        enemyChooser = random.randrange(0,length)
        enemyMethod = "self."+self.enemyList[enemyChooser]+"()"
        exec enemyMethod
        self.enemyLvl = self.enemyStats[0]
        if self.trialCounter < 4:
            if self.level - 1 > self.enemyLvl or self.enemyLvl > self.level + 1:
                self.trialCounter += 1
                self.Start()
            else:
                self.trialCounter = 0
                self.Encounter()
        else:
            self.trialCounter = 0
            self.Encounter()

    def Encounter(self):
        self.trialCounter = 0
        self.enemyName = self.enemyStats[1]
        self.enemyHP = self.enemyStats[2]
        self.enemyExp = self.enemyStats[3]
        enemyEurosLow = int(round(self.enemyStats[4]*0.8,0))
        enemyEurosHigh = int(round(self.enemyStats[4]*1.2,0))
        self.enemyImage = self.enemyStats[5]
        if enemyEurosLow == enemyEurosHigh:
            self.enemyEurosRand = enemyEurosLow
        else:
            self.enemyEurosRand = int(round(random.randrange(enemyEurosLow,\
            enemyEurosHigh)+1,0))
        print "\nYou've encountered:",self.enemyName.replace("the ","")\
        +", level",str(self.enemyLvl)+"."
        self.MainWindow()

    def MainWindow(self):
        self.autoKillChance = 0
        if self.turn < 2:
            self.MainBattle()
        else:
            pass
        if self.firstRound == 1:
            self.masterBattle = Tk()
            self.v = StringVar()
            swordThumb = PhotoImage(file="swordthumb.gif")
            axeThumb = PhotoImage(file="axethumb.gif")
            dragonThumb = PhotoImage(file="dragonthumb.gif")
            bootsThumb = PhotoImage(file="bootsthumb.gif")
            shieldThumb = PhotoImage(file="shieldthumb.gif")
            enemyPic = PhotoImage(file=self.enemyImage)
            self.masterBattle.title("Battle-Battle!")
            fB = Frame(self.masterBattle).grid()
            
            l1B = Label(fB, fg="blue", text="Battle with "+self.enemyName,\
            ).grid(row=1, column=0, columnspan=3)
            
            b1B = Button(fB, bg="blue", image=swordThumb, command=self.NormalAttack)
            b1B.grid(row=3, column=0,padx=5)
            b2B = Button(fB, bg="yellow",image=axeThumb, command=self.LuckyStrike)
            b2B.grid(row=5, column=0,padx=5)
            l2B = Label(fB, image=enemyPic, relief="sunken")
            l2B.grid(row=2, rowspan=5, column=1)

            if len(self.abilities) >= 1:
                self.r1B = Radiobutton(fB, text=self.abilities[0],variable=self.v,value=0)
                self.r1B.grid(row=8,column=1,sticky=W)
            if len(self.abilities) >= 2:
                self.r2B = Radiobutton(fB, text=self.abilities[1],variable=self.v,value=1)
                self.r2B.grid(row=9,column=1,sticky=W)
            if len(self.abilities) >= 3:
                self.r3B = Radiobutton(fB, text=self.abilities[2],variable=self.v,value=2)
                self.r3B.grid(row=10,column=1,sticky=W)
            if len(self.abilities) >= 4:
                self.r4B = Radiobutton(fB, text=self.abilities[3],variable=self.v,value=3)
                self.r4B.grid(row=11,column=1,sticky=W)
                                  
            b3B = Button(fB, bg="orange",image=dragonThumb, command=self.AbilAttack)
            b3B.grid(row=7, column=1,sticky=N,pady=5)
            b4B = Button(fB, bg="black",image=bootsThumb, command=self.Flee)
            b4B.grid(row=5, column=2,padx=5)
            b5B = Button(fB, bg="brown",image=shieldThumb, command=self.Defend)
            b5B.grid(row=3, column=2,padx=5)
            self.helpWindow = "battle"
            bHelp = Button(fB, bitmap="question", bg="white", command=self.Helper)
            bHelp.grid(row=1, column=2, sticky=NE)
            
            self.firstRound = 0
            self.masterBattle.mainloop()
        else:
            pass
            
    def EnemyTurn(self):    #if enemy attacks it goes here too
        print self.enemyMsg
        if self.weaponAttribute == "fast":
            self.turn += 4
        elif self.weaponAttribute == "slow":
            self.turn += 1
        else:
            self.turn += 2

    def Defend(self):   #skips user turn
        self.attackMsg = self.name+" did nothing for the turn."
        self.MainBattle()

    def Flee(self): #if user clicks boots
        if self.enemyName == "Tomas Tam, Remover of Souls":
            self.attackMsg = "Tomas Tam: \"You cannot escape from Tomas Tam!\""
            self.MainBattle()
        else:
            print "\n"+self.name+" attempted to flee the fight..."
            fleeChance = random.randrange(1,5)
            if fleeChance != 4:
                eurosLostMin = self.euros/10
                eurosLostMax = self.euros/5
                if eurosLostMin == eurosLostMax:
                    eurosLost = eurosLostMin
                else:
                    eurosLost = random.randrange(eurosLostMin,eurosLostMax)
                self.euros -= eurosLost
                time.sleep(2)
                print self.name+" has fled successfully, but lost "+str(eurosLost)+" euros on the way out!"
                self.masterBattle.destroy()
                if self.hb == 1:
                    self.hb = 0
                    self.maxHP = self.maxHPtemp
                    self.maxNRG = self.maxNRGtemp
                    if self.HP > self.maxHP: self.HP = self.maxHP
                    else: pass
                    if self.NRG > self.maxNRG: self.NRG = self.maxNRG
                    else: pass
                else:
                    pass
                time.sleep(1.5)
                self.goBack()
            else:
                time.sleep(2)
                self.attackMsg = self.name+" did not manage to flee from battle!"
                self.MainBattle()
    
    def MainBattle(self):   #displays msgs in console and decides if it's enemy's turn to attack
        if self.autoKillChance == 100:
            self.PrintBars()
            print self.attackMsg
            print self.enemyName.replace("the ","The ")+" D/Cs itself from "+self.name+"'s singing."
            self.EnemyDeath()
        else:
            self.NRG += int(round(self.maxNRG/50,0))
            if self.NRG > self.maxNRG:
                self.NRG = self.maxNRG
            else:
                pass
            if self.enemyHP > 0 and self.turn < 3:
                self.EnemyAttack()
            else:
                pass
            self.PrintBars()
            if self.turn > 1:
                print self.attackMsg
                self.turn -= 2
                if self.enemyHP > 0 and self.turn < 2:
                    self.EnemyTurn()
                else:
                    pass
            elif self.enemyHP > 0:
                self.EnemyTurn()
            #when battle is over
            if self.HP <= 0:
                self.masterBattle.destroy()
                try:
                    import winsound
                    winsound.Beep(int(329.627556913),800)
                    winsound.Beep(int(311.126983722),800)
                    winsound.Beep(int(294),800)
                except ImportError:
                    pass
                print "You have been killed by",self.enemyName+"."
                time.sleep(3)
                print "Toshe's Quest ends here."
                time.sleep(10)
                sys.exit()
            elif self.enemyHP <= 0:
                self.EnemyDeath()
            elif self.turn > 1:
                self.MainWindow()
            else:
                self.MainWindow()

    def PrintBars(self):    #displays image of HP, NRG, and EnemyHP
        self.HPBar()
        self.NRGBar()
        print "\nHP: "+str(self.HP)+"/"+str(self.maxHP)+"\t\t\t"+\
              self.enemyName.replace("the ",""),"HP: "+str(self.enemyHP)+\
              "/"+str(self.enemyStats[2])
        print self.HPbarpic
        print "NRG: "+str(self.NRG)+"/"+str(self.maxNRG)
        print self.NRGbarpic

    def EnemyDeath(self):   #when enemies dies it goes to this
        self.masterBattle.destroy()
        try:
            import winsound
            winsound.Beep(int(1046.5022612),150)
            winsound.Beep(int(1567.98174392),150)
        except ImportError:
            pass
        if self.enemyName != "Tomas Tam, Remover of Souls" or self.enemyName != "Zain":
            print "You have slain",self.enemyName+"."
        else: print self.enemyName+" has fainted."
        self.exp += self.enemyExp
        self.euros += self.enemyEurosRand

        print self.name,"gained",self.enemyExp,"experience and",\
            self.enemyEurosRand,"euros."
        self.LevelUp()
        if self.enemyStats[-1] != 0:
            weaponRoll = random.randrange(1,11)
            if weaponRoll == 1:
                print self.enemyName.replace("the ","The ")+" dropped a "+str(self.enemyStats[-1]).lower()+"."
                self.newWeapon = self.buyWeapon = self.enemyStats[-1]
                self.BuyWeaponLookUp()
                self.New_Weapon()
            else:
                self.etcCheck()
                self.goBack()
        else:
            self.etcCheck()
            self.goBack()

    def etcCheck(self): #checks for quests and etc
        if self.hb == 1:
            self.hb = 0
            self.maxHP = self.maxHPtemp
            self.maxNRG = self.maxNRGtemp
        else:
            pass
        if self.q1 == 1 and self.enemyName == "the Rumadan Man":
            self.killCount += 1
            if self.killCount == 2:
                self.q1 = 2
            else:
                pass
        else:
            pass
        if self.killZain == 1 and self.enemyName == "Zain":
            self.zainKilled = 1
        else:
            pass
        if self.enemyName == "Tomas Tam, Remover of Souls":
            self.goBack = self.EndGame
        else:
            pass
        time.sleep(1.5)

    def EndGame(self):  #goes here when tomas is killed
        raw_input("\nTomas Tam: \"Ouuuooouuh...\" [Enter]")
        raw_input(self.name+": ... [Enter]")
        raw_input("Seamen: \"IT'S GONNA BLOW!\" [Enter]")
        raw_input("\n"+self.name+""" nimbly jumps over the debris left by the fight
and hops into a lifeboat. [Enter]""")
        print "\nTomas Tam: \"Ugh.\""
        time.sleep(1.5)
        print "\nK",
        time.sleep(0.2)
        print "A",
        time.sleep(0.2)
        print "-",
        time.sleep(0.2)
        print "B",
        time.sleep(0.2)
        print "O",
        time.sleep(0.2)
        print "O",
        time.sleep(0.2)
        print "M!",
        time.sleep(2)
        print "The ship explodes from the intensity of your fight with Tomas."
        time.sleep(2)
        raw_input("\n"+self.name+": Macedonia is safe for now. (End)")
        print "You have killed Tomas Tam, but the Key to Macedonia is forever lost."
        time.sleep(5)
        print "However, you can go underwater to find the key in Toshe's Underwater Adventures."
        time.sleep(5)
        print "Buy it now for only $49.99 plus shipping and handling."
        time.sleep(5)
        
        print "THANKS FOR PLAYING! YOU HAVE FINISHED TOSHE'S QUEST!"
        time.sleep(10)
        sys.exit()
        
#main

instance = Game()
instance.Beginning()
instance.Crossroads()

#-------------------------------------------------------------------------------
