

def act(robot, env, camera):
    document = registry(env, 'document_189')
    MoveBot(env, robot, document, camera)
    donothing(env)
