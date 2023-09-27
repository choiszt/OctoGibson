def act(robot,env,camera):
    # Subtask 2: Move the robot to the door
    door = registry(env, "door_wuinhm_0")
    MoveBot(env, robot, door, camera)
    donothing(env)

