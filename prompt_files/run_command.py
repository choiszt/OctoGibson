import subprocess

def run_command_in_terminal(command_args, process_name, conda_env):
    activate_env_command = f"source /opt/anaconda3/bin/activate {conda_env}"
    if process_name == 'gpt':
        command = f"python prompt_files/execute_gpt.py -save {command_args['save']}"
    elif process_name == 'sim':
        command = f"python prompt_files/execute_sim.py -t {command_args['t']} -g {command_args['g']} -s {command_args['s']} -a {command_args['a']} -save {command_args['save']} -r {command_args['r']} -target {command_args['target']} --/log/level=error --/log/fileLogLevel=error --/log/outputStreamLevel=error"
    full_command = f"bash -c '{activate_env_command} && {command}'"
    subprocess.Popen(["gnome-terminal", "--", "bash", "-c", full_command])

if __name__ == "__main__":
    pass
    # test1_command = "python prompt_files/execute_gpt.py"
    # test2_command = "python prompt_files/execute_sim.py --/log/level=error --/log/fileLogLevel=error --/log/outputStreamLevel=error"
    # conda_env1 = "gpt"
    # conda_env2 = "omni"

    # run_command_in_terminal(test1_command, conda_env1)
    # run_command_in_terminal(test2_command, conda_env2)
