def act(robot,env,camera):
    # Subtask 1: Grasp the document.
    document_189 = registry(env,"document_189")
    EasyGrasp(robot, document_189)
    donothing(env)

