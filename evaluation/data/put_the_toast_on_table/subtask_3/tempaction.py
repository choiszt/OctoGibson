def act(robot,env,camera):
    # Subtask 3: Grasp the toast from the bottom cabinet
    toast_150 = registry(env,"toast_150")
    EasyGrasp(robot, toast_150)
    donothing(env)

