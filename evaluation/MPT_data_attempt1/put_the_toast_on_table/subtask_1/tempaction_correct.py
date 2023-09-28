

def act(robot, env, camera):
    bottom_cabinet = registry(env, 'bottom_cupboard_no_top_vzzafs_0')
    open(robot, bottom_cabinet)
    donothing(env)
