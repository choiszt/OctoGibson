def act( task,robext):
    # Subtask 1: Grasp The Recyclingsbag
    recyclingsbag = registry(env, "recycled_bag_193")
    EasyGrasp(robot, recyclingbag)
    donothing(env)

