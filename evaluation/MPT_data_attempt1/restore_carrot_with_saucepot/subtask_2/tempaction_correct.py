

def act(robot, env, camera):
    fridge = registry(env, 'carrot-151')
    MoveBot(env, robot, fridge, camera)
