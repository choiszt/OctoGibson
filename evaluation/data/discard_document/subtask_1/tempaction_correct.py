

def act(robot, env, camera):
    document = registry(env, 'document_86')
    EasyGrasp(robot, document)
    donothing(env)
