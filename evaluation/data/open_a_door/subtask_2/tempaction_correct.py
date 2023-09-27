

def act(robot, env, camera):
    door = registry(env, 'door_wuinhm_0')
    MoveBot(env, robot, door, camera)
    donothing(env)
