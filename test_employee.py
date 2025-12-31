from employee import employee_details
def test_employee_details():
    expected_output = (
        "Employee_Name:Nitya Savadatti\n"
        "Employee_ID:01FE24BCA174\n"
        "Department:BCA\n"
        "Salary:80000"
    )
    assert employee_details("Nitya Savadatti","01FE24BCA174","BCA",80000)==expected_output
