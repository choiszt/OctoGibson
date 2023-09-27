

def act(robot, env, camera):
    floor = registry(env, 'floor')
    MoveBot(env, robot, floor, camera)
    donothing(env)
