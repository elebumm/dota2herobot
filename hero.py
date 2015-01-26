#import praw (for the reddit api of course), time (for timer between loops), re (for the regular expression on hero names), and sqlite3 to store in your database!
import praw
import time
import re
import sqlite3

#username for reddit. This will not make an account so go on reddit and make another account and put username and password here.
username = "LewisTheRobot"
password = "lewismenelaws"

subreddit = "dota2"
#credentials of your sqlite database. Download sqlite3 viewer to make one easily.
conn = sqlite3.connect('')
c = conn.cursor()
#user_agent tells the reddit servers what your bot does.
r = praw.Reddit(user_agent = "Count amount of times heroes are mentioned")

#lists all dota heroes in game
words_to_match = [r'\bAbaddon\b', r'\bAlchemist\b', r'\bAncient Apparition\b', r'\bAnti Mage\b', r'\bAxe\b', r'\bBane\b', r'\bBatrider\b', r'\bBeastmaster\b', r'\bBloodseeker\b', r'\bBounty Hunter\b', r'\rBrewmaster\b', r'\bBristleback\b', r'\bBroodmother\b', r'\bCentaur Warrunner\b', r'\bChaos Knight\b', r'\bChen\b', r'\bClinkz\b', r'\bClockwerk\b', r'\bCrystal Maiden\b', r'\bDark Seer\b', r'\bDazzle\b', r'\bDeath Prophet\b', r'\bDisruptor\b', r'\bDoom\b', r'\bDragon Knight\b', r'\bDrow Ranger\b', r'\bEarthshaker\b', r'\bEarth Spirt\b', r'\bElder Titan\b', r'\bEmber Spirit\b', r'\bEnchantress\b', r'\bEnigma\b', r'\bFaceless Void\b', r'\bGyrocopter\b', r'\bHuskar\b', r'\bInvoker\b', r'\bIo\b', r'\bJakiro\b', r'\bJuggernaut\b', r'\bKeeper of the Light\b', r'\bKunkka\b', r'\bLegion Commander\b', r'\bLeshrac\b', r'\bLich\b', r'\bLifestealer\b', r'\bLina\b', r'\bLion\b', r'\bLone Druid\b', r'\bLuna\b', r'\bLycan\b', r'\bMagnus\b', r'\bMedusa\b', r'\bMeepo\b', r'\bMirana\b', r'\bMorphling\b', r'\bNaga Siren\b', r'\bNatures Prophet\b', r'\bNecrophos\b', r'\bNight Stalker\b', r'\bNyx Assassin\b', r'\bOgre Magi\b', r'\bOmniKnight\b', r'\bOracle\b', r'\bOutworld Devourer\b', r'\bPhantom Assassin\b', r'\bPhantom Lancer\b', r'\bPheonix\b', r'\bPuck\b', r'\bPudge\b', r'\bPugna\b', r'\bQueen of Pain\b', r'\bRazor\b', r'\bRiki\b', r'\bRubick\b', r'\bSand King\b', '\bShadow Demon\b', r'\bShadow Fiend\b', r'\bShadow Shaman\b', r'\bSilencer\b', r'\bSkywrath Mage\b', r'\bSlardar\b', r'\bSlark\b', r'\bSniper\b', r'\bSpectre\b', r'\bSpirit Breaker\b', r'\bStorm Spirit\b', r'\bSven\b', r'\bTechies\b', r'\bTemplar Assassin\b', r'\bTerrorblade\b', r'\bTidehunter\b', r'\bTimbersaw\b', r'\bTinker\b', r'\bTiny\b', r'\bTreant Protector\b', r'\bTroll Warlord\b', r'\bTusk\b', r'\bUndying\b', r'\bUrsa\b', r'\bVengeful Spirit\b', r'\bVenomancer\b', r'\bViper\b', r'\bVisage\b', r'\bWarlock\b', r'\bWeaver\b', r'\bWindranger\b', r'\bWitch Doctor\b', r'\bWraith King\b', r'\bZeus\b']


#Empty list to store all comments in so that the prompt can show you how many have been counted

storage = []