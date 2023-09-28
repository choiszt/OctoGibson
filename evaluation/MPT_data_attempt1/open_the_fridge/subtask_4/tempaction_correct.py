

def act(robot, env):
    fridge = registry(env, 'fridgexyejds_0', 'openable')
    open(robot, fridge)
    donothing([])
