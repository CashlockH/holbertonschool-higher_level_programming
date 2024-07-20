import os
def generate_invitations(template, attendees):
    if type(template) is not str or type(attendees) is not list:
        print("Invalid input type")
    if not template:
        print("Template is empty, no output files generated.")
        return
    elif not attendees:
        print("No data provided, no output files generated.")
        return
    for index, element in enumerate(attendees):
        file = "output_{}.txt".format(index + 1)
        with open(file, 'w+') as f:
            f.write(template.format(name = checker("name", element),
                                    event_title = checker("event_title", element),
                                    event_date = checker("event_date", element),
                                    event_location = checker("event_location", element)))

def checker(key, dict):
    if key not in dict:
        return "{}: N/A".format(key)
    elif not dict[key]:
        return "N/A"
    else:
        return "{}".format(dict[key])