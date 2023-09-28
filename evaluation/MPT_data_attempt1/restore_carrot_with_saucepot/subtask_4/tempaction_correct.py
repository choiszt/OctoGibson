

def act(robot, env, camera):
    carrot = registry(env, 'carrot')
    MoveBot(env, robot, carrot, camera)
    donothing(env)
