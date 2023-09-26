

def act(robot, env, camera):
    bottom_cupboard = registry(env, 'bottom_htck_ca1')
    open(robot, (bottom_cupboard - camera))
    donothing(env)
