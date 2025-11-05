## Game Systems - Time and Room Management
## This file contains the time system and all room actions

################################################################################
## Initialization - Call this from your main script
################################################################################

# Add this label to start the room-based gameplay
# Call it with: jump start_room_system
label start_room_system:
    $ current_room = "bedroom"
    $ game_time = GameTime()
    $ cat_tamed = False
    $ cat_fed_today = False
    $ cat_location = None
    $ has_prayed_today = False
    $ soldiers_available = 50
    $ scouting_party_sent = False
    $ reception_held_today = False
    $ partner_available = False
    $ partner_name = ""
    $ relationship_points = 0
    
    jump room_bedroom

################################################################################
## Time System
################################################################################

init python:
    class GameTime:
        def __init__(self):
            self.hour = 8
            self.minute = 0
            self.day = 1
            self.season = "Winter"
            self.day_names = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
            self.current_day_name = self.day_names[0]
            
        def advance_time(self, hours=0, minutes=0):
            """Advance time by specified hours and minutes"""
            self.minute += minutes
            if self.minute >= 60:
                self.hour += self.minute // 60
                self.minute = self.minute % 60
            
            self.hour += hours
            if self.hour >= 24:
                self.day += self.hour // 24
                self.hour = self.hour % 24
                # Update day name
                day_index = (self.day - 1) % 7
                self.current_day_name = self.day_names[day_index]
        
        def get_time_string(self):
            """Return formatted time string"""
            period = "AM" if self.hour < 12 else "PM"
            display_hour = self.hour if self.hour <= 12 else self.hour - 12
            if display_hour == 0:
                display_hour = 12
            return "{:02d}:{:02d} {}".format(display_hour, self.minute, period)
        
        def get_time_of_day(self):
            """Return time of day description"""
            if 5 <= self.hour < 12:
                return "Morning"
            elif 12 <= self.hour < 17:
                return "Afternoon"
            elif 17 <= self.hour < 21:
                return "Evening"
            else:
                return "Night"
        
        def is_breakfast_time(self):
            return self.hour <= 9
        
        def is_lunch_time(self):
            return 13 <= self.hour <= 15
        
        def is_dinner_time(self):
            return 18 <= self.hour <= 20

    # Initialize game time
    game_time = GameTime()

# Game state variables
default cat_tamed = False
default cat_fed_today = False
default cat_location = None  # None, "garden", "bedroom", etc.
default has_prayed_today = False
default current_room = "bedroom"
default soldiers_available = 50
default scouting_party_sent = False
default reception_held_today = False

# Relationship variables
default partner_available = False
default partner_name = ""
default relationship_points = 0

################################################################################
## Action Menu Screen (Bottom Right Corner)
################################################################################

screen action_menu():
    frame:
        xalign 1.0
        yalign 1.0
        xoffset -10
        yoffset -80
        xsize 320
        ysize 600
        background "#000000cc"
        padding (15, 15)
        
        vbox:
            spacing 8
            
            # Time display
            frame:
                background "#00000099"
                padding (10, 8)
                xfill True
                
                vbox:
                    spacing 5
                    text "[game_time.current_day_name], Day [game_time.day]" size 18 color "#ffffff" xalign 0.5
                    text "[game_time.get_time_string()]" size 22 color "#ffcc00" xalign 0.5 bold True
                    text "[game_time.get_time_of_day()]" size 16 color "#aaaaaa" xalign 0.5
            
            null height 5
            
            # Current location
            text "Location: [current_room!t]" size 18 color "#ffffff"
            
            null height 5
            
            # Scrollable actions viewport
            viewport:
                mousewheel True
                scrollbars "vertical"
                ysize 430
                
                vbox:
                    spacing 5
                    
                    # Room-specific actions
                    if current_room == "palace_walls":
                        use palace_walls_actions
                    elif current_room == "bedroom":
                        use bedroom_actions
                    elif current_room == "cabinet":
                        use cabinet_actions
                    elif current_room == "refectory":
                        use refectory_actions
                    elif current_room == "prison":
                        use prison_actions
                    elif current_room == "map_room":
                        use map_room_actions
                    elif current_room == "throne_room":
                        use throne_room_actions
                    elif current_room == "garden":
                        use garden_actions
                    elif current_room == "watchtower":
                        use watchtower_actions

