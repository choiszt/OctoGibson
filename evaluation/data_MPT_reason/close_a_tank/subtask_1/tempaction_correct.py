

def act(robot, env, camera):
    tank_88 = registry(env, 'tank-88')
    MoveBot(env, robot, tank_88, camera)
    donothing(env)
