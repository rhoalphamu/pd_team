from src.employee import Employee


def test_salary_function():
    expected_outcome = 2000
    calculated_outcome = Employee("ram", 28, 2).calculate_salary()

    assert expected_outcome == calculated_outcome