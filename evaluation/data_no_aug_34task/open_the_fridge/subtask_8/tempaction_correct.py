

def act(robot, env):
    door = registry(env, 'door_xyezr_0')
    open(robot, door)
    donothing(env)
