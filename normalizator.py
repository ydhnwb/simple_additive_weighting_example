class Normalizator:

    def normalize_salary(self, datas, salary):
        """The data must be numeric. The more high salary,
         higher salary will reduce the probability to get scholarship"""
        lowest_salary = min(datas)
        return lowest_salary/salary

    def normalize_dependant(self, datas, num_child):
        """Get parents total dependant. Higher is better to get the probability"""
        maximum_num = max(datas)
        return (num_child/maximum_num)/10

    def normalize_gpa(self, datas, gpa):
        """Get gpa. Higher is better"""
        maximum_num = max(datas)
        return gpa/maximum_num

