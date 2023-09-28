

def act(robot, env, camera):
    beet3 = registry(env, 'beet')
    EasyGrasp(robot, beet3)
    donothing(env)
