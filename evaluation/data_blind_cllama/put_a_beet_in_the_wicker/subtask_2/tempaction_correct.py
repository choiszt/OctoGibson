

def act(robot, env, camera):
    beet_275 = registry(env, 'beet_275')
    EasyGrasp(robot, beet_275)
    donothing(env)