################################################################################
## Room Action Screens
################################################################################

screen palace_walls_actions():
    vbox:
        spacing 5
        
        text "Palace Walls" size 20 color "#ffcc00" underline True
        
        textbutton "Gaze at Horizon" action Jump("palace_walls_horizon")
        textbutton "Speak with Guard" action Jump("palace_walls_guard")
        textbutton "Search for Cats" action Jump("palace_walls_find_cat")
        textbutton "Inspect Fortifications" action Jump("palace_walls_fortifications")
        textbutton "Watch the Sunset" action Jump("palace_walls_sunset") sensitive (17 <= game_time.hour <= 19)
        textbutton "Training Grounds" action Jump("palace_walls_training")
        textbutton "Check Defenses" action Jump("palace_walls_defenses")

screen bedroom_actions():
    vbox:
        spacing 5
        
        text "Bedroom" size 20 color "#ffcc00" underline True
        
        textbutton "Sleep" action Jump("bedroom_sleep")
        textbutton "Pray" action Jump("bedroom_pray") sensitive (not has_prayed_today)
        textbutton "Talk to Partner" action Jump("bedroom_partner") sensitive partner_available
        textbutton "Father's Portrait" action Jump("bedroom_portrait")
        textbutton "Play with Cat" action Jump("bedroom_cat") sensitive (cat_tamed and cat_location == "bedroom")
        textbutton "Look out Window" action Jump("bedroom_window")
        textbutton "Mirror Reflection" action Jump("bedroom_mirror")
        textbutton "Read Personal Journal" action Jump("bedroom_journal")
        textbutton "Organize Wardrobe" action Jump("bedroom_wardrobe")
        textbutton "Rest on Bed" action Jump("bedroom_rest")

screen cabinet_actions():
    vbox:
        spacing 5
        
        text "Cabinet" size 20 color "#ffcc00" underline True
        
        textbutton "Write Letter" action Jump("cabinet_letter")
        textbutton "Read Book" action Jump("cabinet_read")
        textbutton "Look out Window" action Jump("cabinet_window")
        textbutton "Review Documents" action Jump("cabinet_documents")
        textbutton "Study Maps" action Jump("cabinet_maps")
        textbutton "Write in Journal" action Jump("cabinet_journal")
        textbutton "Practice Calligraphy" action Jump("cabinet_calligraphy")
        textbutton "Examine Heirlooms" action Jump("cabinet_heirlooms")

screen refectory_actions():
    vbox:
        spacing 5
        
        text "Refectory" size 20 color "#ffcc00" underline True
        
        textbutton "Have Breakfast" action Jump("refectory_breakfast") sensitive game_time.is_breakfast_time()
        textbutton "Have Lunch" action Jump("refectory_lunch") sensitive game_time.is_lunch_time()
        textbutton "Have Dinner" action Jump("refectory_dinner") sensitive game_time.is_dinner_time()
        textbutton "Speak to Cook" action Jump("refectory_cook")
        textbutton "Check Supplies" action Jump("refectory_supplies")
        textbutton "Sample Wine" action Jump("refectory_wine")
        textbutton "Inspect Kitchen" action Jump("refectory_kitchen")
        textbutton "Taste Dishes" action Jump("refectory_taste")

screen prison_actions():
    vbox:
        spacing 5
        
        text "Prison" size 20 color "#ffcc00" underline True
        
        textbutton "Speak with Prisoners" action Jump("prison_prisoners")
        textbutton "Speak with Guard" action Jump("prison_guard")
        textbutton "Inspect Cells" action Jump("prison_inspect")
        textbutton "Review Cases" action Jump("prison_cases")
        textbutton "Check Conditions" action Jump("prison_conditions")
        textbutton "Interview Suspects" action Jump("prison_interview")
        textbutton "Pardon a Prisoner" action Jump("prison_pardon")

