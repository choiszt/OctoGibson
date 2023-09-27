def act(robot,env,camera):
    # Subtask 5: Move to the table
    breakfast_table_dnsjnv_0 = registry(env,"breakfast_table_dnsjnv_0")
    MoveBot(env, robot, breakfast_table_dnsjnv_0, camera)
    donothing(env)

