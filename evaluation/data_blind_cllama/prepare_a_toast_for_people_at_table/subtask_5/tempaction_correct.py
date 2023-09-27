

def act(robot, env, camera):
    toast_150 = registry(env, 'toast_150')
    EasyGrasp(robot, toast_150)
    donothing(env)
