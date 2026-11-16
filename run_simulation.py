import json
import argparse

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

    parser = argparse.ArgumentParser()

    parser.add_argument(
        "--scenario",
        default="test_scenario_01.json"
    )

    args = parser.parse_args()

    success = run_simulation(args.scenario)

    if not success:
        raise SystemExit(1)
