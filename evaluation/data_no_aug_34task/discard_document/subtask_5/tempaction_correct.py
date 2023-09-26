

def act(camera, robot):
    recyclings = registry(env, 'recycliling_bin')
    (MoveBot(env.world, robot, recyclings, camera),)
    donothing(env)
