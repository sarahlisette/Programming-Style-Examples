class ElectionResults:
  
    def __init__(self, filename):
        self.filename = filename

    def load(self):
        self.file = open(self.filename, 'r')
        self.all_lines = self.file.readlines()

    def obama(self):
        total_votes = []
        for line in self.all_lines[1:]:
            columns = line.split(',')
            total_votes.append(int(columns[3]))
        return sum(total_votes)

    def romney(self):
        total_votes = []
        for line in self.all_lines[1:]:
            columns = line.split(',')
            total_votes.append(int(columns[5]))
        return sum(total_votes)


 
