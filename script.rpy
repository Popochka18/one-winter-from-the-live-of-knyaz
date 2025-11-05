################################################################################
# ГОЙДА ГОЙДА ГОЙДА
# РУСЬ МАТУШКА - ЗЕМЛЯ РОДНАЯ
# НЕ ВИДАТЬ КОНЦА И КРАЯ
# НЕТ ТАКОГО ВРАГА С КЕМ БЫ НЕ СПРАВИЛАСЬ РОССИЯ
# ДАТАМАЙНЕРЫ ВЫПИСЫВАЮТСЯ ИЗ СЛОНОВ В ХОХЛЫ ЕСЛИ НЕ ЗАКРОЮТ ЭТОТ СКРИПТ
################################################################################
################################################################################
# One Winter from the Life of a Knyaz
# DATAMINERS SUCKS
################################################################################
init python:
    config.keymap['down'] = ['K_DOWN', 'repeat_K_DOWN']
    config.keymap['up'] = ['K_UP', 'repeat_K_UP']
    config.keymap['left'] = ['K_LEFT', 'repeat_K_LEFT']
    config.keymap['right'] = ['K_RIGHT', 'repeat_K_RIGHT']
#ИГРОВАЯ ЛОГИККА И КОСТЫЛИ
# 1. Game Definition and Configuration
#-------------------------------------------------------------------------------
define config.name = "One winter from the live of Knyaz"
define config.version = "0.1"
define config.save_directory = "one-winter-knyaz-12345"
define gui.show_name = True

# PLAYER CHARACTER POSITIONING TRANSFORMS - FIXED VERSION
# ============================================================================
# These transforms ensure consistent positioning of the player sprite
# across all scenes in the game

transform player_left:
    xalign 0.25
    yalign 1.0
    yanchor 1.0
    
transform player_center:
    xalign 0.5
    yalign 1.0
    yanchor 1.0
    
transform player_right:
    xalign 0.75
    yalign 1.0
    yanchor 1.0
    
transform player_far_left:
    xalign 0.1
    yalign 1.0
    yanchor 1.0
    
transform player_far_right:
    xalign 0.9
    yalign 1.0
    yanchor 1.0

# Transform for smooth character entrance
transform player_enter_left:
    xalign -0.2
    yalign 1.0
    yanchor 1.0
    ease 0.5 xalign 0.25

transform player_enter_right:
    xalign 1.2
    yalign 1.0
    yanchor 1.0
    ease 0.5 xalign 0.75

transform player_enter_center:
    xalign 0.5
    yalign 1.2
    yanchor 1.0
    ease 0.5 yalign 1.0

# Transform for character exit
transform player_exit_left:
    xalign 0.25
    yalign 1.0
    yanchor 1.0
    ease 0.5 xalign -0.2

transform player_exit_right:
    xalign 0.75
    yalign 1.0
    yanchor 1.0
    ease 0.5 xalign 1.2

# Transform with slight movement for talking animations
transform player_talking:
    yalign 1.0
    yanchor 1.0
    block:
        ease 0.1 yoffset -2
        ease 0.1 yoffset 0
        pause 0.3
        repeat

# Zoom transforms for emphasis
transform player_focus:
    zoom 1.1
    yalign 1.0
    
transform player_normal:
    zoom 1.0
    yalign 1.0

# 2. Character and Asset Definitions
#-------------------------------------------------------------------------------
# Define your main character. The 'image' tag links this character to the sprite.
define player = Character("[persistent.player_name]", who_color="#c8c8c8", image="player_sprite")

# Define a narrator for descriptive text, imbued with the doomer vibe.
define narrator = Character(None, what_color="#a0a0a0", what_italic=True)

# Define NPCs
define priest = Character("Father Yevgraf", who_color="#d0c0a0")
define captain = Character("Captain Borislav", who_color="#b0b0b0")
define guard = Character("Guard", who_color="#909090")
define janek = Character("Knyaz Janek", who_color="#a0b0c0", what_italic=True)
define cook = Character("Agnia", who_color="#d2b48c")
define brother = Character("Mstislav", who_color="#aaddff")
define sister = Character("Lyudmila", who_color="#ffccdd")


# --- Placeholder Images ---
# You will replace these with your actual assets.
# Backgrounds
image bg throne_room = "images/backgrounds/throne_room.jpg"
image bg palace_map = "images/backgrounds/palace_map.jpg"
image bg bedroom = "images/backgrounds/bedroom.jpg"
image bg prison = "images/backgrounds/prison.jpg"
image bg map_room = "images/backgrounds/map_room.jpg"
image bg creation = "images/backgrounds/creation.jpg"
image bg coronation_hall = "images/backgrounds/coronation_hall.jpg"
image bg cabinet = "images/backgrounds/cabinet.jpg"
image bg refectory = "images/backgrounds/refectory.jpg"
image bg palace_walls = "images/backgrounds/palace_walls.jpg"
image bg garden = "images/backgrounds/garden.jpg"
image bg watchtower = "images/backgrounds/watchtower.jpg"


# Prehistory & Prologue Backgrounds
image bg_prehistory_1 = "images/backgrounds/prehistory_1.jpg"
image bg_prehistory_2 = "images/backgrounds/prehistory_2.jpg"
image bg_prehistory_3 = "images/backgrounds/prehistory_3.jpg"
image bg_prehistory_4 = "images/backgrounds/prehistory_4.jpg"
image bg_prehistory_5 = "images/backgrounds/prehistory_5.jpg"
image bg_fathers_chambers = "images/backgrounds/fathers_chambers.jpg"

# Other Placeholders
image map_western_sibara = "images/ui/map_western_sibara.jpg"


# Player Character Parts (placeholders)
# Create subfolders in 'images' for organization, e.g., 'images/player/body/...'
image player wear simple = "images/player/wear/simple.png"
image player wear noble = "images/player/wear/noble.png"
image player wear warrior = "images/player/wear/warrior.png"
image player wear formal_robes = "images/player/wear/formal_robes.png"
image player wear hunting_leathers = "images/player/wear/hunting_leathers.png"
image player wear rags = "images/player/wear/rags.png"


# --- Heads (9 types) ---
image player head oval = "images/player/head/oval.png"
image player head round = "images/player/head/round.png"
image player head square = "images/player/head/square.png"
image player head heart = "images/player/head/heart.png"
image player head long = "images/player/head/long.png"
image player head diamond = "images/player/head/diamond.png"
image player head pear = "images/player/head/pear.png"
image player head oblong = "images/player/head/oblong.png"
image player head triangle = "images/player/head/triangle.png"

# --- Eyes (24 types) ---
image player eyes almond = "images/player/eyes/almond.png"
image player eyes round = "images/player/eyes/round.png"
image player eyes hooded = "images/player/eyes/hooded.png"
image player eyes upturned = "images/player/eyes/upturned.png"
image player eyes downturned = "images/player/eyes/downturned.png"
image player eyes monolid = "images/player/eyes/monolid.png"
image player eyes protruding = "images/player/eyes/protruding.png"
image player eyes deepset = "images/player/eyes/deepset.png"
image player eyes close_set = "images/player/eyes/close_set.png"
image player eyes wide_set = "images/player/eyes/wide_set.png"
image player eyes small = "images/player/eyes/small.png"
image player eyes large = "images/player/eyes/large.png"
image player eyes tired = "images/player/eyes/tired.png"
image player eyes sharp = "images/player/eyes/sharp.png"
image player eyes soft = "images/player/eyes/soft.png"
image player eyes heavy_lidded = "images/player/eyes/heavy_lidded.png"
image player eyes youthful = "images/player/eyes/youthful.png"
image player eyes aged = "images/player/eyes/aged.png"
image player eyes piercing = "images/player/eyes/piercing.png"
image player eyes gentle = "images/player/eyes/gentle.png"
image player eyes hollow = "images/player/eyes/hollow.png"
image player eyes bright = "images/player/eyes/bright.png"
image player eyes narrow = "images/player/eyes/narrow.png"
image player eyes droopy = "images/player/eyes/droopy.png"

