

def act(robot, env, camera):
    fridge_xyejdx_0 = registry(env, 'fridge_xyejdx_0')
    MoveBot(env, robot, fridge_xyejdx_0, camera)
    donothing(env)
