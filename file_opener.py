file_system = [
    [
        "nothing.txt",
        "dog_pic.png",
        [
            "secret_plan.pdf"
        ]
    ],
    "notion.app",
    "slack.app",
    [
        "fun.txt",
        [
            "meaningless_file.txt",
            "chicken_dinner.txt"
        ],
        "not_fun.txt"
    ],
    "zoom.app"
]

target = "chicken_dinner.txt"

#each folder is represented as a list
#for this problem we will only ever be dealing with folders (lists) and files (strings).

#open folder
#search through each item in the folder
#and determine if the current item is the target file (base case)
#however items might be subfolders that also need to be search through, (recursive case) .isinstance()
#when you land on a new folder, take yourself back to the top of these instructions


def find_file(file_system, target):

    for item in file_system:
        if item == target: # Base Case
            return f"Found {target}"
        elif isinstance(item, list):
            found = find_file(item, target)
            if found:
                return found
    return None