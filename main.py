def on_on_chat():
    mobs.kill(mobs.target(ALL_PLAYERS))
player.on_chat("$Kill All", on_on_chat)

def on_on_chat2():
    player.say("Nigger or niggas")
player.on_chat("$N Word", on_on_chat2)

def on_on_chat3():
    player.say("LIST OF COMMANDS $Kill All $Crash All $N Word $FC $SA $Agent $Block $Mob Creator $TNT TEST")
player.on_chat("$Help", on_on_chat3)

def on_on_chat4():
    mobs.spawn(PRIMED_TNT, pos(0, 0, 0))
player.on_chat("$TNT TEST", on_on_chat4)

def on_on_chat5():
    gameplay.set_game_mode(CREATIVE, mobs.target(ALL_PLAYERS))
player.on_chat("$FC", on_on_chat5)

def on_on_chat6():
    gameplay.set_game_mode(SURVIVAL, mobs.target(ALL_PLAYERS))
player.on_chat("$SA", on_on_chat6)

def on_on_chat7():
    for index in range(4):
        mobs.spawn(CHICKEN, pos(0, 0, 0))
player.on_chat("$Mob Creator", on_on_chat7)

def on_on_chat8():
    for index2 in range(3424988):
        blocks.place(GRASS, pos(0, 0, 0))
        gameplay.time_set(gameplay.time(DAY))
        gameplay.time_set(gameplay.time(NIGHT))
        mobs.spawn(CHICKEN, pos(10, 0, 0))
        gameplay.set_game_mode(CREATIVE, mobs.target(ALL_PLAYERS))
        mobs.spawn(PRIMED_TNT, pos(0, 0, 0))
        gameplay.set_game_mode(SURVIVAL, mobs.target(ALL_PLAYERS))
        blocks.place(OBSIDIAN, pos(0, 0, 0))
        gameplay.xp(999999999, mobs.target(ALL_PLAYERS))
player.on_chat("$Crash All", on_on_chat8)

def on_on_chat9():
    agent.teleport_to_player()
player.on_chat("$Agent", on_on_chat9)

def on_on_chat10():
    mobs.apply_effect(FIRE_RESISTANCE, mobs.target(ALL_PLAYERS), 600, 255)
    mobs.apply_effect(NIGHT_VISION, mobs.target(ALL_PLAYERS), 600, 255)
player.on_chat("$Effect All", on_on_chat10)

def on_on_chat11():
    gameplay.set_weather(CLEAR)
    gameplay.time_set(gameplay.time(DAY))
player.on_chat("$Day", on_on_chat11)

def on_on_chat12():
    blocks.place(STONE, pos(0, 0, 0))
player.on_chat("$Block", on_on_chat12)
