

def act(robot, env, camera):
    modem_279 = registry(env, 'modem_279')
    MoveBot(env, robot, modem_279, camera)
    donothing(env)
