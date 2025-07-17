from os.path import exists
import re


def generate_invitations(template_content: str, attendees: dict):

    keyList = []
    pattern = r"\{[^}]*\}"
    attendee_index = 0
    original_content = template_content

    for dicts in attendees:
        for keys in dicts:
            keyList.append(keys)
            keyList = list(dict.fromkeys(keyList))

    matches = re.findall(pattern, template_content)

    while attendee_index < (len(attendees)):
        template_content = original_content

        for match in matches:
            for key in keyList:

                braced_key = f"{{{key}}}"

                if (match == braced_key):
                    value = attendees[attendee_index][key]

                    try:
                        template_content = template_content.replace(
                            match,
                            value
                            )
                    except (TypeError, KeyError):
                        value = 'N/A'
                        template_content = template_content.replace(
                            match,
                            value
                            )

        file_name = f"output_{str(attendee_index + 1)}.txt"

        if template_content:
            with open(file_name, "w") as f:
                f.write(template_content)
        attendee_index = attendee_index + 1
