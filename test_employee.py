from employee import employee_details

def test_employee_details():
    expected_output = (
        "Employee Name :Shreya\n"
        "Employee ID :01FE24BCA150\n"
        "Department :BCA\n "
        "Salary :80000"
    )
    assert employee_details("Shreya","01FE24BCA150","BCA",80000) == expected_output
