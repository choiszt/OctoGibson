import subprocess
import time
import signal
import os


def run_command_in_terminal(command, conda_env):
    activate_env_command = f"source /opt/anaconda3/bin/activate {conda_env}"
    full_command = f"bash -c '{activate_env_command} && {command}'"
    return subprocess.Popen(["gnome-terminal", "--", "bash", "-c", full_command])


def check_processes(processes):
    while True:
        for p in processes:
            retcode = p.poll()
            # 如果其中一个进程结束或异常退出
            if retcode is not None:
                terminate_processes(processes)
                return

        time.sleep(5)  # 每隔5秒检查一次进程的状态


def terminate_processes(processes):
    for p in processes:
        if p.poll() is None:  # 如果进程仍然在运行
            os.killpg(os.getpgid(p.pid), signal.SIGTERM)  # 杀死该进程及其子进程


if __name__ == "__main__":
    test1_command = "python prompt_files/1.py"
    test2_command = "python prompt_files/2.py"
    conda_env1 = "base"
    conda_env2 = "kitti"

    processes = []
    processes.append(run_command_in_terminal(test1_command, conda_env1))
    processes.append(run_command_in_terminal(test2_command, conda_env2))

    try:
        check_processes(processes)
    except KeyboardInterrupt:
        terminate_processes(processes)