screen map_room_actions():
    vbox:
        spacing 5
        
        text "Map Room" size 20 color "#ffcc00" underline True
        
        textbutton "View Territory Map" action Jump("map_room_territory")
        textbutton "Send Scouting Party" action Jump("map_room_scout") sensitive (soldiers_available >= 15 and not scouting_party_sent)
        textbutton "Diplomacy" action Jump("map_room_diplomacy")
        textbutton "Study Geography" action Jump("map_room_geography")
        textbutton "Plan Campaign" action Jump("map_room_campaign")
        textbutton "Trade Routes" action Jump("map_room_trade")
        textbutton "Review Intelligence" action Jump("map_room_intelligence")
        textbutton "Send Messenger" action Jump("map_room_messenger")

screen throne_room_actions():
    vbox:
        spacing 5
        
        text "Throne Room" size 20 color "#ffcc00" underline True
        
        textbutton "Hold Reception" action Jump("throne_room_reception") sensitive (not reception_held_today)
        textbutton "Hear Petitions" action Jump("throne_room_petitions")
        textbutton "Meet Advisors" action Jump("throne_room_advisors")
        textbutton "Review Treasury" action Jump("throne_room_treasury")
        textbutton "Inspect Throne" action Jump("throne_room_throne")
        textbutton "Address Court" action Jump("throne_room_address")
        textbutton "Sign Decrees" action Jump("throne_room_decrees")

screen garden_actions():
    vbox:
        spacing 5
        
        text "Garden" size 20 color "#ffcc00" underline True
        
        if persistent.player_title == "Knyaz":
            textbutton "Speak to Sisters" action Jump("garden_sisters")
        else:
            textbutton "Speak to Siblings" action Jump("garden_siblings")
        
        textbutton "Play with Cat" action Jump("garden_cat_play") sensitive (cat_tamed and cat_location == "garden")
        textbutton "Feed the Cat" action Jump("garden_cat_feed") sensitive (cat_tamed and not cat_fed_today)
        textbutton "Tend to Flowers" action Jump("garden_flowers")
        textbutton "Walk the Paths" action Jump("garden_walk")
        textbutton "Sit by Fountain" action Jump("garden_fountain")
        textbutton "Pick Herbs" action Jump("garden_herbs")
        textbutton "Meditation" action Jump("garden_meditation")

screen watchtower_actions():
    vbox:
        spacing 5
        
        text "Watchtower" size 20 color "#ffcc00" underline True
        
        textbutton "Gaze at Horizon" action Jump("watchtower_horizon")
        textbutton "Speak with Watchman" action Jump("watchtower_watchman")
        textbutton "Survey Lands" action Jump("watchtower_survey")
        textbutton "Check for Threats" action Jump("watchtower_threats")
        textbutton "Observe Stars" action Jump("watchtower_stars") sensitive (game_time.hour >= 21 or game_time.hour <= 5)
        textbutton "Signal Practice" action Jump("watchtower_signals")
        textbutton "Enjoy the View" action Jump("watchtower_view")

################################################################################
## Navigation Screen
################################################################################

screen room_navigation():
    frame:
        xalign 0.0
        yalign 0.5
        xoffset 20
        background "#000000cc"
        padding (15, 15)
        
        vbox:
            spacing 8
            
            text "Navigate" size 20 color "#ffcc00" underline True
            
            textbutton "Palace Walls" action [SetVariable("current_room", "palace_walls"), Jump("room_palace_walls")]
            textbutton "Bedroom" action [SetVariable("current_room", "bedroom"), Jump("room_bedroom")]
            textbutton "Cabinet" action [SetVariable("current_room", "cabinet"), Jump("room_cabinet")]
            textbutton "Refectory" action [SetVariable("current_room", "refectory"), Jump("room_refectory")]
            textbutton "Prison" action [SetVariable("current_room", "prison"), Jump("room_prison")]
            textbutton "Map Room" action [SetVariable("current_room", "map_room"), Jump("room_map_room")]
            textbutton "Throne Room" action [SetVariable("current_room", "throne_room"), Jump("room_throne_room")]
            textbutton "Garden" action [SetVariable("current_room", "garden"), Jump("room_garden")]
            textbutton "Watchtower" action [SetVariable("current_room", "watchtower"), Jump("room_watchtower")]

