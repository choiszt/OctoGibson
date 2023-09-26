def act(robot,env,camera):
    # Subtask 1: Grasp The Document
    document = registry(env, "document_86")
    EasyGrasp(roBot, document)
    donothing(env)

