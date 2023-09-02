import subprocess

def run_command_in_terminal(command, conda_env):
    activate_env_command = f"source ~/anaconda3/bin/activate {conda_env}"
    full_command = f"bash -c '{activate_env_command} && {command}'"
    subprocess.Popen(["gnome-terminal", "--", "bash", "-c", full_command])

if __name__ == "__main__":
    test1_command = "python execute_gpt.py"
    test2_command = "python execute_sim.py"
    conda_env1 = "gpt"
    conda_env2 = "omnigibson"

    run_command_in_terminal(test1_command, conda_env1)
    run_command_in_terminal(test2_command, conda_env2)