################################################################################
## Room Description Labels
################################################################################

label room_palace_walls:
    scene bg palace_walls
    show screen action_menu
    show screen room_navigation
    
    "You stand atop the palace walls, the cold wind biting at your face. The view stretches far across your domain."
    
    jump palace_walls_main

label palace_walls_main:
    show screen action_menu
    show screen room_navigation
    pause
    jump palace_walls_main

label room_bedroom:
    scene bg bedroom
    show screen action_menu
    show screen room_navigation
    
    "Your private chambers offer a moment of respite from the duties of rule."
    
    jump bedroom_main

label bedroom_main:
    show screen action_menu
    show screen room_navigation
    pause
    jump bedroom_main

label room_cabinet:
    scene bg cabinet
    show screen action_menu
    show screen room_navigation
    
    "Your private study, filled with books, documents, and the tools of governance."
    
    jump cabinet_main

label cabinet_main:
    show screen action_menu
    show screen room_navigation
    pause
    jump cabinet_main

label room_refectory:
    scene bg refectory
    show screen action_menu
    show screen room_navigation
    
    "The smell of cooking fills the air in the palace refectory."
    
    jump refectory_main

label refectory_main:
    show screen action_menu
    show screen room_navigation
    pause
    jump refectory_main

label room_prison:
    scene bg prison
    show screen action_menu
    show screen room_navigation
    
    "The dank cells beneath the palace hold those who have broken your laws."
    
    jump prison_main

label prison_main:
    show screen action_menu
    show screen room_navigation
    pause
    jump prison_main

label room_map_room:
    scene bg map_room
    show screen action_menu
    show screen room_navigation
    
    "Maps and strategic documents cover every surface in this chamber of war and diplomacy."
    
    jump map_room_main

label map_room_main:
    show screen action_menu
    show screen room_navigation
    pause
    jump map_room_main

label room_throne_room:
    scene bg throne_room
    show screen action_menu
    show screen room_navigation
    
    "The grand throne room, where you dispense justice and receive petitioners."
    
    jump throne_room_main

label throne_room_main:
    show screen action_menu
    show screen room_navigation
    pause
    jump throne_room_main

label room_garden:
    scene bg garden
    show screen action_menu
    show screen room_navigation
    
    "The palace garden offers peace and beauty amidst the harsh winter."
    
    jump garden_main

label garden_main:
    show screen action_menu
    show screen room_navigation
    pause
    jump garden_main

label room_watchtower:
    scene bg watchtower
    show screen action_menu
    show screen room_navigation
    
    "From the highest tower, you can see everything that approaches your domain."
    
    jump watchtower_main

label watchtower_main:
    show screen action_menu
    show screen room_navigation
    pause
    jump watchtower_main

################################################################################
## Action Implementations - Palace Walls
################################################################################

label palace_walls_horizon:
    hide screen room_navigation
    $ game_time.advance_time(minutes=15)
    
    narrator "You stand at the battlements and gaze out across your lands. The snow-covered fields stretch endlessly toward the horizon."
    
    show screen room_navigation
    jump palace_walls_main

label palace_walls_guard:
    hide screen room_navigation
    $ game_time.advance_time(minutes=30)
    
    "Guard" "My [persistent.player_title], all is quiet on the walls."
    narrator "You discuss the state of the defenses with the guard captain."
    
    show screen room_navigation
    jump palace_walls_main

