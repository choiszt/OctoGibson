

def act(robot, env, camera):
    carrot = registry(env, 'carrot', '151')
    MoveBot(env, robot, carrot, camera)
    donothing(env)
