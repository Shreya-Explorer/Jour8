from employee import employee_details
def test_employee_details():
    expected_output = (
        "Employee_Name:Sinchana Naik\n"
        "Employee_ID:01FE24BCA169\n"
        "Department:BCA\n"
        "Salary:80000"
    )
    assert employee_details("Sinchana Naik","01FE24BCA169","BCA",80000)==expected_output
