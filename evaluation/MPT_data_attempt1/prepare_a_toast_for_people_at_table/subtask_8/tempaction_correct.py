

def act(robot, env):
    countertop = registry(env, 'countertop-tpuwsys_1')
    MoveBot(env, donothing(countertop), camera)
    donothing(env)
