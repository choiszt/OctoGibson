def act(robot,env,camera):
    # Subtask 1: Grasp the plate
    plate_191 = registry(env,"plate_191")
    EasyGrasp(robot, plate_191)
    donothing(env)

