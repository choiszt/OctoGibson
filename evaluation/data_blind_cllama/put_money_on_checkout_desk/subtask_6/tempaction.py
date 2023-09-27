def act(robot,env,camera):
    # Subtask 3: Move to the checkout desk
    checkout_counter_sckdal_0 = registry(env,"checkout_counter_sckdal_0")
    MoveBot(env, robot, checkout_counter_sckdal_0, camera)
    donothing(env)

