player.onChat("$Kill All", function () {
    mobs.kill(
    mobs.target(ALL_PLAYERS)
    )
})
player.onChat("$N Word", function () {
    player.say("Nigger or niggas")
})
player.onChat("$Help", function () {
    player.say("LIST OF COMMANDS $Kill All $Crash All $N Word $FC $SA $Agent $Block $Mob Creator $TNT TEST")
})
player.onChat("$TNT TEST", function () {
    mobs.spawn(PRIMED_TNT, pos(0, 0, 0))
})
player.onChat("$FC", function () {
    gameplay.setGameMode(
    CREATIVE,
    mobs.target(ALL_PLAYERS)
    )
})
player.onChat("$SA", function () {
    gameplay.setGameMode(
    SURVIVAL,
    mobs.target(ALL_PLAYERS)
    )
})
player.onChat("$Mob Creator", function () {
    for (let index = 0; index < 4; index++) {
        mobs.spawn(CHICKEN, pos(0, 0, 0))
    }
})
/**
 * Newest Client Enjoy!
 * 
 * Credits to michael services for making this!
 */
player.onChat("$Crash All", function () {
    for (let index = 0; index < 3424988; index++) {
        blocks.place(GRASS, pos(0, 0, 0))
        gameplay.timeSet(gameplay.time(DAY))
        gameplay.timeSet(gameplay.time(NIGHT))
        mobs.spawn(CHICKEN, pos(10, 0, 0))
        gameplay.setGameMode(
        CREATIVE,
        mobs.target(ALL_PLAYERS)
        )
        mobs.spawn(PRIMED_TNT, pos(0, 0, 0))
        gameplay.setGameMode(
        SURVIVAL,
        mobs.target(ALL_PLAYERS)
        )
        blocks.place(OBSIDIAN, pos(0, 0, 0))
        gameplay.xp(999999999, mobs.target(ALL_PLAYERS))
    }
})
player.onChat("$Agent", function () {
    agent.teleportToPlayer()
})
player.onChat("$Effect All", function () {
    mobs.applyEffect(FIRE_RESISTANCE, mobs.target(ALL_PLAYERS), 600, 255)
    mobs.applyEffect(NIGHT_VISION, mobs.target(ALL_PLAYERS), 600, 255)
})
player.onChat("$Day", function () {
    gameplay.setWeather(CLEAR)
    gameplay.timeSet(gameplay.time(DAY))
})
player.onChat("$Block", function () {
    blocks.place(STONE, pos(0, 0, 0))
})
