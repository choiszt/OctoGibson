

def act(robot, env, camera):
    suitcase_276 = registry(env, 'suitcase-276')
    MoveBot(env, robot, suitcase_276, camera)
    donothing(env)
