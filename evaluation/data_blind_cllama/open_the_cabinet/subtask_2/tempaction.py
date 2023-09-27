def act(robot,env,camera):
    # Subtask 2: Open the cabinet
    bottom_cabinet_nddvba_0 = registry(env,"bottom_cabinet_nddvba_0")
    open(robot, bottom_cabinet_nddvba_0)
    donothing(env)

