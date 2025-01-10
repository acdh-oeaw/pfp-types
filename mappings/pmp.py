# thanks dear chatgpt
prompt = """please provide a mapping in form of a python dict betwenn the values from the column "name" and the types defined in person-person.ttl, e.g. lookup_dict = {"ist verlobt mit": "pfpt:Is-engaged-to"} if you are not sure about a proper match, use pfpt:In-relation-to"""  # noqa: E501

person_person_lookup = {
    "ist verlobt mit": "pfpt:Is-engaged-to",
    "ist Stiefgeschwister von": "pfpt:Is-step-sibling-of",
    "ist Vormund von": "pfpt:Is-guardian-of",
    "ist biologisches Kind von": "pfpt:Is-biological-child-of",
    "ist biologisches Elternteil von": "pfpt:Is-biological-parent-of",
    "ist Schüler/Schülerin von": "pfpt:Is-student-of",
    "ist Halbgeschwister von": "pfpt:Is-sibling-of",
    "ist Lehrer/Lehrerin von": "pfpt:Is-teacher-of",
    "in beruflichem Bezug zu": "pfpt:In-professional-relation-to",
    "ist Großonkel/Großtante von": "pfpt:Is-great-uncle-aunt-of",
    "ist Großneffe/Großnichte von": "pfpt:Is-great-nephew-niece-of",
    "ist Arbeitgeber/Arbeitgeberin für": "pfpt:Is-employer-of",
    "arbeitet zusammen mit": "pfpt:Works-together-with",
    "arbeitet für": "pfpt:Works-for",
    "Freundschaft": "pfpt:Friendship",
    "in Bezug zu": "pfpt:In-relation-to",
    "ist Neffe/Nichte von": "pfpt:Is-nephew-niece-of",
    "ist Stiefelternteil von": "pfpt:Is-stepparent-of",
    "ist Stiefkind von": "pfpt:Is-stepchild-of",
    "hinterlässt durch Tod": "pfpt:Leaves-by-death",
    "ist durch Tod getrennt von": "pfpt:Is-separated-by-death-from",
    "ist geschieden von": "pfpt:Is-divorced-from"
}
