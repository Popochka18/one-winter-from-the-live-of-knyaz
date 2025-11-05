## NPCs - Character Definitions and Sprites
## This file contains all non-player characters, their definitions, and sprite compositions

################################################################################
## Character Definitions
################################################################################

# Main NPCs
define priest = Character("Father Yevgraf", who_color="#d0c0a0")
define captain = Character("Captain Borislav", who_color="#b0b0b0")
define guard = Character("Guard", who_color="#909090")
define governor = Character("Governor Konstantin Orlov", who_color="#8b0000")
define janek = Character("Knyaz Janek", who_color="#a0b0c0", what_italic=True)
define cook = Character("Agnia", who_color="#d2b48c")
define brother = Character("Mstislav", who_color="#aaddff")
define sister = Character("Lyudmila", who_color="#ffccdd")

# Additional NPCs
define merchant = Character("Merchant Boris", who_color="#c9a76f")
define advisor = Character("Chancellor Dimitri", who_color="#7b68ee")
define servant = Character("Servant", who_color="#a8a8a8")
define peasant = Character("Peasant", who_color="#8b7355")
define noble = Character("Boyar", who_color="#daa520")
define spy = Character("Informant", who_color="#696969")
define healer = Character("Healer Oksana", who_color="#90ee90")
define blacksmith = Character("Ivan the Smith", who_color="#cd853f")
define hunter = Character("Pyotr the Hunter", who_color="#8b4513")
define beggar = Character("Beggar", who_color="#778899")
define prisoner = Character("Prisoner", who_color="#4a4a4a")
define messenger = Character("Messenger", who_color="#b0c4de")
define librarian = Character("Father Leonid", who_color="#dda0dd")
define stable_master = Character("Grigory", who_color="#bc8f8f")
define master_at_arms = Character("Sergeant Vasily", who_color="#708090")

# Foreign NPCs
define tealean_envoy = Character("Tealean Envoy", who_color="#4169e1")
define northern_trader = Character("Northern Trader", who_color="#6495ed")
define southern_diplomat = Character("Southern Diplomat", who_color="#ff6347")
define rival_knyaz = Character("Rival Knyaz", who_color="#dc143c")

# Family NPCs (conditional based on player choices)
define mother = Character("Mother Superior", who_color="#dda0dd")
define uncle = Character("Uncle Vladislav", who_color="#9370db")
define cousin = Character("Cousin Anatoly", who_color="#87ceeb")

# Supernatural/Special NPCs
define old_woman = Character("Old Crone", who_color="#9932cc")
define mystic = Character("Wandering Mystic", who_color="#ba55d3")
define ghost = Character("Ghostly Apparition", who_color="#e6e6fa", what_italic=True)

################################################################################
## NPC Sprite Definitions
################################################################################

# Priest Sprite - Father Yevgraf
image priest_sprite:
    "images/npcs/priest/body.png"
    "images/npcs/priest/robes.png"
    "images/npcs/priest/head.png"
    "images/npcs/priest/eyes.png"
    "images/npcs/priest/beard.png"

# Captain Sprite - Captain Borislav
image captain_sprite:
    "images/npcs/captain/body.png"
    "images/npcs/captain/armor.png"
    "images/npcs/captain/head.png"
    "images/npcs/captain/eyes.png"
    "images/npcs/captain/scar.png"

# Governor Sprite - Governor Konstantin Orlov
image governor_sprite:
    "images/npcs/governor/body.png"
    "images/npcs/governor/robe.png"
    "images/npcs/governor/head.png"
    "images/npcs/governor/eyes.png"
    "images/npcs/governor/beard.png"
    "images/npcs/governor/medal.png"

# Cook Sprite - Agnia
image cook_sprite:
    "images/npcs/cook/body.png"
    "images/npcs/cook/dress.png"
    "images/npcs/cook/head.png"
    "images/npcs/cook/eyes.png"
    "images/npcs/cook/hair.png"
    "images/npcs/cook/apron.png"

