def act(robot,env,camera):
    # Subtask 5: Grasp the chocolates
    chocolates = registry(env,"chocolates_177")
    EasyGrasp(robot, chocolates)
    donothing(env)

