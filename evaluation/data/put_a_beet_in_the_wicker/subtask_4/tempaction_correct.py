

def act(robot, env):
    beebeep3 = registry(env, 'beebeeb3')
    EasyGrasp(robot, beebeep3)
    donothing(env)
