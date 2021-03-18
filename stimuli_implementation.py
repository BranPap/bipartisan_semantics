### This is a simple algorithmic implementation of the proposed stimuli creation and randomisation for Papineau & Velasquez (in progress), an investigation into the semantic bounding of 'Bipartisan'.

# Dependencies
import string
import random

### This will assign participants to one of two conditions; either a fictional alien context, or an American one.

def condition():
    vignette = ""
    trial_condition = random.randint(0,1)
    if trial_condition == 0:
        vignette = "alien"
    else:
        vignette = "american"
    return vignette

### Creates an object class VoteShare

class VoteShare:
    def __init__(self,party_one_for,party_two_for,verdict,dominator):
        ### attrributes
        self.party_one_for = int(party_one_for)
        self.party_one_against = int(50 - party_one_for)
        self.party_two_for = int(party_two_for)
        self.party_two_against = int(50 - party_two_for)
        self.verdict = verdict
        self.dominator = dominator
        self.total_for = int(party_one_for) + int(party_two_for)
        self.total_against = self.party_one_against + self.party_two_against

### This will generate a random voteshare for each of the two parties, regardless of condition assigned. It will also define the winning party, and whether or not the legislation passes. All of this will be then instantiated as an object of class VoteShare.

def random_party_votes():
    party_one_for = random.randint(0,50)
    party_two_for = random.randint(0,50)
    if int(party_one_for + party_two_for >= 51):
        verdict = "pass"
    else:
        verdict = "fail"
    if party_one_for > party_two_for:
        dominator = "party_one"
    elif party_one_for < party_two_for:
        dominator = "party_two"
    else:
        dominator = "tie"
    TrialVote = VoteShare(party_one_for,party_two_for,verdict,dominator)
    return TrialVote

### This will determine which of the 10 predetermined coordinates will be tested

def control_party_votes(n):
    if int(n) == 1:
        TrialVote = VoteShare(0,0,"fail","tie")
    elif int(n) == 2:
        TrialVote = VoteShare(1,1,"fail","tie")
    elif int(n) == 3:
        TrialVote = VoteShare(50,0,"fail","party_one")
    elif int(n) == 4:
        TrialVote = VoteShare(25,25,"fail","tie")
    elif int(n) == 5:
        TrialVote = VoteShare(50,25,"pass","party_one")
    elif int(n) == 6:
        TrialVote = VoteShare(0,50,"fail","party_two")
    elif int(n) == 7:
        TrialVote = VoteShare(25,50,"pass","party_two")
    elif int(n) == 8:
        TrialVote = VoteShare(50,50,"pass","tie")
    elif int(n) == 9:
        TrialVote = VoteShare(25,0,"fail","party_one")
    else:
        TrialVote = VoteShare(0,25,"fail","party_two")
    return TrialVote

### The full random stimuli generator

def generate_stimuli():
    trial_condition = condition()
    if trial_condition == "american":
        party_one_name = "Democrat"
        party_two_name = "Replican"
    else:
        party_one_name = "Flot"
        party_two_name = "Tolf"
    chance = random.randint(1,15)
    if int(chance) < 10:
        trial_vote = control_party_votes(chance)
    else:
        trial_vote = random_party_votes()
    ###Here's all the printing; this can be changed to an object of a new class for the purposes of stimuli creation. This is for visualisation purposes only
    print(f'Condition: {trial_condition}')
    print('')
    print(f'{party_one_name} Votes For: {trial_vote.party_one_for}')
    print(f'{party_one_name} Votes Against: {trial_vote.party_one_against}')
    print('')
    print(f'{party_two_name} Votes For: {trial_vote.party_two_for}')
    print(f'{party_two_name} Votes Against: {trial_vote.party_two_against}')
    print('')
    print(f'Votes: {trial_vote.total_for}-{trial_vote.total_against}')
    print('')
    print(f'Vedict: {trial_vote.verdict}')

    if trial_vote.dominator == "party_one":
        print(f'Majority Party: {party_one_name} Party')
    elif trial_vote.dominator == "party_two":
        print(f'Majority Party: {party_two_name} Party')
    else:
        print('Majority Party: None')







### TEST CODE

generate_stimuli()

# test_vote = random_party_votes()
#
# print(test_vote.party_two_for, test_vote.party_one_for, test_vote.party_two_against, test_vote.party_one_against, test_vote.verdict, test_vote.dominator)
