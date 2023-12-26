acronyms = {"LOL": "laugh out loud", "IDK": "I don't know", "TBH": "to be honest"}

acronym = "BTW"

try:
    definition = acronyms[acronym]
    print(f"Definition of {acronym} is {definition}")
except:
    print("Key does not exist")
finally:
    print("The acronyms that are defined are:")
    for a in acronyms:
        print(a)
