

def act(robot, env, camera):
    countertop = registry(env, 'countertop_tpuwys_2')
    MoveBot(env, robot, countertop, camera)
    donothing(env)
