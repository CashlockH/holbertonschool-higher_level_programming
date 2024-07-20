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
        file = "output_{}.txt".format(index)
        if os.path.exist(file) is False:
            with open(file, 'w') as f:
                f.write(template.format(name = element["name"] if element["name"] else "name: N/A", event_title = element["event_title"] if element["event_title"] else "event_title: N/A", event_date = element["event_date"] if element["event_date"] else "event_date: N/A", event_location = element["event_location"] if element["event_location"] else "event_location: N/A"))
