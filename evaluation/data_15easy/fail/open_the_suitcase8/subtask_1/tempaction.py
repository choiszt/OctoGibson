def act(robot,env,camera):
    # Subtask 1: Move the bot to the suitcase
    suitcase_275 = registry(env,"suitcase")
    MoveBot(env, robot, suitcase_275, camera)
    donothing(env)