# --- Pupils (14 types for each eye) ---
image player l_pupil normal = "images/player/pupils/left/normal.png"
image player l_pupil small = "images/player/pupils/left/small.png"
image player l_pupil large = "images/player/pupils/left/large.png"
image player l_pupil slit = "images/player/pupils/left/slit.png"
image player l_pupil goat = "images/player/pupils/left/goat.png"
image player l_pupil blind = "images/player/pupils/left/blind.png"
image player l_pupil red = "images/player/pupils/left/red.png"
image player l_pupil blue = "images/player/pupils/left/blue.png"
image player l_pupil green = "images/player/pupils/left/green.png"
image player l_pupil brown = "images/player/pupils/left/brown.png"
image player l_pupil hazel = "images/player/pupils/left/hazel.png"
image player l_pupil grey = "images/player/pupils/left/grey.png"
image player l_pupil glowing = "images/player/pupils/left/glowing.png"
image player l_pupil star = "images/player/pupils/left/star.png"

image player r_pupil normal = "images/player/pupils/right/normal.png"
image player r_pupil small = "images/player/pupils/right/small.png"
image player r_pupil large = "images/player/pupils/right/large.png"
image player r_pupil slit = "images/player/pupils/right/slit.png"
image player r_pupil goat = "images/player/pupils/right/goat.png"
image player r_pupil blind = "images/player/pupils/right/blind.png"
image player r_pupil red = "images/player/pupils/right/red.png"
image player r_pupil blue = "images/player/pupils/right/blue.png"
image player r_pupil green = "images/player/pupils/right/green.png"
image player r_pupil brown = "images/player/pupils/right/brown.png"
image player r_pupil hazel = "images/player/pupils/right/hazel.png"
image player r_pupil grey = "images/player/pupils/right/grey.png"
image player r_pupil glowing = "images/player/pupils/right/glowing.png"
image player r_pupil star = "images/player/pupils/right/star.png"

# --- Eyebrows (1 type + none) ---
image player eyebrows standard = "images/player/eyebrows/standard.png"
image player eyebrows none = Null()

# --- Noses (13 types) ---
image player nose straight = "images/player/nose/straight.png"
image player nose hooked = "images/player/nose/hooked.png"
image player nose button = "images/player/nose/button.png"
image player nose roman = "images/player/nose/roman.png"
image player nose wide = "images/player/nose/wide.png"
image player nose thin = "images/player/nose/thin.png"
image player nose crooked = "images/player/nose/crooked.png"
image player nose snub = "images/player/nose/snub.png"
image player nose sharp = "images/player/nose/sharp.png"
image player nose bulbous = "images/player/nose/bulbous.png"
image player nose flat = "images/player/nose/flat.png"
image player nose upturned = "images/player/nose/upturned.png"
image player nose hawk = "images/player/nose/hawk.png"

# --- Wrinkles (2 types + none) ---
image player wrinkles none = Null()
image player wrinkles crows_feet = "images/player/wrinkles/crows_feet.png"
image player wrinkles forehead = "images/player/wrinkles/forehead.png"

image player mouth neutral = "images/player/mouth/neutral.png"
image player mouth thin = "images/player/mouth/thin.png"
image player mouth full = "images/player/mouth/full.png"

image player cheekbones high = "images/player/cheekbones/high.png"
image player cheekbones low = "images/player/cheekbones/low.png"

image player cheeks gaunt = "images/player/cheeks/gaunt.png"
image player cheeks full = "images/player/cheeks/full.png"

image player beard none = Null() # No beard is an empty image
image player beard stubble = "images/player/beard/stubble.png"
image player beard long = "images/player/beard/long.png"

# --- Chin and Hair Placeholders ---
image player chin average = "images/player/chin/average.png"
image player chin square = "images/player/chin/square.png"
image player chin pointed = "images/player/chin/pointed.png"

image player hair_front short = "images/player/hair/front/short.png"
image player hair_front long = "images/player/hair/front/long.png"
image player hair_front widows_peak = "images/player/hair/front/widows_peak.png"
image player hair_front braided = "images/player/hair/front/braided.png"
image player hair_front top_knot = "images/player/hair/front/top_knot.png"
image player hair_front shaved_sides = "images/player/hair/front/shaved_sides.png"
image player hair_front bald = Null()

image player hair_back long = "images/player/hair/back/long.png"
image player hair_back braided = "images/player/hair/back/braided.png"
image player hair_back top_knot = "images/player/hair/back/top_knot.png"


# --- NPC Sprites (Fixed layered images) ---
image priest_sprite:
    "images/npcs/priest.png"

image captain_sprite:
    "images/npcs/captain.png"

# --- Solid Placeholder Avatars ---
image guard_sprite = "images/npcs/guard.png"
image janek_deathbed = "images/npcs/janek_deathbed.png"


# 3. Persistent Game Variables
#-------------------------------------------------------------------------------
default persistent.player_name = "Knyaz"
default persistent.player_title = "Knyaz" # or "Knyaginya"
default persistent.knyazhestvo_name = "Kholodny Krai"

# --- Player Appearance Variables (simplified names) ---
default persistent.age = "young"
default persistent.body = "average"
default persistent.underwear = "simple"
default persistent.wear = "noble"
default persistent.head = "oval"
default persistent.eyes = "almond"
default persistent.l_pupil = "normal"
default persistent.r_pupil = "normal"
default persistent.eyebrows = "standard"
default persistent.mouth = "neutral"
default persistent.nose = "straight"
default persistent.cheekbones = "high"
default persistent.cheeks = "gaunt"
default persistent.wrinkles = "none"
default persistent.beard = "none"
default persistent.chin = "average"
default persistent.hair_style = "long"

# Player stats
default persistent.diplomacy = 5
default persistent.warfare = 5
default persistent.stewardship = 5
default persistent.intrigue = 5
default persistent.piety = 5
default persistent.health = 100 # Player's health. If it reaches 0, the game ends.
default persistent.stress = 0   # High stress can lead to negative events.

# Principality Resources
default persistent.treasury = 100
default persistent.food = 100
default persistent.army_size = 50
default persistent.morale = 70

# Faction Loyalty (0-100)
default persistent.faction_church = 50
default persistent.faction_army = 50
default persistent.faction_empire = 50
default persistent.faction_commoners = 50
default persistent.faction_rich = 50

# Game State
default persistent.day = 1
default persistent.time = 8 # 24-hour format, starts at 8:00
default persistent.winter_days = 90 # Goal is to survive this many days
default persistent.game_over_reason = ""
default persistent.player_overthrown = False

# Story Flags
default persistent.has_partner = False
default persistent.cat_tamed = False

