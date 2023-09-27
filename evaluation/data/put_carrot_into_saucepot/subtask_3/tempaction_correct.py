

def act(robot, env, camera):
    saucepot_170 = registry(env, 'saucepot_170')
    MoveBot(env, robot, saucepot_170, camera)
    donothing(env)
