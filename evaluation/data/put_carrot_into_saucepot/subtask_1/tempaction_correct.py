

def act(robot, env, camera):
    carrot_178 = registry(env, 'carrot_178')
    MoveBot(env, robot, carrot_178, camera)
    donothing(env)