# Brother Sprite - Mstislav
layeredimage brother_sprite:
    always:
        "images/npcs/brother/body.png"
    always:
        "images/npcs/brother/noble_clothes.png"
    always:
        "images/npcs/brother/head.png"
    always:
        "images/npcs/brother/eyes.png"
    always:
        "images/npcs/brother/hair.png"

# Sister Sprite - Lyudmila
layeredimage sister_sprite:
    always:
        "images/npcs/sister/body.png"
    always:
        "images/npcs/sister/dress.png"
    always:
        "images/npcs/sister/head.png"
    always:
        "images/npcs/sister/eyes.png"
    always:
        "images/npcs/sister/hair.png"
    always:
        "images/npcs/sister/jewelry.png"

# Advisor Sprite - Chancellor Dimitri
image advisor_sprite:
    "images/npcs/advisor/body.png"
    "images/npcs/advisor/robes.png"
    "images/npcs/advisor/head.png"
    "images/npcs/advisor/eyes.png"
    "images/npcs/advisor/beard.png"
    "images/npcs/advisor/scroll.png"

# Merchant Sprite - Merchant Boris
image merchant_sprite:
    "images/npcs/merchant/body.png"
    "images/npcs/merchant/clothes.png"
    "images/npcs/merchant/head.png"
    "images/npcs/merchant/eyes.png"
    "images/npcs/merchant/hat.png"
    "images/npcs/merchant/coin_purse.png"

# Healer Sprite - Healer Oksana
image healer_sprite:
    "images/npcs/healer/body.png"
    "images/npcs/healer/robe.png"
    "images/npcs/healer/head.png"
    "images/npcs/healer/eyes.png"
    "images/npcs/healer/hair.png"
    "images/npcs/healer/herbs.png"

# Blacksmith Sprite - Ivan the Smith
image blacksmith_sprite:
    "images/npcs/blacksmith/body.png"
    "images/npcs/blacksmith/apron.png"
    "images/npcs/blacksmith/head.png"
    "images/npcs/blacksmith/eyes.png"
    "images/npcs/blacksmith/beard.png"
    "images/npcs/blacksmith/hammer.png"

# Hunter Sprite - Pyotr the Hunter
image hunter_sprite:
    "images/npcs/hunter/body.png"
    "images/npcs/hunter/furs.png"
    "images/npcs/hunter/head.png"
    "images/npcs/hunter/eyes.png"
    "images/npcs/hunter/beard.png"
    "images/npcs/hunter/bow.png"

# Master at Arms Sprite - Sergeant Vasily
image master_at_arms_sprite:
    "images/npcs/master_at_arms/body.png"
    "images/npcs/master_at_arms/armor.png"
    "images/npcs/master_at_arms/head.png"
    "images/npcs/master_at_arms/eyes.png"
    "images/npcs/master_at_arms/scar.png"
    "images/npcs/master_at_arms/sword.png"

# Old Crone Sprite
image old_woman_sprite:
    "images/npcs/old_woman/body.png"
    "images/npcs/old_woman/rags.png"
    "images/npcs/old_woman/head.png"
    "images/npcs/old_woman/eyes.png"
    "images/npcs/old_woman/hair.png"
    "images/npcs/old_woman/staff.png"

# Mystic Sprite
image mystic_sprite:
    "images/npcs/mystic/body.png"
    "images/npcs/mystic/robes.png"
    "images/npcs/mystic/head.png"
    "images/npcs/mystic/eyes.png"
    "images/npcs/mystic/beard.png"
    "images/npcs/mystic/amulet.png"

# --- Placeholder Single-Image Sprites (for NPCs without layered images) ---
image guard_sprite = "images/npcs/guard.png"
image janek_deathbed = "images/npcs/janek_deathbed.png"
image servant_sprite = "images/npcs/servant.png"
image peasant_sprite = "images/npcs/peasant.png"
image noble_sprite = "images/npcs/noble.png"
image beggar_sprite = "images/npcs/beggar.png"
image prisoner_sprite = "images/npcs/prisoner.png"
image messenger_sprite = "images/npcs/messenger.png"
image stable_master_sprite = "images/npcs/stable_master.png"
image spy_sprite = "images/npcs/spy.png"
image librarian_sprite = "images/npcs/librarian.png"

