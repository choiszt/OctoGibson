def act(robot,env,camera):
    # Subtask 2: Grasp the beet
    beet_275 = registry(env,"beet_275")
    EasyGrasp(robot, beet_275)
    donothing(env)

