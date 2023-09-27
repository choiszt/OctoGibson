def act(robot,env,camera):
    # Subtask 2: Grasp the document
    document = registry(env, "document_189")
    EasyGrasp(robot, document)
    donothing(env)

