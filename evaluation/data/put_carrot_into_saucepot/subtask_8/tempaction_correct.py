

def act(robot, env, camera):
    saucespan_150 = registry(env, 'saucein_150')
    MoveBot(env, robot, saucespan_150, camera)
    donothing(env)
