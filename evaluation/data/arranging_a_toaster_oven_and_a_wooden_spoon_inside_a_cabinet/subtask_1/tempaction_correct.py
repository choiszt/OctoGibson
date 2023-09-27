

def act(robot, env, camera):
    toaster_oven_wuinhm_0 = registry(env, 'toaster_oven_wuinhm_0')
    MoveBot(env, robot, toaster_oven_wuinhm_0, camera)
    donothing(env)
