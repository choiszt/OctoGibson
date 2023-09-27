def act(robot,env,camera):
    # Subtask 3: Discard the document
    document = registry(env, "document_189")
    discard(robot, document)
    donothing(env)

