def act(robot,env,camera):
    # Subtask 1: Grasp the cup
    cup_85 = registry(env,"cup_85")
    EasyGrasp(robot, cup_85)
    donothing(env)

