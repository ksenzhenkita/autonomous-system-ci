def calculate_control(target_speed, current_speed):
    error = target_speed - current_speed
    return error * 0.5


def run_service(target_speed, current_speed):
    control = calculate_control(target_speed, current_speed)

    return {
        "target_speed": target_speed,
        "current_speed": current_speed,
        "control": control
    }


if __name__ == "__main__":
    result = run_service(10, 8)
    print("Autonomous service started")
    print(result)
