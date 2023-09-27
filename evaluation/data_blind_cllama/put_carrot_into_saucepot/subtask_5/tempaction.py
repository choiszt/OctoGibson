def act(robot,env,camera):
    # Subtask 4: Put the carrot into the saucepot
    carrot_151 = registry(env,"carrot_151")
    saucepot_170 = registry(env,"saucepot_170")
    put_inside(robot, carrot_151, saucepot_170)
    donothing(env)

