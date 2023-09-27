def act(robot,env,camera):
    # Subtask 1: Register the door
    door = registry(env, "door_wuinhm_0")
    # Subtask 2: Open the door
    open(robot, door)
    donothing(env)