# 4. Game Screens
#-------------------------------------------------------------------------------

# --- Styles for Customization Screen ---
style customization_frame is frame:
    background "#00000099"
    padding (15, 15)
    xsize 450

# NEW style for the clickable rows used for keyboard navigation
style customization_row_button is button:
    background None
    padding (5, 3)
    hover_background "#ffffff22"
    properties gui.button_properties("default")

style customization_label is label:
    yalign 0.5

style customization_label_text is gui_text:
    color "#c0c0c0"
    size 18
    yalign 0.5

style customization_option_text is gui_text:
    color "#ffffff"
    text_align 0.5
    size 18
    yalign 0.5

style customization_title is label_text:
    color "#ffffff"
    size 24
    xalign 0.5
    padding (0, 10)

style customization_button is gui_button

style customization_button_text is gui_button_text:
    color "#ffffff"
    hover_color "#00ff00"
    bold True
    size 22


# --- Layered Image for the Player ---
# This combines all the player's appearance choices into one sprite.
layeredimage player_sprite:
    # The hair_back layer must be drawn first, behind everything else.
    if persistent.hair_style == "long":
        "images/player/hair/back/long.png"

    if persistent.hair_style == "braided":
        "images/player/hair/back/braided.png"

    if persistent.hair_style == "top_knot":
        "images/player/hair/back/top_knot.png"

    always:
        ConditionSwitch(
            "persistent.player_title == 'Knyaz'", "images/player/body/male/[persistent.body].png",
            "True", "images/player/body/female/[persistent.body].png"
        )

    always:
        ConditionSwitch(
            "persistent.player_title == 'Knyaz'", "images/player/underwear/male/[persistent.underwear].png",
            "True", "images/player/underwear/female/[persistent.underwear].png"
        )

    always "images/player/wear/[persistent.wear].png"
    always "images/player/head/[persistent.head].png"
    always "images/player/chin/[persistent.chin].png"
    always "images/player/eyes/[persistent.eyes].png"
    always "images/player/pupils/left/[persistent.l_pupil].png"
    always "images/player/pupils/right/[persistent.r_pupil].png"

    if persistent.eyebrows != "none":
        "images/player/eyebrows/[persistent.eyebrows].png"

    always "images/player/mouth/[persistent.mouth].png"
    always "images/player/nose/[persistent.nose].png"
    always "images/player/cheekbones/[persistent.cheekbones].png"
    always "images/player/cheeks/[persistent.cheeks].png"

    if persistent.wrinkles != "none":
        "images/player/wrinkles/[persistent.wrinkles].png"

    if persistent.hair_style != "bald":
        "images/player/hair/front/[persistent.hair_style].png"

    if persistent.player_title == "Knyaz" and persistent.beard != "none":
        "images/player/beard/[persistent.beard].png"


# This is a reusable screen for a single customization option row.
# It now accepts the data it needs as arguments to avoid scope errors.
screen customization_row(category_name, category_label):
    # Get the list of options for this category from the parent scope
    $ options_list = customization_options_map[category_name]
    # Get the index of this category in the navigation order
    $ category_index = property_order.index(category_name)

    button:
        # When clicked, this row becomes the active one for keyboard controls.
        action SetVariable("current_property_index", category_index)
        style "customization_row_button"
        # The background changes to show it's selected for keyboard focus.
        if current_property_index == category_index:
            background "#ffffff33"
        else:
            background None

        hbox:
            label category_label style "customization_label"
            # The "<" button to go to the previous option.
            textbutton "<" style "customization_button" action SetField(persistent, category_name, options_list[(options_list.index(getattr(persistent, category_name)) - 1) % len(options_list)])
            # Display the current option's name.
            text "[getattr(persistent, category_name)]" style "customization_option_text" min_width 150
            # The ">" button to go to the next option.
            textbutton ">" style "customization_button" action SetField(persistent, category_name, options_list[(options_list.index(getattr(persistent, category_name)) + 1) % len(options_list)])


