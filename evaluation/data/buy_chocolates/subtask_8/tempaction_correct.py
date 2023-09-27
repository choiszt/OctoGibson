

def act(robot, env, camera):
    checkout_counter = registry(env, 'checkout_counter_sckdal_0')
    MoveBot(env, robot, checkout_counter, camera)
    donothing(env)
