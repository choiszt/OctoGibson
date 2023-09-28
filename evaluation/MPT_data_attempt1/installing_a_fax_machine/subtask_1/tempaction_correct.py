

def act(robot, env, camera):
    fax_device = registry(env, 'fax_phone_88')
    MoveBot(env, 'robot', fax_device, camera)
    donothing(env)
