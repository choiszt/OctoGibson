def act(robot,env,camera):
    # Subtask 2: Open the Oven, Put the Saucepot on Top, and Close the Ooven after Grasping the Carrots
    oven = registry(env, "oven_wuinhm_0")
    open( robot, oven)
    donothing(env)