# Foreign NPCs
image tealean_envoy_sprite = "images/npcs/foreign/tealean_envoy.png"
image northern_trader_sprite = "images/npcs/foreign/northern_trader.png"
image southern_diplomat_sprite = "images/npcs/foreign/southern_diplomat.png"
image rival_knyaz_sprite = "images/npcs/foreign/rival_knyaz.png"

# Ghost (transparent/special effect)
image ghost_sprite:
    "images/npcs/ghost/apparition.png"
    alpha 0.6

################################################################################
## NPC Relationship Variables
################################################################################

default priest_relationship = 0
default captain_relationship = 0
default governor_relationship = 0
default cook_relationship = 0
default brother_relationship = 0
default sister_relationship = 0
default advisor_relationship = 0
default merchant_relationship = 0
default healer_relationship = 0
default blacksmith_relationship = 0

# Trust levels
default priest_trust = 50
default captain_trust = 50
default governor_trust = 0
default advisor_trust = 50

# Special NPC states
default priest_met = False
default captain_met = False
default governor_met = False
default cook_met = False
default brother_met = False
default sister_met = False
default advisor_met = False
default merchant_met = False

# Quest-related NPC flags
default merchant_trade_available = False
default healer_available = False
default blacksmith_can_craft = False
default hunter_quest_active = False
default mystic_encountered = False
default ghost_seen = False

################################################################################
## NPC Dialogue Helpers
################################################################################

init python:
    def get_priest_greeting():
        """Returns appropriate greeting based on relationship"""
        if priest_relationship >= 20:
            return "Blessings upon you, my child. The gods smile on your deeds."
        elif priest_relationship >= 0:
            return "May the gods watch over you, [persistent.player_title]."
        else:
            return "The gods are... displeased with recent events."
    
    def get_captain_greeting():
        """Returns appropriate greeting based on relationship"""
        if captain_relationship >= 20:
            return "My [persistent.player_title]! It's good to see you. The men speak highly of your leadership."
        elif captain_relationship >= 0:
            return "My [persistent.player_title]."
        else:
            return "My [persistent.player_title]... we need to talk about the state of our forces."
    
    def get_governor_greeting():
        """Returns appropriate greeting based on relationship"""
        if governor_relationship >= 10:
            return "Ah, [persistent.player_title]. The Empire is pleased with your... cooperation."
        elif governor_relationship >= -10:
            return "[persistent.player_title]. I trust your tribute will be forthcoming."
        else:
            return "[persistent.player_title]. The Empire grows impatient."
    
    def get_cook_greeting():
        """Returns appropriate greeting based on relationship"""
        if cook_relationship >= 20:
            return "Oh, my dear [persistent.player_title]! I've made your favorite!"
        elif cook_relationship >= 0:
            return "Good day, [persistent.player_title]. What can I prepare for you?"
        else:
            return "Yes, [persistent.player_title]?"
    
    def change_npc_relationship(npc_name, amount):
        """Change relationship with an NPC"""
        if npc_name == "priest":
            store.priest_relationship += amount
        elif npc_name == "captain":
            store.captain_relationship += amount
        elif npc_name == "governor":
            store.governor_relationship += amount
        elif npc_name == "cook":
            store.cook_relationship += amount
        elif npc_name == "brother":
            store.brother_relationship += amount
        elif npc_name == "sister":
            store.sister_relationship += amount
        elif npc_name == "advisor":
            store.advisor_relationship += amount
        elif npc_name == "merchant":
            store.merchant_relationship += amount
        
        # Notify player of major relationship changes
        if amount >= 10:
            renpy.notify(npc_name.capitalize() + " is pleased with you.")
        elif amount <= -10:
            renpy.notify(npc_name.capitalize() + " is displeased with you.")

