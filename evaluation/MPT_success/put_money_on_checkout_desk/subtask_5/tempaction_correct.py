

def act(robot, env, camera):
    camera = registry(env, 'camera')
    MoveBot(env, camera, camera)
    donothing(env)
