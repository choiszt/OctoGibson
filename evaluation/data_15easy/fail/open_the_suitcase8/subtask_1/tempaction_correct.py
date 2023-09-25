

def act(robot, env, camera):
    suitcase_275 = registry(env, 'suitcase')
    MoveBot(env, robot, suitcase_275, camera)
    donothing(env)
