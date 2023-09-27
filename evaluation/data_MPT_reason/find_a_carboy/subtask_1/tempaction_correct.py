

def act(robot, env, camera):
    fridge = registry(env, 'fridge_dszchb_0')
    open(robot, fridge)
    donothing(env)
