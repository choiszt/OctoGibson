def act(robot,env,camera):
    # Subtask 2: Grasp the money from the checkout counter
    money_142 = registry(env,"money_142")
    EasyGrasp(robot, money_142)
    donothing(env)

