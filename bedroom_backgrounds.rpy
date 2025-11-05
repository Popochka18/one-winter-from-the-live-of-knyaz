## Action Backgrounds - Bedroom Scene Definitions
## This file defines background images for specific actions in the bedroom

################################################################################
## Bedroom Action Backgrounds
################################################################################

# Sleep action
image bg bedroom_sleep = "images/backgrounds/bedroom_sleep.jpg"

# Prayer action
image bg bedroom_pray = "images/backgrounds/bedroom_pray.jpg"

# Partner conversation action
image bg bedroom_partner = "images/backgrounds/bedroom_partner.jpg"

# Father's portrait action
image bg bedroom_portrait = "images/backgrounds/bedroom_portrait.jpg"

# Playing with cat action
image bg bedroom_cat = "images/backgrounds/bedroom_cat.jpg"

# Window view action
image bg bedroom_window = "images/backgrounds/bedroom_window.jpg"

# Mirror reflection action
image bg bedroom_mirror = "images/backgrounds/bedroom_mirror.jpg"

# Journal reading/writing action
image bg bedroom_journal = "images/backgrounds/bedroom_journal.jpg"

# Wardrobe organizing action
image bg bedroom_wardrobe = "images/backgrounds/bedroom_wardrobe.jpg"

# Resting on bed action
image bg bedroom_rest = "images/backgrounds/bedroom_rest.jpg"

################################################################################
## Enhanced Bedroom Actions with Background Changes
################################################################################

# These labels override the ones in game_systems.rpy with enhanced visuals

label bedroom_sleep:
    hide screen room_navigation
    hide screen action_menu
    
    scene bg bedroom_sleep with fade
    
    narrator "You retire to bed, letting sleep claim you."
    
    scene black with fade
    pause 1.0
    
    $ game_time.hour = 8
    $ game_time.minute = 0
    $ game_time.day += 1
    $ has_prayed_today = False
    $ cat_fed_today = False
    $ scouting_party_sent = False
    $ reception_held_today = False
    
    # Update day name
    python:
        day_index = (game_time.day - 1) % 7
        game_time.current_day_name = game_time.day_names[day_index]
    
    scene bg bedroom with fade
    narrator "You wake refreshed as morning light filters through your window."
    
    show screen room_navigation
    show screen action_menu
    jump bedroom_main

label bedroom_pray:
    hide screen room_navigation
    
    scene bg bedroom_pray with fade
    $ game_time.advance_time(minutes=30)
    $ has_prayed_today = True
    
    narrator "You kneel before the icon in your chamber, the candlelight flickering across the gilded surface."
    narrator "You offer prayers for wisdom and strength to guide your people through these dark times."
    
    menu:
        "Pray for your people's well-being":
            narrator "You pray for the health and prosperity of your subjects."
            narrator "May they endure this harsh winter."
            
        "Pray for strength in leadership":
            narrator "You ask for the wisdom to make difficult decisions."
            narrator "The weight of the crown is heavy indeed."
            
        "Pray for your father's soul":
            narrator "You remember your father and pray for his eternal rest."
            narrator "His legacy weighs upon you."
    
    narrator "You feel a sense of peace as you finish your prayers."
    
    scene bg bedroom with fade
    show screen room_navigation
    jump bedroom_main

label bedroom_partner:
    hide screen room_navigation
    
    scene bg bedroom_partner with fade
    $ game_time.advance_time(minutes=45)
    
    narrator "You spend intimate time with [partner_name], discussing the affairs of the day."
    
    menu:
        "Discuss your worries":
            player "Sometimes I fear I'm not strong enough for this."
            narrator "[partner_name] takes your hand reassuringly."
            narrator "Their support means more than they know."
            $ relationship_points += 5
            
        "Share your hopes":
            player "When spring comes, things will be better. I promise you."
            narrator "[partner_name] smiles, though there's worry in their eyes."
            $ relationship_points += 3
            
        "Simply enjoy their company":
            narrator "You sit together in comfortable silence, finding solace in each other's presence."
            narrator "These quiet moments are rare and precious."
            $ relationship_points += 7
    
    scene bg bedroom with fade
    show screen room_navigation
    jump bedroom_main

label bedroom_portrait:
    hide screen room_navigation
    
    scene bg bedroom_portrait with fade
    $ game_time.advance_time(minutes=15)
    
    narrator "You stand before the portrait of your father, studying his stern features."
    narrator "The artist captured him perfectly - proud, strong, unyielding."
    
    menu:
        "Seek his guidance":
            player "Father... what would you do in my place?"
            narrator "The painted eyes seem to judge you. He never had easy answers."
            narrator "But perhaps that's the lesson - there are no easy answers."
            
        "Promise to honor his legacy":
            player "I will not fail our house. I swear it."
            narrator "The vow hangs in the air. You hope you can keep it."
            
        "Question his choices":
            narrator "Your father made many difficult decisions. Not all of them wise."
            narrator "You wonder if you're doomed to repeat his mistakes... or if you can do better."
    
    narrator "You turn away from the portrait, returning to the present."
    
    scene bg bedroom with fade
    show screen room_navigation
    jump bedroom_main

