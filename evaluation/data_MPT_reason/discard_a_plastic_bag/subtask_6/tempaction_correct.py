

def act(robot, env, camera):
    straw = registry(env, 'staw-277')
    MoveBot(env, robot, straw, camera)
    donothing(env)
