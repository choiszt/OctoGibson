

def act(robot, env, camera):
    fruit = registry(env, 'fruit_88')
    MoveBot(env, 'robot', fruit, camera)
    donothing(env)
