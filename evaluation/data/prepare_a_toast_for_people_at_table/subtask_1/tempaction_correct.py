

def act(robot, env, camera):
    bottom_cabinet = registry(env, 'bottom_hock_ca_1')
    MoveBot(env, robot, bottom_cabinet, camera)
    donothing(env)
