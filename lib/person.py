class Person:
    approved_jobs = [
        "ITC", "Doctor", "Teacher", "Programmer",
        "Lawyer", "Engineer", "Accountant", "Nurse"
    ]

    def __init__(self, name="", job=None):
        # ---- NAME VALIDATION (MUST BE FIRST!) ----
        if not isinstance(name, str):
            print("Name must be string between 1 and 25 characters.")
            self.name = None
        elif len(name) == 0 or len(name) > 25:
            print("Name must be string between 1 and 25 characters.")
            self.name = None
        else:
            self.name = name.title()

        # ---- JOB VALIDATION (only runs after name check) ----
        if job is not None and job not in self.approved_jobs:
            print("Job must be in list of approved jobs.")
            self.job = None
        else:
            self.job = job