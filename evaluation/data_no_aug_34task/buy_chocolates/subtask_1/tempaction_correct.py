

def act(robot, env, camera):
    stove = registry(env, 'stove_rgpphy_0')
    open(robot, stove)
    donothing(env)
