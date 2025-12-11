from employee import employee_details

def test_employee_details():
    expected_output = (
        "Employee_Name:Shreya Raykar\n"
        "Employee_ID:01FE24BCA150\n"
        "Department:BCA\n"
        "Salary:80000"
    )
    assert employee_details("Shreya Raykar","01FE24BCA150","BCA",80000)==expected_output
