#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
    
with open("/Users/melvpaul/Documents/100 days of code/Python/Mail Merge Project Start/Input/Names/invited_names.txt", "r") as s:
    names = s.readlines()

for i in range(len(names)):
    re = names[i]
    re = re.strip()
    with open("/Users/melvpaul/Documents/100 days of code/Python/Mail Merge Project Start/Input/Letters/starting_letter.txt", "r+") as f:
        content = f.read()
        new = content.replace("[name]", re)
    with open(f"/Users/melvpaul/Documents/100 days of code/Python/Mail Merge Project Start/Output/ReadyToSend/Letter_for_{re}.txt", "w") as d:
        d.write(new)
        
    