# this is legit the most basic fucking BWS calculator in existence

print("===== LEGIT THE MOST BASIC BWS CALCULATOR IN EXISTENCE =====")

rank = int(input("Enter your rank:   "))
badges = int(input("Enter your badge count:   "))

BWS = rank**(0.9937**(badges**2))

print("Your BWS rank: ", BWS)