def act(robot,env,camera):
    # Subtask 1: Move the robot To theplastic_ bag-275
    plastic_baskets_277 = registry(env,"plastic_ basket_277")
    MoveBot(env, robot, plastic_baskets_277, camera)
    donothing(env)

