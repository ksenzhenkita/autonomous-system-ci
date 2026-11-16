def calculate_control(target_speed, current_speed):
    """
    Розрахунок керувального сигналу
    для автономної системи.
    """
    error = target_speed - current_speed
    control = error * 0.5

    return control


def run_service(target_speed, current_speed):
    control = calculate_control(
        target_speed,
        current_speed
    )

    return {
        "target_speed": target_speed,
        "current_speed": current_speed,
        "control": control
    }


if __name__ == "__main__":
    result = run_service(10, 8)

    print("Autonomous system service")
    print("Target speed:", result["target_speed"])
    print("Current speed:", result["current_speed"])
    print("Control signal:", result["control"])
