import json
import sys

from main import calculate_control


def run_simulation(scenario_file):

    with open(scenario_file, "r") as file:
        scenario = json.load(file)

    target = scenario["target_speed"]
    measurements = scenario["measurements"]
    tolerance = scenario["tolerance"]

    print("Starting simulation...")

    for index, current_speed in enumerate(measurements):

        error = abs(target - current_speed)

        control = calculate_control(
            target,
            current_speed
        )

        print(
            f"Step {index + 1}: "
            f"speed={current_speed}, "
            f"control={control}"
        )

        if error > tolerance:
            print("Simulation FAILED")
            return False

    print("Simulation PASSED")
    return True


if __name__ == "__main__":

    scenario_file = (
        sys.argv[1]
        if len(sys.argv) > 1
        else "test_scenario_01.json"
    )

    success = run_simulation(scenario_file)

    if not success:
        sys.exit(1)
