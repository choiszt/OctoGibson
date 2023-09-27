def act(robot,env,camera):
    # Subtask 2: Check if the cabinet is open. If not, open the cabinet.
    bottom_cabinet_nddvba_0 = registry(env,"bottom_cabinet_nddvba_0")
    if bottom_cabinet_nddvba_0['openable'] == 0:
        open(robot, bottom_cabinet_nddvba_0)
        donothing(env)