# --- Appearance Customization Screen ---
# --- Appearance Customization Screen ---
screen appearance_customization_screen():
    tag menu
    add "bg creation"

    # This python block sets up all the data and functions needed for the screen.
    python:
        # Define the lists of options for cycling
        age_options = ["young", "middle-aged", "old"]
        body_options = ["average", "thin", "muscular"]
        wear_options = ["noble", "simple", "warrior", "formal_robes", "hunting_leathers", "rags"]
        underwear_options = ["simple", "fine"]
        head_options = ["oval", "round", "square", "heart", "long", "diamond", "pear", "oblong", "triangle"]
        hair_style_options = ["long", "short", "widows_peak", "bald", "braided", "top_knot", "shaved_sides"]
        chin_options = ["average", "square", "pointed"]
        eyes_options = ["almond", "round", "hooded", "upturned", "downturned", "monolid", "protruding", "deepset", "close_set", "wide_set", "small", "large", "tired", "sharp", "soft", "heavy_lidded", "youthful", "aged", "piercing", "gentle", "hollow", "bright", "narrow", "droopy"]
        l_pupil_options = ["normal", "small", "large", "slit", "goat", "blind", "red", "blue", "green", "brown", "hazel", "grey", "glowing", "star"]
        r_pupil_options = ["normal", "small", "large", "slit", "goat", "blind", "red", "blue", "green", "brown", "hazel", "grey", "glowing", "star"]
        eyebrows_options = ["standard", "none"]
        mouth_options = ["neutral", "thin", "full"]
        nose_options = ["straight", "hooked", "button", "roman", "wide", "thin", "crooked", "snub", "sharp", "bulbous", "flat", "upturned", "hawk"]
        cheekbones_options = ["high", "low"]
        cheeks_options = ["gaunt", "full"]
        wrinkles_options = ["none", "crows_feet", "forehead"]
        beard_options = ["none", "stubble", "long"]

        # This dictionary maps persistent variable names to their option lists.
        customization_options_map = {
            "age": age_options, "body": body_options, "wear": wear_options,
            "underwear": underwear_options, "head": head_options,
            "hair_style": hair_style_options, "chin": chin_options, "eyes": eyes_options,
            "l_pupil": l_pupil_options, "r_pupil": r_pupil_options,
            "eyebrows": eyebrows_options, "mouth": mouth_options, "nose": nose_options,
            "cheekbones": cheekbones_options, "cheeks": cheeks_options,
            "wrinkles": wrinkles_options, "beard": beard_options,
        }

        # This ordered list of properties is used for up/down keyboard navigation.
        property_order = [
            "age", "body", "hair_style", "head", "chin", "eyes", "l_pupil",
            "r_pupil", "eyebrows", "nose", "mouth", "cheekbones", "cheeks",
            "wrinkles", "wear", "underwear"
        ]
        # Only add the beard option if the character is male.
        if persistent.player_title == "Knyaz":
            property_order.append("beard")

        # This function is called by the arrow keys to cycle through options.
        def cycle_persistent_option(category, direction):
            if category in customization_options_map:
                options_list = customization_options_map[category]

                # Prevent changing beard if not Knyaz
                if category == 'beard' and persistent.player_title != 'Knyaz':
                    return

                current_value = getattr(persistent, category)
                try:
                    current_index = options_list.index(current_value)
                except ValueError:
                    current_index = 0

                new_index = (current_index + direction) % len(options_list)
                new_value = options_list[new_index]
                setattr(persistent, category, new_value)

        # Validation
        if persistent.age not in age_options: persistent.age = age_options[0]
        if persistent.body not in body_options: persistent.body = body_options[0]
        if persistent.wear not in wear_options: persistent.wear = wear_options[0]
        if persistent.underwear not in underwear_options: persistent.underwear = underwear_options[0]
        if persistent.head not in head_options: persistent.head = head_options[0]
        if persistent.hair_style not in hair_style_options: persistent.hair_style = hair_style_options[0]
        if persistent.chin not in chin_options: persistent.chin = chin_options[0]
        if persistent.eyes not in eyes_options: persistent.eyes = eyes_options[0]
        if persistent.l_pupil not in l_pupil_options: persistent.l_pupil = l_pupil_options[0]
        if persistent.r_pupil not in r_pupil_options: persistent.r_pupil = r_pupil_options[0]
        if persistent.eyebrows not in eyebrows_options: persistent.eyebrows = eyebrows_options[0]
        if persistent.mouth not in mouth_options: persistent.mouth = mouth_options[0]
        if persistent.nose not in nose_options: persistent.nose = nose_options[0]
        if persistent.cheekbones not in cheekbones_options: persistent.cheekbones = cheekbones_options[0]
        if persistent.cheeks not in cheeks_options: persistent.cheeks = cheeks_options[0]
        if persistent.wrinkles not in wrinkles_options: persistent.wrinkles = wrinkles_options[0]
        if persistent.beard not in beard_options: persistent.beard = beard_options[0]

    default current_property_index = 0

    key "down" action SetVariable("current_property_index", (current_property_index + 1) % len(property_order))
    key "up" action SetVariable("current_property_index", (current_property_index - 1) % len(property_order))  
    key "left" action Function(cycle_persistent_option, category=property_order[current_property_index], direction=-1)
    key "right" action Function(cycle_persistent_option, category=property_order[current_property_index], direction=1)

    hbox:
        # Character Preview
        vbox:
            xalign 0.3 yalign 0.5
            add "player_sprite"

        # Customization Options
        frame:
            style "customization_frame"
            xalign 0.85 yalign 0.5
            has vbox

            label "Appearance" style "customization_title"

            viewport:
                scrollbars "vertical"
                mousewheel True
                yfill True

                vbox:
                    style "vbox"
                    spacing 2

                    # Define rows inline
                    for cat_name, cat_label in [
                        ("age", "Age:"),
                        ("body", "Body:"),
                        ("hair_style", "Hair:"),
                        ("head", "Head:"),
                        ("chin", "Chin:"),
                        ("eyes", "Eyes:"),
                        ("l_pupil", "Left Pupil:"),
                        ("r_pupil", "Right Pupil:"),
                        ("eyebrows", "Eyebrows:"),
                        ("nose", "Nose:"),
                        ("mouth", "Mouth:"),
                        ("cheekbones", "Cheekbones:"),
                        ("cheeks", "Cheeks:"),
                        ("wrinkles", "Wrinkles:"),
                        ("wear", "Wear:"),
                        ("underwear", "Underwear:"),
                    ]:
                        $ options_list = customization_options_map[cat_name]
                        $ category_index = property_order.index(cat_name)

                        button:
                            action SetVariable("current_property_index", category_index)
                            style "customization_row_button"
                            if current_property_index == category_index:
                                background "#ffffff33"
                            else:
                                background None

                            hbox:
                                label cat_label style "customization_label"
                                textbutton "<" style "customization_button" action SetField(persistent, cat_name, options_list[(options_list.index(getattr(persistent, cat_name)) - 1) % len(options_list)])
                                text "[getattr(persistent, cat_name)]" style "customization_option_text" min_width 150
                                textbutton ">" style "customization_button" action SetField(persistent, cat_name, options_list[(options_list.index(getattr(persistent, cat_name)) + 1) % len(options_list)])

                    # Beard option only for Knyaz
                    if persistent.player_title == "Knyaz":
                        $ options_list = customization_options_map["beard"]
                        $ category_index = property_order.index("beard")

                        button:
                            action SetVariable("current_property_index", category_index)
                            style "customization_row_button"
                            if current_property_index == category_index:
                                background "#ffffff33"
                            else:
                                background None

                            hbox:
                                label "Beard:" style "customization_label"
                                textbutton "<" style "customization_button" action SetField(persistent, "beard", options_list[(options_list.index(getattr(persistent, "beard")) - 1) % len(options_list)])
                                text "[getattr(persistent, 'beard')]" style "customization_option_text" min_width 150
                                textbutton ">" style "customization_button" action SetField(persistent, "beard", options_list[(options_list.index(getattr(persistent, "beard")) + 1) % len(options_list)])

            textbutton "Confirm" action Return() xalign 0.5


# Main UI screen overlay showing key stats
screen hud():
    frame:
        style "frame"
        xalign 0.98
        yalign 0.02
        vbox:
            text "Day: [persistent.day] / [persistent.winter_days]"
            text "Time: [persistent.time]:00"
            text "Treasury: [persistent.treasury]"
            text "Food: [persistent.food]"
            text "Health: [persistent.health]"
            text "Stress: [persistent.stress]"

# Palace Map Screen
screen palace_map_screen():
    tag menu

    imagemap:
        ground "bg_palace_map"
        hover "images/ui/map_hover.png" # Placeholder for hover effect

        # Define clickable areas on the map
        hotspot (100, 150, 150, 100) action Jump("throne_room_events") tooltip "Throne Room"
        hotspot (260, 150, 150, 100) action Jump("bedroom_events") tooltip "Bedroom"
        hotspot (420, 150, 150, 100) action Jump("cabinet_events") tooltip "Cabinet"
        hotspot (580, 150, 150, 100) action Jump("map_room_events") tooltip "Map Room"

        hotspot (100, 260, 150, 100) action Jump("refectory_events") tooltip "Refectory"
        hotspot (260, 260, 150, 100) action Jump("garden_events") tooltip "Garden"
        hotspot (420, 260, 150, 100) action Jump("palace_walls_events") tooltip "Palace Walls"
        hotspot (580, 260, 150, 100) action Jump("watchtower_events") tooltip "Watchtower"

        hotspot (100, 370, 150, 100) action Jump("prison_events") tooltip "Prison"


# --- Main Menu Logic ---
# The following screen and styles define the game's main menu.
# Ren'Py automatically uses a screen named 'main_menu' when the game starts.

# Style definitions for the main menu elements.
# Ensure the font file 'Skolar PE Variable Regular (1).ttf' is in the 'game' folder.
style main_menu_title is gui_title_text:
    font "gui/fonts/Skolar PE Variable Regular (1).ttf"
    size 70
    color "#e0e0e0"
    text_align 0.5
    xalign 0.5
    outlines []

style main_menu_button is gui_button:
    size_group "main_menu"
    properties gui.button_properties("main_menu_button")

style main_menu_button_text is gui_button_text:
    font "Skolar PE Variable Regular (1).ttf"
    properties gui.button_text_properties("main_menu_button")
    size 28
    color "#a0a0a0"
    hover_color "#ffffff"

