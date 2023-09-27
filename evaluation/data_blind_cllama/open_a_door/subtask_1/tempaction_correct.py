

def act(robot, env, camera):
    door = registry(env, 'door_wuinhm_0')
    open(robot, door)
    donothing(env)
