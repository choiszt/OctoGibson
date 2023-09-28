def act(robot,env,camera):
    # Subtask 1: Move the Robot to the Paper Bag
    paper_bag_277 = registry(env,"paper_box_277")
    MoveBot(env, robot, paper_bag-277, camera)
    donothing(env)