screen main_menu():
    tag menu

    # Add the video background.
    # Ensure you have a video file (e.g., .webm, .mp4) at 'game/images/bg_main_menu.webm'
    add Movie(play="images/bg_main_menu.webm", loop=True)

    # Use a frame to organize the layout
    frame:
        style "gui_vbox"
        xalign 0.5
        yalign 0.5

        # Game Title
        text "One Winter from the Life of a Knyaz":
            style "main_menu_title"
            yalign 0.3

        # Navigation Menu
        vbox:
            style "gui_menu_vbox"
            yalign 0.7
            spacing 15

            textbutton _("New Game") action Start()
            textbutton _("Load Game") action ShowMenu("load")
            textbutton _("Preferences") action ShowMenu("preferences")
            textbutton _("Quit") action Quit(confirm=False)


# 5. Game Logic and Story Starts Here
#-------------------------------------------------------------------------------

label start:
    # This will only run on a new game.
    if persistent.day == 1 and persistent.time == 8:
        jump prehistory
    else:
        # Returning player
        narrator "The bleak winter wind howls, a familiar, unwelcome sound."
        jump daily_loop

label prehistory:
    scene bg_prehistory_1
    narrator "In 3753 of the fourth era, Tsar Nicholas I of Sibara, following the results of the 2nd Sibara-Tealea War, seized the territories of middle Avrosia, naming them western Sibara due to the proximity of the local people."

    scene bg_prehistory_2
    narrator "There was no limit to the jubilation, because finally, the Sibarian tribes were reunited into one whole."

    scene bg_prehistory_3
    narrator "However, for fear of being hit by the armies of Tealea and Neumeierland, the Tsar began to build a line of fortifications, shifting agriculture."

    scene bg_prehistory_4
    narrator "This spring of 3793, there was a terrible crop failure in the Sibarian Empire. Cattle were dying before our eyes, and people in the central regions of the empire barely had enough food."

    scene bg_prehistory_5
    narrator "In western Sibara, things were much worse. There was no food at all, and in September your father, Knyaz Janek, took to his deathbed."

    jump character_creation


label prologue_scene:
    # This scene happens right after character creation.
    scene bg bedroom
    narrator "You are contemplating the grim state of your lands when a guard enters, his face pale."

    show guard_sprite at left with dissolve

    if persistent.player_title == "Knyaz":
        guard "Sir [persistent.player_name], your father is dying and asks you to come to his chambers."
    else:
        guard "My Lady [persistent.player_name], your father is dying and asks you to come to his chambers."

    show player_sprite at player_right with dissolve

    menu:
        "I will go at once.":
            player "Yes."
            jump fathers_deathbed
        "I need a moment.":
            player "No."
            hide player_sprite
            guard "There is no time, Your Highness. He is fading fast."
            narrator "The guard's urgency leaves you no real choice."
            jump fathers_deathbed

label fathers_deathbed:
    scene bg_fathers_chambers
    show janek_deathbed at center with dissolve

    narrator "You enter your father's chambers. The air is thick with the scent of milk thistle and death. Knyaz Janek lies in his bed, his breath a shallow rattle."

    show player_sprite at player_left with dissolve

    if persistent.player_title == "Knyaz":
        janek "My son... [persistent.player_name]..."
        janek "Listen to me. The winter... it will be the hardest this land has ever known. There is no food. The wolves circle..."
        janek "You must be strong. Stronger than I was. You are the Knyaz now. Rule... wisely. Protect... our people..."
    else: # Player is Knyaginya
        janek "My daughter... [persistent.player_name]..."
        janek "Your brother... he is too young. Too weak for what is coming. The nobles will tear him apart."
        janek "You must rule in his stead. As regent. Despite... despite the traditions. You have a strength he does not."
        janek "Protect him. Protect our people. Survive... the winter..."

    narrator "His eyes close, and the rattling breath ceases. A heavy silence fills the room."

    hide player_sprite
    hide janek_deathbed

    jump coronation_scene

label coronation_scene:
    scene bg coronation_hall

    narrator "The days that follow are a blur of grief and hurried preparations."
    narrator "In the bleak, stone-cold great hall, you are crowned."

    show priest_sprite at left
    show captain_sprite at right

    priest "And so we anoint thee [persistent.player_name], [persistent.player_title] of [persistent.knyazhestvo_name]."

    show player_sprite at player_center
    priest "May your reign be long, and may the gods see fit to guide you through the coming darkness."
    narrator "The crown is heavy. Heavier than you imagined. It feels cold."

    hide player_sprite
    hide priest_sprite
    hide captain_sprite

    narrator "Your rule has begun."
    jump room_bedroom

label daily_loop:
    # Check for game over conditions at the start of each day
    if persistent.health <= 0:
        $ persistent.game_over_reason = "Your body, frail and broken, has finally given up. The winter claims another soul."
        jump player_death
    if persistent.day > persistent.winter_days:
        jump spring_arrived

    # Show the main navigation hub
    narrator "Another grey dawn breaks over [persistent.knyazhestvo_name]. The cold seeps into the stone."
    call screen hud
    call screen palace_map_screen

# --- ROOM EVENTS START HERE ---

label throne_room_events:
    scene bg throne_room
    menu:
        "Start the reception":
            show player_sprite at player_right with dissolve
            narrator "You take your seat on the cold throne. The great hall is drafty, filled with petitioners and opportunists."
            $ event_roll = renpy.random.randint(1, 3)
            if event_roll == 1:
                show priest_sprite at left with dissolve
                narrator "A priest approaches, his face grim. It is Father Yevgraf, his eyes filled with pious fire."
                priest "Your Highness, the people are restless. They see ill omens in the frost. We require funds to hold the proper rituals to appease the old gods."
                menu:
                    "Grant them 20 gold. (Lose 20 Treasury, +5 Church, -2 Rich)":
                        $ persistent.treasury -= 20
                        $ persistent.faction_church += 5
                        $ persistent.faction_rich -= 2
                        $ persistent.time += 1
                        priest "The heavens will look kindly on this."
                    "We have no coin to spare for superstition. (Lose 5 Church, +3 Rich)":
                        $ persistent.faction_church -= 5
                        $ persistent.faction_rich += 3
                        $ persistent.time += 1
                        priest "He scowls. 'The spirits will remember this.'"
                hide priest_sprite
            elif event_roll == 2:
                show captain_sprite at left with dissolve
                narrator "Captain Borislav, his face a roadmap of old scars, bows stiffly."
                captain "My [persistent.player_title], the men's weapons are old and rusted. We need new steel if we are to defend our borders from the northern tribes."
                menu:
                    "Spend 30 gold on new equipment. (Lose 30 Treasury, +5 Army)":
                        $ persistent.treasury -= 30
                        $ persistent.faction_army += 5
                        $ persistent.time += 1
                        captain "A rare smile crosses his face. 'They will be put to good use.'"
                    "Make do with what you have. Our treasury is stretched thin. (-5 Army)":
                        $ persistent.faction_army -= 5
                        $ persistent.time += 1
                        captain "He salutes, but his disappointment is palpable. 'As you command.'"
                hide captain_sprite
            else:
                narrator "The day is quiet. Too quiet. The silence feels heavier than any petition."
                $ persistent.time += 2
            hide player_sprite
            jump daily_loop
        "Return to the map":
            jump daily_loop

