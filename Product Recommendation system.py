# Simple Recommendation System - Easy to Understand

import random

# Database of items
items = {
    'movies': {
        'action': ['The Dark Knight', 'John Wick', 'Die Hard'],
        'comedy': ['The Hangover', 'Superbad', 'Step Brothers'],
        'romance': ['The Notebook', 'Titanic', 'La La Land']
    },
    'books': {
        'fiction': ['The Great Gatsby', '1984', 'To Kill a Mockingbird'],
        'science': ['A Brief History of Time', 'Cosmos', 'The Selfish Gene'],
        'fantasy': ['Harry Potter', 'The Hobbit', 'Game of Thrones']
    }
}

def get_user_preference():
    print("\nWhat do you want recommendations for?")
    print("1. Movies")
    print("2. Books")
    
    choice = input("Enter 1 or 2: ")
    if choice == '1':
        return 'movies'
    elif choice == '2':
        return 'books'
    else:
        print("Invalid choice. Defaulting to movies.")
        return 'movies'

def get_category(category_type):
    print(f"\nWhat {category_type} genre do you like?")
    categories = list(items[category_type].keys())
    for i, cat in enumerate(categories, 1):
        print(f"{i}. {cat.capitalize()}")
    
    choice = input("Enter number: ")
    try:
        idx = int(choice) - 1
        if 0 <= idx < len(categories):
            return categories[idx]
    except:
        pass
    
    print("Invalid choice. Picking random genre.")
    return random.choice(categories)

def recommend_items(category_type, genre, count=3):
    """Get recommendations"""
    available = items[category_type][genre]
    return random.sample(available, min(count, len(available)))

# Main program
print("=" * 40)
print("SIMPLE RECOMMENDATION SYSTEM")
print("=" * 40)

running = True
while running:
    # Get user preferences
    category_type = get_user_preference()
    genre = get_category(category_type)
    
    # Get recommendations
    recommendations = recommend_items(category_type, genre)
    
    # Display results
    print(f"\nRecommended {genre.capitalize()} {category_type}:")
    print("-" * 30)
    for i, item in enumerate(recommendations, 1):
        print(f"{i}. {item}")
    print("-" * 30)
    
    # Ask to continue
    print("\nOptions:")
    print("1. Get more recommendations")
    print("2. Exit")
    
    choice = input("Your choice (1-2): ")
    if choice == '2':
        running = False
        print("\nThanks for using the recommendation system!")
    else:
        continue