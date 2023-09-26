

def act(robot, env, camera):
    ground = MoveBot(env, 'ground')
    MoveBot(env, robot, robot, camera)
    donothing(env)