label cabinet_events:
    scene bg cabinet
    show player_sprite at player_center
    menu:
        "Write a letter":
            $ persistent.time += 2
            narrator "You draft a letter to a neighboring Knyaz, hoping for an ally in these dark times. It is a long shot."
            $ persistent.diplomacy += 1
            jump daily_loop

        "Read a book (+1 Stewardship)":
            $ persistent.time += 2
            narrator "You lose yourself in a tome on agricultural techniques. Perhaps something in these pages can save your people from starvation."
            $ persistent.stewardship += 1
            jump daily_loop

        "Look out the window":
            $ persistent.time += 1
            narrator "From here, you can see the edge of the forest. It looks dark, and hungry."
            jump daily_loop

        "Return to the map":
            hide player_sprite
            jump daily_loop

label refectory_events:
    scene bg refectory
    menu:
        "Have breakfast (-2 Food, -5 Stress)" if persistent.time <= 9:
            $ persistent.food -= 2
            $ persistent.stress -= 5
            $ persistent.time += 1
            narrator "You eat a meager breakfast of stale bread and weak ale. It does little to warm you."
            jump daily_loop

        "Have lunch (-3 Food, -5 Stress)" if persistent.time >= 13 and persistent.time <= 15:
            $ persistent.food -= 3
            $ persistent.stress -= 5
            $ persistent.time += 1
            narrator "A thin stew for lunch. You wonder how much longer the stores will last."
            jump daily_loop

        "Have dinner (-4 Food, -5 Stress)" if persistent.time >= 18 and persistent.time <= 20:
            $ persistent.food -= 4
            $ persistent.stress -= 5
            $ persistent.time += 1
            narrator "Dinner is a quiet, somber affair. Every bite is a reminder of the coming famine."
            jump daily_loop

        "Speak to the cook":
            $ persistent.time += 1
            cook "Your Highness. The stores are low. The salt is running out. I... I am doing my best."
            narrator "The cook's tired eyes tell a story of their own."
            jump daily_loop

        "Return to the map":
            jump daily_loop

label prison_events:
    scene bg prison
    show player_sprite at player_center
    menu:
        "Speak with the prisoners":
            $ persistent.time += 1
            narrator "The cells are currently empty. It is a small mercy."
            jump daily_loop

        "Speak with the guard":
            $ persistent.time += 1
            guard "All is quiet, Your Highness. Cold, but quiet."
            narrator "The guard shivers, his breath misting in the air."
            jump daily_loop

        "Return to the map":
            hide player_sprite
            jump daily_loop

label map_room_events:
    scene bg map_room
    show player_sprite at player_center
    menu:
        "Open map of Western Sibara":
            show map_western_sibara at center
            narrator "The familiar names of the knyazhestvas are spread before you: Volya, Zarya, Tuman... so many rivals, so few friends."
            $ persistent.time += 1
            hide map_western_sibara
            jump daily_loop

        "Send a scouting party (15 soldiers)":
            if persistent.army_size >= 15:
                $ persistent.army_size -= 15
                $ persistent.time += 3
                narrator "You dispatch 15 soldiers into the northern wastes. With luck, they will return with news of the Wild Tribes. Or return at all."
                # TODO: Add a future event for their return
            else:
                narrator "You do not have enough soldiers to spare for such a mission."
            jump daily_loop

        "Diplomacy with other knyazhestvas (15 Treasury)":
            if persistent.treasury >= 15:
                $ persistent.treasury -= 15
                $ persistent.time += 2
                narrator "Your envoy sets out, carrying offers of trade or alliance. You can only hope they are received well."
                # TODO: Trigger a future event based on this.
            else:
                narrator "We cannot afford the expense of diplomacy right now."
            jump daily_loop

        "Return to the map":
            hide player_sprite
            jump daily_loop

label garden_events:
    scene bg garden
    show player_sprite at player_center
    menu:
        "Speak to your siblings":
            $ persistent.time += 2
            if persistent.player_title == "Knyaz":
                sister "Brother. The garden is dying. Everything is."
            else:
                sister "Sister... are you afraid?"
                brother "Lyudmila! Do not bother the Knyaginya with such questions."
            narrator "Your siblings offer little comfort."
            jump daily_loop

        "Play with the cat (-10 Stress)" if persistent.cat_tamed:
            $ persistent.stress -= 10
            $ persistent.time += 1
            narrator "The cat chases a dead leaf across the frozen ground, a brief flash of life in the grey garden."
            jump daily_loop

        "Feed the cat (-1 Food)" if persistent.cat_tamed:
            $ persistent.food -= 1
            $ persistent.time += 1
            narrator "You give the cat a scrap of salted fish. It devours it greedily. You have one less mouth to feed, at least."
            jump daily_loop

        "Return to the map":
            hide player_sprite
            jump daily_loop

label palace_walls_events:
    scene bg palace_walls
    show player_sprite at player_center
    menu:
        "Look to the horizon":
            $ persistent.time += 1
            narrator "The sky and the land blend into a single white expanse. It feels like the world ends just beyond your walls."
            jump daily_loop

        "Speak with a guard":
            $ persistent.time += 1
            guard "Your Highness. The wind bites hard today."
            narrator "The guard's face is red with cold."
            jump daily_loop

        "Find and tame the cat" if not persistent.cat_tamed:
            $ persistent.time += 1
            narrator "You spot a skinny black cat skulking near the kitchens. It watches you with wary, green eyes."
            if renpy.random.randint(1, 3) == 1:
                $ persistent.cat_tamed = True
                narrator "You offer it a piece of dried meat. It hesitates, then snatches it and allows you to stroke its fur. It seems you have a new companion."
            else:
                narrator "It hisses and darts away before you can get close."
            jump daily_loop

        "Return to the map":
            hide player_sprite
            jump daily_loop

label watchtower_events:
    scene bg watchtower
    show player_sprite at player_center
    menu:
        "Look to the horizon":
            $ persistent.time += 1
            narrator "From this high vantage, you can see for miles. The forest is a dark smudge to the north. The southern road is empty. Nothing moves."
            jump daily_loop

        "Return to the map":
            hide player_sprite
            jump daily_loop

# --- End of Day and Game Over States ---

label day_end:
    # Daily resource consumption
    $ food_consumed = persistent.army_size / 10 + 5
    $ persistent.food -= food_consumed
    narrator "Night falls. The principality consumes [food_consumed] food."

    # Check for negative consequences
    if persistent.food < 0:
        $ persistent.food = 0
        $ persistent.faction_commoners -= 5
        $ persistent.morale -= 10
        narrator "There is not enough food. The people are starving, and the army's morale plummets."

    if persistent.stress > 80:
        $ persistent.health -= 5
        narrator "The immense stress of your rule weighs on your health."

    # TODO: Add faction plot events here. If loyalty is too low, they might try to overthrow you.
    if persistent.faction_army < 20:
        narrator "You hear whispers of mutiny among your soldiers. Your authority is slipping."

    # Advance the day
    $ persistent.day += 1
    $ persistent.time = 8 # Reset time for the new day
    jump daily_loop


label spring_arrived:
    narrator "A warm wind blows from the south. The snow begins to melt."
    narrator "You have done it. You have survived the winter."
    if persistent.player_overthrown:
        "Though you no longer rule, you are alive. You watch the spring thaw from a simple hut, a survivor, if not a ruler."
        "The end."
        return
    else:
        "You stand on your balcony, the ruler of [persistent.knyazhestvo_name]. The land is weak, the people are weary, but you survived. You endured."
        "For now, that is enough."
        "The end."
        return

label player_death:
    scene black
    "It is over."
    "[persistent.game_over_reason]"
    "Your rule, and your life, are consumed by the unforgiving winter."
    return

