def act(robot,env,camera):
    # Subtask 1: Move the Robotto the Faxmachine
    faxmachine = registry(env, "fax_machine_88")
    MoveBot( env, robot, faxmachine, camera)
    donothing(env)

