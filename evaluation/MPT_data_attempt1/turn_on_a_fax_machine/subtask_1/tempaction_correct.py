

def act(robot, env, camera):
    faxmachine = registry(env, 'fax_machine_88')
    MoveBot(env, robot, faxmachine, camera)
    donothing(env)
