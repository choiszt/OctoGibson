def act(robot,env,camera):
    # Subtask 6: Put the toast on the table
    toast_191 = registry(env,"toast_191")
    breakfast_table_dnsjnv_0 = registry(env,"breakfast_table_dnsjnv_0")
    put_ontop(robot, toast_191, breakfast_table_dnsjnv_0)
    donothing(env)