label palace_walls_find_cat:
    hide screen room_navigation
    $ game_time.advance_time(hours=1)
    
    if not cat_tamed:
        narrator "You search the nooks and crannies of the palace walls."
        narrator "A small tabby cat peers out from behind a barrel, watching you warily."
        
        menu:
            "Approach slowly":
                narrator "You kneel down and extend your hand. After a moment, the cat sniffs your fingers."
                $ cat_tamed = True
                $ cat_location = "palace_walls"
                narrator "The cat seems to have warmed to you!"
            
            "Leave it alone":
                narrator "You decide not to disturb the creature."
    else:
        narrator "You've already befriended the palace cat."
    
    show screen room_navigation
    jump palace_walls_main

label palace_walls_fortifications:
    hide screen room_navigation
    $ game_time.advance_time(minutes=45)
    
    narrator "You inspect the stone walls and battlements. The fortifications appear solid, though some areas could use repairs before spring."
    
    show screen room_navigation
    jump palace_walls_main

label palace_walls_sunset:
    hide screen room_navigation
    $ game_time.advance_time(minutes=20)
    
    narrator "The setting sun paints the sky in brilliant oranges and purples. For a moment, you forget the weight of your responsibilities."
    
    show screen room_navigation
    jump palace_walls_main

label palace_walls_training:
    hide screen room_navigation
    $ game_time.advance_time(hours=1)
    
    narrator "You watch soldiers drilling below. Their discipline speaks well of your military readiness."
    
    show screen room_navigation
    jump palace_walls_main

label palace_walls_defenses:
    hide screen room_navigation
    $ game_time.advance_time(minutes=45)
    
    narrator "You review the defensive positions with your officers. Everything appears in order."
    
    show screen room_navigation
    jump palace_walls_main

################################################################################
## Action Implementations - Bedroom
################################################################################

# Bedroom actions are now defined in bedroom_backgrounds.rpy with enhanced visuals
# This section is intentionally left empty to avoid label conflicts

################################################################################
## Action Implementations - Cabinet
################################################################################

label cabinet_letter:
    hide screen room_navigation
    $ game_time.advance_time(hours=1)
    
    narrator "You compose a letter, carefully choosing each word to convey your intentions to distant allies or rivals."
    
    show screen room_navigation
    jump cabinet_main

label cabinet_read:
    hide screen room_navigation
    $ game_time.advance_time(hours=2)
    
    narrator "You lose yourself in a tome from the library, expanding your knowledge of history and statecraft."
    
    show screen room_navigation
    jump cabinet_main

label cabinet_window:
    hide screen room_navigation
    $ game_time.advance_time(minutes=10)
    
    narrator "You peer through the window at the courtyard below, watching servants go about their duties."
    
    show screen room_navigation
    jump cabinet_main

label cabinet_documents:
    hide screen room_navigation
    $ game_time.advance_time(hours=1)
    
    narrator "You review important documents requiring your attention - tax records, petitions, and reports from your officials."
    
    show screen room_navigation
    jump cabinet_main

label cabinet_maps:
    hide screen room_navigation
    $ game_time.advance_time(minutes=45)
    
    narrator "You study geographical maps, memorizing the terrain and features of your realm."
    
    show screen room_navigation
    jump cabinet_main

label cabinet_journal:
    hide screen room_navigation
    $ game_time.advance_time(minutes=30)
    
    narrator "You write in your private journal, recording the events and your thoughts on recent decisions."
    
    show screen room_navigation
    jump cabinet_main

label cabinet_calligraphy:
    hide screen room_navigation
    $ game_time.advance_time(hours=1)
    
    narrator "You practice your calligraphy, a skill befitting a ruler who must sign many important documents."
    
    show screen room_navigation
    jump cabinet_main

label cabinet_heirlooms:
    hide screen room_navigation
    $ game_time.advance_time(minutes=20)
    
    narrator "You examine the family heirlooms displayed in your cabinet - each one a reminder of your lineage."
    
    show screen room_navigation
    jump cabinet_main

