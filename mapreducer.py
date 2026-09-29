#Write to python file code
# import modules
from mrjob.job import MRJob
from mrjob.step import MRStep

# create class inherited from MRJob
class DepartmentCount_XXX(MRJob):
    
    # assign steps, first mapper last reducer
    def steps(self):
        return [
            MRStep(mapper=self.mapper_XXX,
                   reducer=self.reducer_XXX,
                   combiner=self.reducer_XXX)
        ]

    # creating mapper, assigning attributes from dataset
    def mapper_XXX(self, _, line):
        words = line.split(',')
        # Skip the header row
        if words[3] != 'department':
            # Yield department and a count of 1
            yield words[3], 1

    # creating reducer, sum
    def reducer_XXX(self, key, values):
        # Python's built-in sum() is faster than a for-loop
        yield key, sum(values)

if __name__ == '__main__':
    DepartmentCount_XXX.run()