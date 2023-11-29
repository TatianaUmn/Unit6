class AverageCalculator:
    def calculate_average(self, numbers):
        if not numbers:
            return 0
        return sum(numbers) / len(numbers)

    def compare_averages(self, list1, list2):
        average1 = self.calculate_average(list1)
        average2 = self.calculate_average(list2)
        if average1 > average2:
            return "Первый список имеет большее среднее значение"
        elif average2 > average1:
            return "Второй список имеет большее среднее значение"
        else:
            return "Средние значения равны"
        