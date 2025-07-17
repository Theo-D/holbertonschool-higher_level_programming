def generate_invitations(template_content: str, attendees: list):

    if not isinstance(attendees, list) or not all(isinstance(attendee, dict) for attendee in attendees):
        print("attendees must be of type list")
        return

    if not attendees:
        print("attendees must not be empty")
        return

    if not isinstance(template_content, str):
        print("template_content must be of type str")
        return

    if not template_content.strip():
        print("template_content must not be empty")
        return

    keyList = []

    for dicts in attendees:
        for keys in dicts:
            keyList.append(keys)
            keyList = list(dict.fromkeys(keyList))

    for i in range(len(attendees)):
        new_template = template_content
        for key in keyList:
                try:
                    value = attendees[i][key]
                    new_template = new_template.replace(f"{{{key}}}", value)
                except (TypeError, KeyError):
                    value = 'N/A'
                    new_template = new_template.replace(f"{{{key}}}", value)

        file_name = f"output_{str(i + 1)}.txt"

        try:
            with open(file_name, "w") as f:
                f.write(new_template)
        except Exception as e:
            raise Exception('Could not open file')
