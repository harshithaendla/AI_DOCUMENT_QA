# AI-BASED DOCUMENT QUESTION ANSWERING SYSTEM

# Step 1: Create Knowledge Base from the document

def create_knowledge_base(filename):

    knowledge_base = {}

    try:
        with open(filename, "r") as file:

            for line in file:

                if ":" in line:
                    key, value = line.split(":", 1)

                    knowledge_base[key.strip().lower()] = value.strip()

        print("Knowledge Base Created Successfully!")

    except FileNotFoundError:
        print("Error: Document not found!")
        return None

    return knowledge_base


# Step 2: Define rules for question processing

rules = {
    "course": ["course", "subject"],
    "course code": ["course code", "code"],
    "department": ["department"],
    "duration": ["duration", "how long"],
    "programming language": ["programming language", "language"],
    "knowledge representation": ["knowledge representation"],
    "search technique": ["search technique", "search method"],
    "reasoning technique": ["reasoning technique", "reasoning method"]
}


# Step 3: Process the question and search the Knowledge Base

def answer_question(question, knowledge_base):

    question = question.lower().strip()

    # Apply predefined rules and keyword matching

    for key, keywords in sorted(
        rules.items(),
        key=lambda item: len(item[0]),
        reverse=True
    ):

        for word in keywords:

            if word in question and key in knowledge_base:

                return "The " + key + " is " + knowledge_base[key] + "."

    # Search for other matching keys

    for key, value in knowledge_base.items():

        if key in question and key not in rules:

            return "The " + key + " is " + value + "."

    # If no matching information is found

    return "Information not found in the document."


# Step 4: Main program

print("-------------------------------------------")
print("AI-BASED DOCUMENT QUESTION ANSWERING SYSTEM")
print("-------------------------------------------")

filename = "sample_document.txt"

# Construct the Knowledge Base

knowledge_base = create_knowledge_base(filename)

# Check whether document is available

if knowledge_base is not None:

    # Accept questions continuously

    while True:

        question = input("\nEnter your question (type exit to stop): ")

        # Exit condition

        if question.lower().strip() == "exit":

            print("Thank you for using the system!")
            break

        # Generate answer

        answer = answer_question(question, knowledge_base)

        print("Answer:", answer)