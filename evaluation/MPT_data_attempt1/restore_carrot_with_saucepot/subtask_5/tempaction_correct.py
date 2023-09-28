

def act(robot, env, camera):
    oven = registry(env, 'oven_wuinhm_0')
    open(robot, oven)
    donothing(env)
