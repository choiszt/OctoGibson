def act(robot,env,camera):
    # Subtask 7: Move to the checkout counter
    checkout_counter = registry(env,"checkout_counter_sckdal_0")
    MoveBot(env, robot, checkout_counter, camera)
    donothing(env)

