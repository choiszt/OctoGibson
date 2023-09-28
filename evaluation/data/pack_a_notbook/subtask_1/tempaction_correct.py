

def act(robot, env, camera):
    cabinet = registry(env, 'cabnet_dszchb_0')
    MoveBot(env, robot, cabinet, camera)
    donothing(env)
