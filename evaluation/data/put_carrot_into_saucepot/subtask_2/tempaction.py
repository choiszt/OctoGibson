def act(robot,env,camera):
    # Subtask 2: Grasp the carrot
    carrot_178 = registry(env,"carrot_178")
    EasyGrasp(robot, carrot_178)
    donothing(env)

