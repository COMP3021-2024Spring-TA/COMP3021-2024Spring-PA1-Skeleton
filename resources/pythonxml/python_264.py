class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        employee_dict = dict()
        for employee in employees:
            employee_dict[employee.id] = employee

        def dfs(index: int) -> int:
            total = employee_dict[index].importance
            for sub_index in employee_dict[index].subordinates:
                total += dfs(sub_index)
            return total

        return dfs(id)