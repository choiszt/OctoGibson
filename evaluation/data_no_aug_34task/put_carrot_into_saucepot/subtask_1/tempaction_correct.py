

def act(robot, env, camera):
    fridge = registry(env, 'fridge_xyejdx_0')
    open(robot, fridge)
    donothing(env)
