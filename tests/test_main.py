import sys
from pathlib import Path

sys.path.insert(
    0,
    str(Path(__file__).resolve().parents[1])
)

from main import calculate_control, run_service


def test_calculate_control():
    result = calculate_control(10, 8)

    assert result == 1.0


def test_zero_error():
    result = calculate_control(10, 10)

    assert result == 0.0


def test_run_service():
    result = run_service(10, 8)

    assert result["target_speed"] == 10
    assert result["current_speed"] == 8
    assert result["control"] == 1.0
