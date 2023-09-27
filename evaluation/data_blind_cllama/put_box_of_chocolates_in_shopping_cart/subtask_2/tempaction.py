def act(robot,env,camera):
    # Subtask 2: Grasp the box of chocolates
    box_of_chocolates = registry(env, "box_of_chocolates_143")
    EasyGrasp(robot, box_of_chocolates)
    donothing(env)

