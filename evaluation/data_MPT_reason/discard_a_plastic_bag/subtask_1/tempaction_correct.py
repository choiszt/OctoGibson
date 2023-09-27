

def act(robot, env, camera):
    straw_171 = registry(env, 'staw_171')
    MoveBot(env, robot, straw_171, camera)
    donothing(env)
