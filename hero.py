#import praw (for the reddit api of course), time (for timer between loops), re (for the regular expression on hero names), and sqlite3 to store in your database!
import praw
import time
import re
import sqlite3

#username for reddit. This will not make an account so go on reddit and make another account and put username and password here.
username = "LewisTheRobot"
password = "lewismenelaws"


#Enter what subreddit you want to choose
subreddit_choice = "dota2"
#credentials of your sqlite database. Download sqlite3 viewer to make one easily.
conn = sqlite3.connect('dotaheroes')
c = conn.cursor()
#user_agent tells the reddit servers what your bot does.
r = praw.Reddit(user_agent = "Count amount of times heroes are mentioned")

#lists all dota heroes in game
words_to_match = [r'\babaddon\b', r'\balchemist\b', r'\bancient apparition\b', r'\banti mage\b', r'\baxe\b', r'\bbane\b', r'\bbatrider\b', r'\bbeastmaster\b', r'\bbloodseeker\b', r'\bbounty hunter\b', r'\rbrewmaster\b', r'\bbristleback\b', r'\bbroodmother\b', r'\bcentaur warrunner\b', r'\bchaos knight\b', r'\bchen\b', r'\bclinkz\b', r'\bclockwerk\b', r'\bcrystal maiden\b', r'\bdark seer\b', r'\bdazzle\b', r'\bdeath prophet\b', r'\bdisruptor\b', r'\bdoom\b', r'\bdragon knight\b', r'\bdrow ranger\b', r'\bearthshaker\b', r'\bearth spirt\b', r'\belder titan\b', r'\bember spirit\b', r'\benchantress\b', r'\benigma\b', r'\bfaceless void\b', r'\bgyrocopter\b', r'\bhuskar\b', r'\binvoker\b', r'\bio\b', r'\bjakiro\b', r'\bjuggernaut\b', r'\bkeeper of the light\b', r'\bkunkka\b', r'\blegion commander\b', r'\bleshrac\b', r'\blich\b', r'\blifestealer\b', r'\blina\b', r'\blion\b', r'\blone druid\b', r'\bluna\b', r'\blycan\b', r'\bmagnus\b', r'\bmedusa\b', r'\bmeepo\b', r'\bmirana\b', r'\bmorphling\b', r'\bnaga siren\b', r'\bnatures prophet\b', r'\bnecrophos\b', r'\bnight stalker\b', r'\bnyx assassin\b', r'\bogre magi\b', r'\bomniknight\b', r'\boracle\b', r'\boutworld devourer\b', r'\bphantom assassin\b', r'\bphantom lancer\b', r'\bpheonix\b', r'\bpuck\b', r'\bpudge\b', r'\bpugna\b', r'\bqueen of pain\b', r'\brazor\b', r'\briki\b', r'\brubick\b', r'\bsand king\b', '\bshadow demon\b', r'\bshadow fiend\b', r'\bshadow shaman\b', r'\bsilencer\b', r'\bskywrath mage\b', r'\bslardar\b', r'\bslark\b', r'\bsniper\b', r'\bspectre\b', r'\bspirit breaker\b', r'\bstorm spirit\b', r'\bsven\b', r'\btechies\b', r'\btemplar assassin\b', r'\bterrorblade\b', r'\btidehunter\b', r'\btimbersaw\b', r'\btinker\b', r'\btiny\b', r'\btreant protector\b', r'\btroll warlord\b', r'\btusk\b', r'\bundying\b', r'\bursa\b', r'\bvengeful spirit\b', r'\bvenomancer\b', r'\bviper\b', r'\bvisage\b', r'\bwarlock\b', r'\bweaver\b', r'\bwindranger\b', r'\bwitch doctor\b', r'\bwraith king\b', r'\bzeus\b']


#Empty list to store all comments in so that the prompt can show you how many have been counted

storage = []

r.login(username, password)

def run_bot():
	subreddit = r.get_subreddit(subreddit_choice)
	print("Grabbing subreddit")
	comments = subreddit.get_comments(limit=200)
	print("Grabbing comments")
	for comment in comments:
		comment_text = comment.body.lower()
		isMatch = any(re.search(string, comment_text) for string in words_to_match)
		if comment.id not in storage and isMatch and comment.author not in storage:
			print("A hero was mentioned! Adding to database :)")
			storage.append(comment.author)
			c.execute("INSERT INTO heroes (id, hero_name) VALUES(?, ?)", (str(comment.id), str(isMatch)))
			conn.commit()

	print("There are currently " + str(len(storage)) + " people who have said a hero name.")



while True:
	run_bot()
	time.sleep(2)




