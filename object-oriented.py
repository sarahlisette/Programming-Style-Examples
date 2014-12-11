# Print out all the state names from the csv
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