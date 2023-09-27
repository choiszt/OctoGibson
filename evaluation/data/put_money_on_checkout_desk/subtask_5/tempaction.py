def act(robot,env,camera):
    # Subtask 4: Put the money on the checkout desk
    money_143 = registry(env,"money_143")
    checkout_counter_sckdal_0 = registry(env,"checkout_counter_sckdal_0")
    put_ontop(robot, money_143, checkout_counter_sckdal_0)
    donothing(env)

