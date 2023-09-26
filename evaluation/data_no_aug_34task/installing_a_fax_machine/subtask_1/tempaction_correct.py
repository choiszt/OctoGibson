

def act(robot, env, camera):
    waxpaper_191 = registry(env, 'waxpot_191')
    MoveBot(env, robot, waxpaper_191, camera)
    donothing(env)