################################################################################
## Action Implementations - Refectory
################################################################################

label refectory_breakfast:
    hide screen room_navigation
    $ game_time.advance_time(hours=1)
    
    narrator "You break your fast with bread, porridge, and preserved fruits. The meal is simple but hearty."
    
    show screen room_navigation
    jump refectory_main

label refectory_lunch:
    hide screen room_navigation
    $ game_time.advance_time(hours=1)
    
    narrator "The midday meal consists of roasted meat, vegetables, and fresh bread from the palace ovens."
    
    show screen room_navigation
    jump refectory_main

label refectory_dinner:
    hide screen room_navigation
    $ game_time.advance_time(hours=1, minutes=30)
    
    narrator "Dinner is the grandest meal of the day - multiple courses including fish, meat, and sweet confections."
    
    show screen room_navigation
    jump refectory_main

label refectory_cook:
    hide screen room_navigation
    $ game_time.advance_time(minutes=30)
    
    "Cook" "My [persistent.player_title]! The kitchens are at your service. Is there anything special you'd like prepared?"
    narrator "You discuss menu planning and the state of the palace food stores."
    
    show screen room_navigation
    jump refectory_main

label refectory_supplies:
    hide screen room_navigation
    $ game_time.advance_time(minutes=45)
    
    narrator "You inspect the larder and storage rooms. The winter stores appear adequate, though spring cannot come soon enough."
    
    show screen room_navigation
    jump refectory_main

label refectory_wine:
    hide screen room_navigation
    $ game_time.advance_time(minutes=20)
    
    narrator "You sample wines from the palace cellars, ensuring only the finest are served at your table."
    
    show screen room_navigation
    jump refectory_main

label refectory_kitchen:
    hide screen room_navigation
    $ game_time.advance_time(minutes=30)
    
    narrator "You tour the kitchens, observing the staff at work. The heat from the ovens is a welcome respite from winter's chill."
    
    show screen room_navigation
    jump refectory_main

label refectory_taste:
    hide screen room_navigation
    $ game_time.advance_time(minutes=15)
    
    narrator "You taste several dishes being prepared. The palace cook maintains high standards."
    
    show screen room_navigation
    jump refectory_main

################################################################################
## Action Implementations - Prison
################################################################################

label prison_prisoners:
    hide screen room_navigation
    $ game_time.advance_time(hours=1)
    
    narrator "You speak with the prisoners, hearing their pleas and stories. Justice must be tempered with mercy."
    
    show screen room_navigation
    jump prison_main

label prison_guard:
    hide screen room_navigation
    $ game_time.advance_time(minutes=30)
    
    "Prison Guard" "The prisoners are secure, my [persistent.player_title]. No incidents to report."
    
    show screen room_navigation
    jump prison_main

label prison_inspect:
    hide screen room_navigation
    $ game_time.advance_time(minutes=45)
    
    narrator "You inspect the cells, ensuring they are secure but not inhumane."
    
    show screen room_navigation
    jump prison_main

label prison_cases:
    hide screen room_navigation
    $ game_time.advance_time(hours=1)
    
    narrator "You review the cases of those imprisoned, considering their crimes and sentences."
    
    show screen room_navigation
    jump prison_main

label prison_conditions:
    hide screen room_navigation
    $ game_time.advance_time(minutes=30)
    
    narrator "You check the conditions of imprisonment - even criminals deserve basic humanity."
    
    show screen room_navigation
    jump prison_main

label prison_interview:
    hide screen room_navigation
    $ game_time.advance_time(hours=1)
    
    narrator "You conduct private interviews with suspects, seeking the truth behind their alleged crimes."
    
    show screen room_navigation
    jump prison_main

label prison_pardon:
    hide screen room_navigation
    $ game_time.advance_time(minutes=30)
    
    narrator "After careful consideration, you grant pardon to a prisoner who has shown genuine remorse."
    
    show screen room_navigation
    jump prison_main

################################################################################
## Action Implementations - Map Room
################################################################################

