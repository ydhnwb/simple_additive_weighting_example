class Normalizator:

    def normalize_salary(self, datas, salary):
        """The data must be numeric. Higher salary will reduce the probability to get scholarship.
        This salary cannot be zero"""
        lowest_salary = min(datas)
        return lowest_salary/salary

    def normalize_dependant(self, datas, num_child):
        """Get parents total dependant. Higher value will get better probability.
        This can be zero"""
        maximum_num = max(datas)
        if num_child == 0:
            return 1
        return (num_child/maximum_num)

    def normalize_gpa(self, datas, gpa):
        """Get gpa. Higher is better. This shouldnt be zero"""
        maximum_num = max(datas)
        return gpa/maximum_num