################################################################################
## NPC Background Information
################################################################################

init python:
    npc_backgrounds = {
        "priest": {
            "name": "Father Yevgraf",
            "age": 58,
            "role": "Orthodox Priest",
            "background": "A devout man who has served the church for over three decades. He knew your father well and offers spiritual guidance, though he can be rigid in his beliefs.",
            "personality": "Pious, traditional, stern but caring",
            "goals": "Maintain the faith, guide the ruler, preserve traditions"
        },
        "captain": {
            "name": "Captain Borislav",
            "age": 45,
            "role": "Military Commander",
            "background": "A veteran soldier with scars from countless battles. Loyal to your family, he commands respect from the troops despite limited resources.",
            "personality": "Gruff, loyal, pragmatic, honorable",
            "goals": "Protect the realm, maintain military readiness, serve honorably"
        },
        "governor": {
            "name": "Governor Konstantin Orlov",
            "age": 52,
            "role": "Imperial Governor",
            "background": "A high-ranking official of the Sibarian Empire, appointed to oversee the western territories. He's politically cunning and serves the Tsar's interests above all.",
            "personality": "Calculating, diplomatic, threatening, ambitious",
            "goals": "Ensure tribute flows to the Empire, maintain control, advance his career"
        },
        "cook": {
            "name": "Agnia",
            "age": 42,
            "role": "Head Cook",
            "background": "She's been cooking for your family since before you were born. Warm and motherly, she knows all the palace gossip.",
            "personality": "Warm, gossipy, caring, knowledgeable",
            "goals": "Keep everyone fed, maintain kitchen standards, look after you"
        },
        "brother": {
            "name": "Mstislav",
            "age": 19,
            "role": "Your Brother",
            "background": "Your younger brother, ambitious and sometimes reckless. He chafes at not being the heir.",
            "personality": "Ambitious, energetic, sometimes jealous, loyal (mostly)",
            "goals": "Prove himself, gain recognition, possibly claim power"
        },
        "sister": {
            "name": "Lyudmila",
            "age": 17,
            "role": "Your Sister",
            "background": "Your sister, clever and observant. She sees more than she lets on and is skilled in courtly intrigue.",
            "personality": "Intelligent, observant, witty, supportive",
            "goals": "Protect family, make advantageous marriage, maintain influence"
        },
        "advisor": {
            "name": "Chancellor Dimitri",
            "age": 61,
            "role": "Chief Advisor",
            "background": "He served your father and grandfather before you. His wisdom is vast, but he may have his own agenda.",
            "personality": "Wise, scheming, experienced, enigmatic",
            "goals": "Guide the realm, maintain stability, preserve his position"
        },
        "merchant": {
            "name": "Merchant Boris",
            "age": 38,
            "role": "Traveling Merchant",
            "background": "A trader who brings goods from across Sibara. He has connections and information from distant lands.",
            "personality": "Gregarious, shrewd, opportunistic, well-informed",
            "goals": "Profit, gather information, establish trade routes"
        },
        "healer": {
            "name": "Healer Oksana",
            "age": 55,
            "role": "Court Healer",
            "background": "A skilled herbalist and healer who tends to the sick and wounded. She knows ancient remedies.",
            "personality": "Gentle, wise, mysterious, compassionate",
            "goals": "Heal the sick, preserve knowledge, protect life"
        },
        "blacksmith": {
            "name": "Ivan the Smith",
            "age": 48,
            "role": "Master Blacksmith",
            "background": "The palace blacksmith, known for crafting quality weapons and armor. Gruff but skilled.",
            "personality": "Gruff, proud, skilled, dependable",
            "goals": "Craft quality work, maintain forge, arm the soldiers"
        }
    }
    
    def get_npc_info(npc_name):
        """Returns background information about an NPC"""
        if npc_name in npc_backgrounds:
            return npc_backgrounds[npc_name]
        return None

################################################################################
## NPC Conversation Starters
################################################################################