label map_room_territory:
    hide screen room_navigation
    $ game_time.advance_time(minutes=30)
    
    narrator "You study the maps of Western Sibara, noting the positions of rival knyazhestvas and potential threats."
    
    show screen room_navigation
    jump map_room_main

label map_room_scout:
    hide screen room_navigation
    $ game_time.advance_time(hours=1)
    $ scouting_party_sent = True
    
    python:
        import random
        scouts = random.randint(10, 20)
        soldiers_available -= scouts
    
    narrator "You dispatch a scouting party of [scouts] men to reconnoiter the borderlands."
    narrator "They will return with intelligence in a few days."
    
    show screen room_navigation
    jump map_room_main

label map_room_diplomacy:
    hide screen room_navigation
    $ game_time.advance_time(hours=2)
    
    narrator "You review diplomatic correspondence and consider which neighboring knyazhestvas might be amenable to alliance."
    
    show screen room_navigation
    jump map_room_main

label map_room_geography:
    hide screen room_navigation
    $ game_time.advance_time(hours=1)
    
    narrator "You study the geography of the region, learning the rivers, mountains, and forests that define these lands."
    
    show screen room_navigation
    jump map_room_main

label map_room_campaign:
    hide screen room_navigation
    $ game_time.advance_time(hours=2)
    
    narrator "You plan military campaigns with your advisors, considering various strategic options."
    
    show screen room_navigation
    jump map_room_main

label map_room_trade:
    hide screen room_navigation
    $ game_time.advance_time(hours=1)
    
    narrator "You examine trade routes and consider how to increase commerce in your realm."
    
    show screen room_navigation
    jump map_room_main

label map_room_intelligence:
    hide screen room_navigation
    $ game_time.advance_time(hours=1)
    
    narrator "You review intelligence reports from spies and informants across Western Sibara."
    
    show screen room_navigation
    jump map_room_main

label map_room_messenger:
    hide screen room_navigation
    $ game_time.advance_time(minutes=45)
    
    narrator "You compose messages to be carried by swift riders to neighboring rulers."
    
    show screen room_navigation
    jump map_room_main

################################################################################
## Action Implementations - Throne Room
################################################################################

label throne_room_reception:
    hide screen room_navigation
    $ game_time.advance_time(hours=3)
    $ reception_held_today = True
    
    narrator "You hold court, receiving nobles and officials who have business with the throne."
    narrator "Hours pass as you dispense justice and hear petitions."
    
    show screen room_navigation
    jump throne_room_main

label throne_room_petitions:
    hide screen room_navigation
    $ game_time.advance_time(hours=2)
    
    narrator "Common folk bring their petitions and grievances before you. You listen to each carefully."
    
    show screen room_navigation
    jump throne_room_main

label throne_room_advisors:
    hide screen room_navigation
    $ game_time.advance_time(hours=1)
    
    narrator "Your advisors gather to discuss matters of state - military, economic, and political."
    
    show screen room_navigation
    jump throne_room_main

label throne_room_treasury:
    hide screen room_navigation
    $ game_time.advance_time(hours=1)
    
    narrator "You review the treasury accounts with your steward. Every silver coin must be accounted for."
    
    show screen room_navigation
    jump throne_room_main

label throne_room_throne:
    hide screen room_navigation
    $ game_time.advance_time(minutes=10)
    
    narrator "You sit upon the throne, feeling the weight of authority it represents. Many generations of your family have sat here."
    
    show screen room_navigation
    jump throne_room_main

label throne_room_address:
    hide screen room_navigation
    $ game_time.advance_time(hours=1)
    
    narrator "You address the assembled court, speaking on matters of importance to your realm."
    
    show screen room_navigation
    jump throne_room_main

label throne_room_decrees:
    hide screen room_navigation
    $ game_time.advance_time(hours=1)
    
    narrator "You review and sign official decrees, each one bearing your seal and authority."
    
    show screen room_navigation
    jump throne_room_main

