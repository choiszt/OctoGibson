def act(robot,env,camera):
    # Subtask 3: Put the document into the bin.
    legal_document_189 = registry(env,"legal_document_189")
    recycling_bin_188 = registry(env,"recycling_bin_188")
    put_inside(robot, legal_document_189, recycling_bin_188)
    donothing(env)

