from mrjob.job import MRJob
from mrjob.step import MRStep
# python 4.py tem.csv
class HottestCoolestYear(MRJob):

    def steps(self):
        return [
            MRStep(mapper=self.mapper,
                   reducer=self.reducer),
            MRStep(reducer=self.reducer_avg)
        ]

    def mapper(self, _, line):
        year, temp = line.strip().split(',')
        yield year, float(temp)

    def reducer(self, key, values):
        temps = list(values)
        if temps:  # Check if temps is not empty
            yield None, (key, max(temps), min(temps))

    def reducer_avg(self, _, temps):
        hottest_year = None
        hottest_temp = float("-inf")
        coolest_year = None
        coolest_temp = float("inf")

        for year, max_temp_year, min_temp_year in temps:
            if max_temp_year > hottest_temp:
                hottest_temp = max_temp_year
                hottest_year = year
            if min_temp_year < coolest_temp:
                coolest_temp = min_temp_year
                coolest_year = year

        if hottest_year:
            yield "Hottest year", (hottest_year, hottest_temp)
        if coolest_year:
            yield "Coolest year", (coolest_year, coolest_temp)

if __name__ == '__main__':
    HottestCoolestYear.run()
