

def act(robot, env):
    toasterive = registry(env, 'Toaster_Oven_170')
    EasyGrasp(robot, toasterive)
    donothing(env)
