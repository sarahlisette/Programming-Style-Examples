# Class modified to read Obama vote percentages

class ElectionResults:
  
    def __init__(self, filename):
        self.filename = filename

    def load(self):
        self.file = open(self.filename, 'r')
        self.all_lines = self.file.readlines()

    def obamaper(self):
        all_perc = []
        for line in self.all_lines:
            columns = line.split(',')
            all_perc.append(columns[4])
        return all_perc[1:]

    def obamaper_count(self):
        return len(self.obamaper())



# Print out all the Percentages of Obama votes from the csv
# Coded in the "object-oriented" style

from electiondata import ElectionResults

filename = '2012_US_election_state.csv'
results = ElectionResults(filename)
results.load()
print "Opened file:"

obama_perc = results.obamaper()
for perc in obama_perc:
    print "  "+perc

print "done ("+str(results.obamaper_count())+" lines)"