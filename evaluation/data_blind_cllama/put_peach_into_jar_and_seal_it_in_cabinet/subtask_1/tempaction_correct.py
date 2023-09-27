

def act(robot, env, camera):
    countertop_tpuwys_1 = registry(env, 'countertop_tpuwys_1')
    MoveBot(env, robot, countertop_tpuwys_1, camera)
    donothing(env)
