

def act(robot, env, camera):
    bottom_cabinet = registry(env, 'bottom_cabinet_no_top_qudfwe_0')
    open(robot, bottom_cabinet)
    donothing(env)