label player_overthrown:
    # This can be jumped to from a faction plot event
    $ persistent.player_overthrown = True
    narrator "The coup was swift. Your own guards turned against you."
    narrator "They did not kill you. Instead, they cast you out, exiling you from your own lands."
    jump spring_arrived # Even if overthrown, the goal is to survive.

################################################################################
## Updated Character Creation Labels
## Replace the character_creation label in your script.rpy
################################################################################

label character_creation:
    narrator "A heavy crown now falls upon a new head."

    menu:
        "Who are you?"
        "A son, the heir.":
            $ persistent.player_title = "Knyaz"
            $ persistent.warfare += 2
        "A daughter, the regent.":
            $ persistent.player_title = "Knyaginya"
            $ persistent.diplomacy += 2

    $ player_name_input = renpy.input("What is your name?", length=15, default="Alexei" if persistent.player_title == "Knyaz" else "Anastasia").strip()
    if not player_name_input:
        $ player_name_input = "Alexei" if persistent.player_title == "Knyaz" else "Anastasia"
    $ persistent.player_name = player_name_input

    # Call the NEW enhanced appearance customization screen
    call screen appearance_customization_screen_v2

    $ knyazhestvo_name_input = renpy.input("What is the name of this cold, forgotten land you rule?", length=20, default="Gorestir").strip()
    if not knyazhestvo_name_input:
        $ knyazhestvo_name_input = "Gorestir"
    $ persistent.knyazhestvo_name = knyazhestvo_name_input

    jump prologue_scene


################################################################################
## Enhanced HUD with Character Customization Access
## Replace the hud screen in your script
################################################################################

screen hud():
    # Main stats frame
    frame:
        style "frame"
        xalign 0.98
        yalign 0.02
        vbox:
            spacing 5
            text "Day: [persistent.day] / [persistent.winter_days]" size 18
            text "Time: [persistent.time]:00" size 18
            text "Treasury: [persistent.treasury]" size 18
            text "Food: [persistent.food]" size 18
            text "Health: [persistent.health]" size 18
            text "Stress: [persistent.stress]" size 18
    
    # Quick access buttons
    hbox:
        xalign 0.02
        yalign 0.02
        spacing 10
        
        textbutton "⚙":
            action ShowMenu("enhanced_preferences")
            tooltip "Settings"
            xsize 40
            ysize 40
        
        textbutton "👤":
            action Show("character_appearance_menu")
            tooltip "Change Appearance"
            xsize 40
            ysize 40


################################################################################
## Character Appearance Menu (In-Game Access)
################################################################################

screen character_appearance_menu():
    modal True
    zorder 100
    
    add Solid("#000000aa")
    
    frame:
        xalign 0.5
        yalign 0.5
        xsize 400
        padding (30, 30)
        
        vbox:
            spacing 20
            
            text "Character Menu" size 28 xalign 0.5
            
            textbutton "Customize Appearance":
                xsize 340
                action [
                    Hide("character_appearance_menu"),
                    Show("appearance_customization_screen_v2")
                ]
            
            textbutton "Save Current Look":
                xsize 340
                action [
                    Hide("character_appearance_menu"),
                    Show("save_appearance_dialog")
                ]
            
            textbutton "Load Saved Look":
                xsize 340
                action [
                    Hide("character_appearance_menu"),
                    Show("load_appearance_presets")
                ]
            
            null height 10
            
            textbutton "View Stats":
                xsize 340
                action [
                    Hide("character_appearance_menu"),
                    Show("character_stats_screen")
                ]
            
            null height 20
            
            textbutton "Close":
                xsize 340
                action Hide("character_appearance_menu")


################################################################################
## Character Stats Screen
################################################################################

screen character_stats_screen():
    modal True
    
    add Solid("#000000aa")
    
    frame:
        xalign 0.5
        yalign 0.5
        xsize 600
        padding (30, 30)
        
        vbox:
            spacing 20
            
            text "[persistent.player_name], [persistent.player_title] of [persistent.knyazhestvo_name]":
                size 32
                xalign 0.5
                color "#ffffff"
            
            null height 10
            
            # Personal Stats
            label "Personal Attributes" xalign 0.5
            
            grid 2 5:
                spacing 10
                xalign 0.5
                
                text "Diplomacy:" color "#c0c0c0"
                text "[persistent.diplomacy]" color "#ffffff"
                
                text "Warfare:" color "#c0c0c0"
                text "[persistent.warfare]" color "#ffffff"
                
                text "Stewardship:" color "#c0c0c0"
                text "[persistent.stewardship]" color "#ffffff"
                
                text "Intrigue:" color "#c0c0c0"
                text "[persistent.intrigue]" color "#ffffff"
                
                text "Piety:" color "#c0c0c0"
                text "[persistent.piety]" color "#ffffff"
            
            null height 20
            
            # Faction Relations
            label "Faction Relations" xalign 0.5
            
            vbox:
                spacing 8
                xsize 540
                
                # Church faction
                hbox:
                    text "Church:" xsize 150 color "#c0c0c0"
                    bar value persistent.faction_church range 100 xsize 300
                    text "[persistent.faction_church]" xsize 50 xalign 1.0
                
                # Army faction
                hbox:
                    text "Army:" xsize 150 color "#c0c0c0"
                    bar value persistent.faction_army range 100 xsize 300
                    text "[persistent.faction_army]" xsize 50 xalign 1.0
                
                # Empire faction
                hbox:
                    text "Empire:" xsize 150 color "#c0c0c0"
                    bar value persistent.faction_empire range 100 xsize 300
                    text "[persistent.faction_empire]" xsize 50 xalign 1.0
                
                # Commoners faction
                hbox:
                    text "Commoners:" xsize 150 color "#c0c0c0"
                    bar value persistent.faction_commoners range 100 xsize 300
                    text "[persistent.faction_commoners]" xsize 50 xalign 1.0
                
                # Rich faction
                hbox:
                    text "Nobility:" xsize 150 color "#c0c0c0"
                    bar value persistent.faction_rich range 100 xsize 300
                    text "[persistent.faction_rich]" xsize 50 xalign 1.0
            
            null height 20
            
            textbutton "Close":
                xalign 0.5
                xsize 200
                action Hide("character_stats_screen")


################################################################################
## Enhanced Bedroom Events with Character Menu Access
## Update the bedroom_events label
################################################################################

