

def act(robot, env, camera):
    cab_1 = registry(env)
    MoveBot(env, robot, cab_1, camera)
    donothing(env)
