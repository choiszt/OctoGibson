

def act(robot, env, camera):
    beet_275 = registry(env, 'beet_275')
    MoveBot(env, robot, beet_275, camera)
    donothing(env)
