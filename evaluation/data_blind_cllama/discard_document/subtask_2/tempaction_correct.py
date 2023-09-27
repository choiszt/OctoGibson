

def act(robot, env, camera):
    document = registry(env, 'document_189')
    EasyGrasp(robot, document)
    donothing(env)
