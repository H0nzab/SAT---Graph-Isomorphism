import subprocess
import sys
import re

def solve_cnf(cnf_filepath, solver_cmd=None):
    """
    Spustí solver nad DIMACS souborem.
    Vrací (is_sat, true_vars), kde true_vars obsahuje ID proměnných s hodnotou True.
    """
    if solver_cmd is None:
        solver_cmd = ["glucose", "-model"]

    try:
        result = subprocess.run(
            [*solver_cmd, cnf_filepath],
            capture_output=True,
            text=True
        )
    except FileNotFoundError:
        print(f"Chyba: SAT solver '{solver_cmd[0]}' nebyl nalezen.")
        sys.exit(1)

    match = re.search(r"c CPU time\s*:\s*([0-9.]+)\s*s", result.stdout)
    cpu_time = match.group(1) if match else "?"

    if result.returncode == 20:
        return False, [], cpu_time

    true_vars = []
    for line in result.stdout.splitlines():
        if line.startswith("v "):
            for token in line.split()[1:]:
                val = int(token)
                if val > 0:
                    true_vars.append(val)

    return True, true_vars, cpu_time