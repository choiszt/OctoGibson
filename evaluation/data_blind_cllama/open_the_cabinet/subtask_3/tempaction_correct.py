

def act(robot, env, camera):
    bottom_cabinet_nddvba_0 = registry(env, 'bottom_cabinet_nddvba_0')
    MoveBot(env, robot, bottom_cabinet_nddvba_0, camera)
    donothing(env)
