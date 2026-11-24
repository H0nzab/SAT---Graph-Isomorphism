import subprocess
import sys


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

    is_sat = False
    true_vars = []

    for line in result.stdout.splitlines():
        line = line.strip()
        if line.startswith("s "):
            if "UNSATISFIABLE" in line:
                return False, []
            if "SATISFIABLE" in line:
                is_sat = True
        elif line.startswith("v "):
            for token in line.split()[1:]:
                val = int(token)
                if val > 0:
                    true_vars.append(val)

    return is_sat, true_vars