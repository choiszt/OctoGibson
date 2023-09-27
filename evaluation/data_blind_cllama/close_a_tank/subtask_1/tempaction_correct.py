

def act(robot, env, camera):
    tank_88 = registry(env, 'tank_88')
    MoveBot(env, robot, tank_88, camera)
    donothing(env)
    close(robot, tank_88)
    donothing(env)
