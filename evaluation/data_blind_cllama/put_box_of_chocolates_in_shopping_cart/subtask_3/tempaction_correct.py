

def act(robot, env, camera):
    countertop = registry(env, 'countertop_tpuwys_1')
    MoveBot(env, robot, countertop, camera)
    donothing(env)
