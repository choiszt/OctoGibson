

def act(robot, env, camera):
    desk_erg_0 = registry(env, 'desk-erg-0')
    MoveBot(env, robot, desk_erg_0, camera)
    donothing(env)
