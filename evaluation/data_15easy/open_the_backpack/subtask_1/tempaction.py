def act(robot,env,camera):
    # Subtask 1: Move the operator to the suitcase
    suitcase_276 = registry(env,"suitcase-276")
    MoveBot(env, robot, suitcase_276, camera)
    donothing(env)

