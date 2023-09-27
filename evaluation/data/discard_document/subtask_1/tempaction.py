def act(robot,env,camera):
    # Subtask 1: Move the robot to the document
    document = registry(env, "document_189")
    MoveBot(env, robot, document, camera)

