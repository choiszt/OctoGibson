

def act(robot, env, camera):
    wicker_wizard = registry(env, 'wickerbaskets_276')
    EasyGrasp(robot, wicker_wizard)
    donothing(env)
