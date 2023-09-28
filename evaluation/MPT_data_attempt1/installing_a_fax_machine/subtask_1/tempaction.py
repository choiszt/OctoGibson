def act(robot,env,camera):
    # Subtask 1: Move the Robotto the Fax_Device_88
    fax_device = registry(env, "fax_phone_88")
    MoveBot(env,"robot", fax_phone, camera)
    donothing(env)

