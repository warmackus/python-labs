class Employee:
    def __init__(self, name, emp_id):
        self.name = name
        self.id = emp_id

    def get_info(self):
        return f"ID: {self.id}, Имя: {self.name}"


class Manager(Employee):
    def __init__(self, name, emp_id, department):
        super().__init__(name, emp_id)
        self.department = department

    def manage_project(self):
        return f"{self.name} управляет проектом в отделе {self.department}"


class Technician(Employee):
    def __init__(self, name, emp_id, specialization):
        super().__init__(name, emp_id)
        self.specialization = specialization

    def perform_maintenance(self):
        return f"{self.name} выполняет техническое обслуживание ({self.specialization})"


class TechManager(Manager, Technician):
    def __init__(self, name, emp_id, department, specialization):
        Manager.__init__(self, name, emp_id, department)
        Technician.__init__(self, name, emp_id, specialization)
        self.team = []  # список подчиненных

    def add_employee(self, employee):
        self.team.append(employee)
        print(f"{employee.name} добавлен в команду")

    def get_team_info(self):
        if not self.team:
            return "В команде нет сотрудников"
        info = "Команда TechManager:\n"
        for emp in self.team:
            info += f"  - {emp.get_info()}\n"
        return info


# Пример использования
emp1 = Employee("Иван Петров", "E001")
mgr1 = Manager("Анна Сидорова", "M001", "IT")
tech1 = Technician("Петр Иванов", "T001", "Сети")

tm = TechManager("Сергей Технов", "TM001", "Разработка", "DevOps")
tm.add_employee(emp1)
tm.add_employee(mgr1)

print(emp1.get_info())
print(mgr1.manage_project())
print(tech1.perform_maintenance())
print(tm.get_team_info())