label bedroom_events:
    scene bg bedroom
    show player_sprite at player_center with dissolve
    menu:
        "Sleep (End the Day)":
            hide player_sprite
            jump day_end

        "Customize Appearance":
            hide player_sprite
            call screen appearance_customization_screen_v2
            jump daily_loop

        "Pray (+2 Piety, -5 Stress)":
            $ persistent.piety += 2
            $ persistent.stress -= 5
            $ persistent.time += 1
            narrator "You kneel before a small icon, the silence of the room a brief comfort. For a moment, the weight on your shoulders feels lighter."
            jump daily_loop

        "Look at your father's portrait":
            $ persistent.time += 1
            narrator "You gaze at the severe face of Knyaz Janek, painted in his prime. He looks strong, indomitable. Nothing like the frail man who died in his bed. You wonder if he would be proud, or disappointed."
            jump daily_loop

        "Look in the mirror":
            $ persistent.time += 1
            narrator "You see your own reflection. The face of the ruler of [persistent.knyazhestvo_name]. Do you see a leader, or just a frightened soul wearing a crown?"
            menu:
                "I should change my appearance.":
                    call screen appearance_customization_screen_v2
                "This is who I am.":
                    pass
            jump daily_loop

        "Look out the window":
            $ persistent.time += 1
            narrator "The courtyard below is dusted with the first snows of winter. The sky is a uniform, unforgiving grey."
            jump daily_loop

        "Play with the cat (-10 Stress)" if persistent.cat_tamed:
            $ persistent.stress -= 10
            $ persistent.time += 1
            narrator "The small cat purrs loudly as you scratch behind its ears. A simple, honest affection in a world of schemes."
            jump daily_loop

        "Talk to your partner" if persistent.has_partner:
            $ persistent.time += 2
            narrator "You spend some time with your partner, a rare moment of peace."
            jump daily_loop

        "Return to the map":
            hide player_sprite
            jump daily_loop


################################################################################
## Initialize Keyboard Controls for Customization
## Add this to your init python block
################################################################################

init python:
    # Ensure keyboard controls are properly mapped
    config.keymap['dismiss'] = ['mouseup_1', 'K_RETURN', 'K_SPACE', 'K_KP_ENTER']
    
    # Function to cycle through appearance options with validation
    def safe_cycle_option(category, direction):
        options_map = {
            "age": ["young", "middle-aged", "old"],
            "body": ["average", "thin", "muscular"],
            "head": ["oval", "round", "square", "heart", "long", "diamond", "pear", "oblong", "triangle"],
            "chin": ["average", "square", "pointed"],
            "eyes": ["almond", "round", "hooded", "upturned", "downturned", "monolid", "protruding", "deepset"],
            "nose": ["straight", "hooked", "button", "roman", "wide", "thin", "crooked", "snub", "sharp"],
            "mouth": ["neutral", "thin", "full"],
            "cheekbones": ["high", "low"],
            "cheeks": ["gaunt", "full"],
            "l_pupil": ["normal", "small", "large", "blue", "green", "brown", "hazel", "grey"],
            "r_pupil": ["normal", "small", "large", "blue", "green", "brown", "hazel", "grey"],
            "eyebrows": ["standard", "none"],
            "wrinkles": ["none", "crows_feet", "forehead"],
            "hair_style": ["long", "short", "widows_peak", "bald", "braided", "top_knot", "shaved_sides"],
            "beard": ["none", "stubble", "long"],
            "wear": ["noble", "simple", "warrior", "formal_robes", "hunting_leathers", "rags"],
            "underwear": ["simple", "fine"]
        }
        
        # Skip beard if not male
        if category == "beard" and persistent.player_title != "Knyaz":
            return
        
        if category in options_map:
            options = options_map[category]
            current_value = getattr(persistent, category)
            
            try:
                current_index = options.index(current_value)
            except ValueError:
                current_index = 0
            
            new_index = (current_index + direction) % len(options)
            setattr(persistent, category, options[new_index])
            renpy.restart_interaction()


################################################################################
## Quick Save/Load Appearance Presets
################################################################################

init python:
    import json
    import os
    
    def export_appearance_to_file():
        """Export current appearance to a JSON file"""
        try:
            appearance_data = {
                "name": persistent.player_name,
                "title": persistent.player_title,
                "age": persistent.age,
                "body": persistent.body,
                "head": persistent.head,
                "chin": persistent.chin,
                "eyes": persistent.eyes,
                "nose": persistent.nose,
                "mouth": persistent.mouth,
                "cheekbones": persistent.cheekbones,
                "cheeks": persistent.cheeks,
                "l_pupil": persistent.l_pupil,
                "r_pupil": persistent.r_pupil,
                "eyebrows": persistent.eyebrows,
                "wrinkles": persistent.wrinkles,
                "hair_style": persistent.hair_style,
                "beard": persistent.beard,
                "wear": persistent.wear,
                "underwear": persistent.underwear
            }
            
            # Save to persistent data
            if not hasattr(persistent, 'saved_appearances'):
                persistent.saved_appearances = []
            
            persistent.saved_appearances.append(appearance_data)
            renpy.notify("Appearance saved successfully!")
            return True
        except Exception as e:
            renpy.notify("Error saving appearance: " + str(e))
            return False
    
    def import_appearance_from_preset(preset_index):
        """Import appearance from a saved preset"""
        try:
            if not hasattr(persistent, 'saved_appearances'):
                persistent.saved_appearances = []
                return False
            
            if preset_index >= len(persistent.saved_appearances):
                return False
            
            appearance_data = persistent.saved_appearances[preset_index]
            
            # Apply all appearance settings
            for key, value in appearance_data.items():
                if key not in ['name', 'title']:
                    setattr(persistent, key, value)
            
            renpy.notify("Appearance loaded!")
            renpy.restart_interaction()
            return True
        except Exception as e:
            renpy.notify("Error loading appearance: " + str(e))
            return False
    
    def delete_appearance_preset(preset_index):
        """Delete a saved appearance preset"""
        try:
            if hasattr(persistent, 'saved_appearances') and preset_index < len(persistent.saved_appearances):
                del persistent.saved_appearances[preset_index]
                renpy.notify("Preset deleted")
                renpy.restart_interaction()
                return True
            return False
        except Exception as e:
            renpy.notify("Error deleting preset: " + str(e))
            return False


screen saved_appearances_manager():
    modal True
    
    add Solid("#000000aa")
    
    frame:
        xalign 0.5
        yalign 0.5
        xsize 700
        ysize 600
        padding (30, 30)
        
        vbox:
            spacing 15
            
            text "Saved Appearances" size 32 xalign 0.5 color "#ffffff"
            
            null height 10
            
            viewport:
                scrollbars "vertical"
                mousewheel True
                ysize 450
                
                vbox:
                    spacing 10
                    
                    if not hasattr(persistent, 'saved_appearances') or not persistent.saved_appearances:
                        text "No saved appearances yet" xalign 0.5 color "#888888" size 20
                    else:
                        for i, preset in enumerate(persistent.saved_appearances):
                            frame:
                                background "#00000099"
                                padding (15, 15)
                                xfill True
                                
                                hbox:
                                    spacing 15
                                    
                                    vbox:
                                        spacing 5
                                        xsize 450
                                        
                                        text "[preset.get('name', 'Unknown')] - [preset.get('title', 'Knyaz')]":
                                            size 22
                                            color "#ffffff"
                                        
                                        text "Age: [preset.get('age', 'N/A')] | Body: [preset.get('body', 'N/A')]":
                                            size 16
                                            color "#c0c0c0"
                                        
                                        text "Hair: [preset.get('hair_style', 'N/A')] | Outfit: [preset.get('wear', 'N/A')]":
                                            size 16
                                            color "#c0c0c0"
                                    
                                    vbox:
                                        spacing 5
                                        
                                        textbutton "Load":
                                            xsize 100
                                            action Function(import_appearance_from_preset, i)
                                        
                                        textbutton "Delete":
                                            xsize 100
                                            action Function(delete_appearance_preset, i)
            
            hbox:
                spacing 20
                xalign 0.5
                
                textbutton "Save Current":
                    xsize 200
                    action Function(export_appearance_to_file)
                
                textbutton "Close":
                    xsize 200
                    action Hide("saved_appearances_manager")

