import json

def parse_jsonl_file(file_path):
    data = []

    with open(file_path, 'r') as file:
        for line in file:
            try:
                json_object = json.loads(line.strip())
                data.append(json_object)
            except json.JSONDecodeError as e:
                print(f"Error parsing JSON in line: {line}")
                print(e)

    return data

def save_to_jsonl_file(file_path, data):
    with open(file_path, 'a') as file:
        for entry in data:
            json.dump(entry, file)
            file.write('\n')

def add_new_entry():
    word = input("Enter the word: ")
    key = input("Enter the key: ")
    pos = input("Enter the part of speech: ")
    synonyms = input("Enter synonyms (comma-separated): ").split(',')

    entry = {
        'word': word.strip(),
        'key': key.strip(),
        'pos': pos.strip(),
        'synonyms': [syn.strip() for syn in synonyms]
    }

    return entry

def get_word_details(word, data):
    word_details = []

    for entry in data:
        if entry.get('word') == word:
            key = entry.get('key')
            pos = entry.get('pos')
            synonyms = entry.get('synonyms', [])
            word_details.append((key, pos, synonyms))
    
    return word_details

def main():
    file_path = 'en_thesaurus.jsonl'
    parsed_data = parse_jsonl_file(file_path)

    while True:
        action = input("Enter 'search' to look up a word, 'add' to add new data, or 'exit' to quit: ")

        if action.lower() == 'exit':
            break
        elif action.lower() == 'search':
            search_word = input("Enter a word: ").lower()
            word_details = get_word_details(search_word, parsed_data)

            if word_details:
                print(f"Word: {search_word}")
                for index, (key, pos, synonyms) in enumerate(word_details, start=1):
                    print(f"Meaning {index}:")
                    print(f"  Key: {key}")
                    print(f"  Part of Speech: {pos}")
                    print(f"  Synonyms: {', '.join(synonyms)}")
            else:
                print(f"No information found for the word '{search_word}'.")
        elif action.lower() == 'add':
            new_entry = add_new_entry()
            parsed_data.append(new_entry)
            save_to_jsonl_file(file_path, [new_entry])
            print("Data added successfully!")
        else:
            print("Invalid action. Please enter 'search', 'add', or 'exit'.")
        print()

if __name__ == "__main__":
    main()
