def act(robot,env,camera):
    # Subtask 3: Move the robot to the trash can.
    trash_can_281 = registry(env,"trash_can_281")
    MoveBot(env, robot, trash_can_281, camera)
    donothing(env)

