def employee_details(name,emp_id,department,salary):
    result = (
        f"Employee_Name:{name}\n"
        f"Employee_ID:{emp_id}\n"
        f"Department:{department}\n"
        f"Salary:{salary}"
    )
    return result

if __name__ == "__main__":
    name="Sinchana Naik"
    emp_id="01FE24BCA169"
    department="BCA"
    salary=80000
    print(employee_details(name,emp_id,department,salary))
