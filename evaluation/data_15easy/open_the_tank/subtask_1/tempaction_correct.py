

def act(robot, env, camera):
    stank = registry(env, 'tank_88')
    MoveBot(open(robot), stank, camera)
    donothing(env)
