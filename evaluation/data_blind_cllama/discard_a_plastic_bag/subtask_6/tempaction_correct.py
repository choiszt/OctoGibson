

def act(robot, env, camera):
    clothes_dryer = registry(env, 'clothes_dryer_zlmnfg_0')
    MoveBot(env, robot, clothes_dryer, camera)
    donothing(env)
