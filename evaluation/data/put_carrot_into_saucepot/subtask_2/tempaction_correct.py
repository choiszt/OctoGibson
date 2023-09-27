

def act(robot, env, camera):
    countertop_tpuwys_2 = registry(env, 'countertop-tpuwiys-2')
    MoveBot(env, robot, countertop_tpuwys_2, camera)
    donothing(env)