label bedroom_cat:
    hide screen room_navigation
    
    scene bg bedroom_cat with fade
    $ game_time.advance_time(minutes=30)
    
    narrator "The cat is curled up on your bed, watching you with lazy eyes."
    narrator "You dangle a ribbon, and it suddenly springs to life."
    
    narrator "The cat pounces and tumbles, chasing the ribbon with fierce determination."
    narrator "For these few minutes, you forget about tribute payments, food shortages, and political intrigue."
    narrator "There is only you, the cat, and this simple game."
    
    narrator "The cat finally tires and curls up in your lap, purring contentedly."
    narrator "Its warmth and trust bring a rare smile to your face."
    
    scene bg bedroom with fade
    show screen room_navigation
    jump bedroom_main

label bedroom_window:
    hide screen room_navigation
    
    scene bg bedroom_window with fade
    $ game_time.advance_time(minutes=10)
    
    narrator "You stand at the window, frost painting intricate patterns on the glass."
    narrator "Beyond, your domain stretches out under its blanket of snow."
    
    if game_time.hour < 12:
        narrator "Morning light makes the snow sparkle like scattered diamonds."
        narrator "Smoke rises from village hearths. Your people are waking to another cold day."
    elif game_time.hour < 17:
        narrator "The afternoon sun hangs low in the winter sky, casting long shadows."
        narrator "Figures move through the snow below - servants, guards, villagers going about their business."
    else:
        narrator "Twilight descends, painting the snow in shades of blue and purple."
        narrator "Lights begin to appear in windows across your domain."
        narrator "Soon, darkness will claim the land once more."
    
    narrator "You wonder how many more winters your people can endure."
    
    scene bg bedroom with fade
    show screen room_navigation
    jump bedroom_main

label bedroom_mirror:
    hide screen room_navigation
    
    scene bg bedroom_mirror with fade
    $ game_time.advance_time(minutes=15)
    
    narrator "You stand before the ornate mirror, studying your reflection."
    narrator "The face that stares back is your own, yet somehow changed."
    
    menu:
        "See strength and determination":
            narrator "The ruler you see is strong, capable, ready to lead."
            narrator "Perhaps the mirror shows what you wish to be."
            
        "See worry and doubt":
            narrator "You see the fear in your eyes, the weight you carry."
            narrator "Leadership has already begun to age you."
            
        "See your father's features":
            narrator "There - in the line of your jaw, the set of your eyes."
            narrator "You are more like him than you realized."
            narrator "For better or worse."
    
    narrator "You turn away from the mirror, uncertain which version of yourself is true."
    
    scene bg bedroom with fade
    show screen room_navigation
    jump bedroom_main

label bedroom_journal:
    hide screen room_navigation
    
    scene bg bedroom_journal with fade
    $ game_time.advance_time(minutes=30)
    
    narrator "You open your personal journal, the leather-bound book familiar in your hands."
    narrator "Its pages contain your private thoughts, fears, and hopes."
    
    menu:
        "Read past entries":
            narrator "You flip through earlier pages, reading your thoughts from weeks ago."
            narrator "So much has changed. So quickly."
            
        "Write about recent events":
            narrator "You dip your quill and begin to write."
            narrator "Recording the day's events, your decisions, your doubts."
            narrator "Perhaps future generations will read these words and understand."
            
        "Write about your feelings":
            narrator "You pour your heart onto the page - fears, hopes, frustrations."
            narrator "Here, at least, you can be honest. No masks, no pretense."
    
    narrator "You close the journal and lock it away. Some thoughts are yours alone."
    
    scene bg bedroom with fade
    show screen room_navigation
    jump bedroom_main

label bedroom_wardrobe:
    hide screen room_navigation
    
    scene bg bedroom_wardrobe with fade
    $ game_time.advance_time(minutes=20)
    
    narrator "You open the wardrobe, examining the various garments within."
    narrator "Each outfit serves a purpose - formal robes for court, simple clothes for privacy, furs for warmth."
    
    menu:
        "Choose formal attire":
            narrator "You select your finest robes, appropriate for receiving important guests."
            narrator "The weight of the fabric reminds you of the weight of office."
            
        "Choose practical clothing":
            narrator "You pick simple, warm garments. Comfort over ceremony."
            narrator "Today, you wish to be a person, not just a ruler."
            
        "Choose hunting leathers":
            narrator "The leather is worn but well-maintained."
            narrator "Perhaps you should spend more time outdoors, away from courtly intrigue."
    
    narrator "You organize the wardrobe, finding a small measure of control in this simple task."
    
    scene bg bedroom with fade
    show screen room_navigation
    jump bedroom_main

label bedroom_rest:
    hide screen room_navigation
    
    scene bg bedroom_rest with fade
    $ game_time.advance_time(hours=1)
    
    narrator "You lie back on your bed, not to sleep, but simply to rest."
    narrator "The mattress is stuffed with good wool, the blankets heavy and warm."
    
    narrator "You close your eyes, letting tension drain from your body."
    narrator "The sounds of the palace drift through your door - distant voices, footsteps, the crackle of fires."
    
    narrator "For one hour, you allow yourself to simply exist."
    narrator "No decisions to make, no petitioners to hear, no crown to wear."
    
    narrator "Just rest."
    
    narrator "When you finally rise, you feel somewhat restored."
    narrator "The duties of leadership await, but you're better prepared to face them."
    
    scene bg bedroom with fade
    show screen room_navigation
    jump bedroom_main