################################################################################
## Action Implementations - Garden
################################################################################

label garden_sisters:
    hide screen room_navigation
    $ game_time.advance_time(hours=1)
    
    narrator "You walk with your sisters through the snow-covered garden paths, discussing family matters."
    
    show screen room_navigation
    jump garden_main

label garden_siblings:
    hide screen room_navigation
    $ game_time.advance_time(hours=1)
    
    narrator "You spend time with your siblings, enjoying their company away from the formality of court."
    
    show screen room_navigation
    jump garden_main

label garden_cat_play:
    hide screen room_navigation
    $ game_time.advance_time(minutes=30)
    
    narrator "You play with the cat in the garden. It chases leaves blown by the winter wind."
    
    show screen room_navigation
    jump garden_main

label garden_cat_feed:
    hide screen room_navigation
    $ game_time.advance_time(minutes=15)
    $ cat_fed_today = True
    
    narrator "You feed the cat scraps from the kitchen. It purrs contentedly."
    
    show screen room_navigation
    jump garden_main

label garden_flowers:
    hide screen room_navigation
    $ game_time.advance_time(minutes=45)
    
    narrator "You tend to the hardy winter flowers that somehow bloom despite the cold."
    
    show screen room_navigation
    jump garden_main

label garden_walk:
    hide screen room_navigation
    $ game_time.advance_time(minutes=30)
    
    narrator "You walk the garden paths, finding peace in the quiet beauty of nature."
    
    show screen room_navigation
    jump garden_main

label garden_fountain:
    hide screen room_navigation
    $ game_time.advance_time(minutes=20)
    
    narrator "You sit by the frozen fountain, watching icicles sparkle in the winter sun."
    
    show screen room_navigation
    jump garden_main

label garden_herbs:
    hide screen room_navigation
    $ game_time.advance_time(minutes=30)
    
    narrator "You gather herbs from the garden - some for cooking, others for medicine."
    
    show screen room_navigation
    jump garden_main

label garden_meditation:
    hide screen room_navigation
    $ game_time.advance_time(minutes=45)
    
    narrator "You find a quiet spot and meditate, clearing your mind of worries and concerns."
    
    show screen room_navigation
    jump garden_main

################################################################################
## Action Implementations - Watchtower
################################################################################

label watchtower_horizon:
    hide screen room_navigation
    $ game_time.advance_time(minutes=20)
    
    narrator "From this height, you can see for miles. Your domain stretches before you, vast and demanding."
    
    show screen room_navigation
    jump watchtower_main

label watchtower_watchman:
    hide screen room_navigation
    $ game_time.advance_time(minutes=30)
    
    "Watchman" "All quiet, my [persistent.player_title]. No signs of trouble on the roads."
    
    show screen room_navigation
    jump watchtower_main

label watchtower_survey:
    hide screen room_navigation
    $ game_time.advance_time(minutes=45)
    
    narrator "You use a spyglass to survey your lands, noting activity in the villages and on the roads."
    
    show screen room_navigation
    jump watchtower_main

label watchtower_threats:
    hide screen room_navigation
    $ game_time.advance_time(minutes=30)
    
    narrator "You scan the horizon for potential threats - bandits, rival forces, or other dangers."
    
    show screen room_navigation
    jump watchtower_main

label watchtower_stars:
    hide screen room_navigation
    $ game_time.advance_time(minutes=30)
    
    narrator "The night sky is clear and filled with countless stars. You pick out familiar constellations."
    
    show screen room_navigation
    jump watchtower_main

label watchtower_signals:
    hide screen room_navigation
    $ game_time.advance_time(minutes=45)
    
    narrator "You practice signal codes with the watch - essential for rapid communication across your domain."
    
    show screen room_navigation
    jump watchtower_main

label watchtower_view:
    hide screen room_navigation
    $ game_time.advance_time(minutes=15)
    
    narrator "You simply stand and enjoy the magnificent view from the highest point in your palace."
    
    show screen room_navigation
    jump watchtower_main
