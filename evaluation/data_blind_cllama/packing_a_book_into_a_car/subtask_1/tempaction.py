def act(robot,env,camera):
    # Subtask 1: Move the robot to the suitcase
    suitcase_279 = registry(env,"suitcase_279")
    MoveBot(env, robot, suitcase_279, camera)