label talk_to_priest:
    show priest_sprite at left
    priest "[get_priest_greeting()]"
    
    menu:
        "Ask for spiritual guidance":
            priest "The path ahead is treacherous, my child. Trust in the divine, and you shall find your way."
            $ change_npc_relationship("priest", 2)
            
        "Discuss church matters":
            priest "The church requires support, [persistent.player_title]. Faith does not sustain itself on prayers alone."
            
        "Ask about your father":
            priest "Your father was a good man, if troubled. He sought to do what was right, even when the path was unclear."
            $ change_npc_relationship("priest", 1)
        
        "Leave":
            priest "May the gods watch over you."
    
    hide priest_sprite
    return

label talk_to_captain:
    show captain_sprite at right
    captain "[get_captain_greeting()]"
    
    menu:
        "Discuss military readiness":
            captain "We're doing what we can with what we have. The men are loyal, but they need proper equipment."
            
        "Ask about threats":
            captain "The borders are always under pressure. Bandits, rival knyazhestvas, and who knows what else in winter."
            $ change_npc_relationship("captain", 1)
            
        "Inquire about training":
            captain "Training never stops. A soldier who doesn't train is a dead soldier."
        
        "Leave":
            captain "My [persistent.player_title]."
    
    hide captain_sprite
    return

label talk_to_cook:
    show cook_sprite at left
    cook "[get_cook_greeting()]"
    
    menu:
        "Ask about the kitchen":
            cook "Everything's running smoothly, my dear. Though we could use more supplies before the deep winter sets in."
            
        "Listen to gossip":
            cook "Oh, well... I shouldn't say, but I heard from the servants that..."
            cook "She leans in conspiratorially and shares the latest palace rumors."
            $ change_npc_relationship("cook", 2)
            
        "Request a special meal":
            cook "Of course! I'll prepare something special just for you!"
            $ change_npc_relationship("cook", 3)
        
        "Leave":
            cook "Come back anytime, dear!"
    
    hide cook_sprite
    return

label talk_to_governor:
    show governor_sprite at player_center
    governor "[get_governor_greeting()]"
    
    menu:
        "Discuss tribute arrangements":
            governor "The Empire expects 500 gold quarterly. I trust there will be no... delays."
            
        "Ask about the Empire":
            governor "The Tsar's reach extends across all of Sibara. It would be wise to remember that."
            
        "Question his authority":
            governor "His eyes narrow dangerously."
            governor "Are you questioning the Tsar's appointed representative, [persistent.player_title]?"
            $ change_npc_relationship("governor", -5)
        
        "Be respectful and leave":
            governor "Good. Remember your place."
            $ change_npc_relationship("governor", 1)
    
    hide governor_sprite
    return

################################################################################
## Random NPC Encounter System
################################################################################

init python:
    def random_npc_encounter():
        """Generates random NPC encounters in various rooms"""
        import random
        encounters = [
            "servant_cleaning",
            "guard_patrol",
            "messenger_arrival",
            "merchant_visit",
            "beggar_plea",
            "peasant_petition",
            None,  # No encounter
            None,
            None
        ]
        return random.choice(encounters)

label npc_encounter_handler:
    $ encounter = random_npc_encounter()
    
    if encounter == "servant_cleaning":
        show servant_sprite at right
        servant "Oh! My [persistent.player_title], I didn't see you there. I was just tidying up."
        hide servant_sprite
        
    elif encounter == "guard_patrol":
        show guard_sprite at left
        guard "All quiet, my [persistent.player_title]."
        hide guard_sprite
        
    elif encounter == "messenger_arrival":
        show messenger_sprite at player_center
        messenger "My [persistent.player_title]! I bring word from the southern border."
        hide messenger_sprite
        
    elif encounter == "merchant_visit":
        show merchant_sprite at left
        merchant "Ah, [persistent.player_title]! Perhaps you'd be interested in some rare goods?"
        hide merchant_sprite
        
    elif encounter == "beggar_plea":
        show beggar_sprite at right
        beggar "Please, my lord/lady... just a few coins for food..."
        hide beggar_sprite
    
    return
