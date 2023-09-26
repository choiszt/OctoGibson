

def act(robot, env, camera):
    oven_wuinhm_0 = registry(env, 'oven_wuinhm0')
    MoveBot(env, robot, oven_wuinhm_0, camera)
    donothing(env)
