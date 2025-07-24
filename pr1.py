def ai_perception():
    print("\n[Perception Simulation]")
    image_input = input("Describe what you 'see' (e.g., cat, car, person): ")
    print(f"AI Perception: Detected object is a '{image_input.lower()}'.")

def ai_reasoning():
    print("\n[Reasoning Simulation]")
    symptom = input("Enter your symptom (e.g., fever, cough, headache): ").lower()
    if symptom == "fever":
        print("AI Reasoning: You might have an infection or flu.")
    elif symptom == "cough":
        print("AI Reasoning: You might have a cold or respiratory issue.")
    elif symptom == "headache":
        print("AI Reasoning: You might be stressed or dehydrated.")
    else:
        print("AI Reasoning: Symptom not recognized. Please consult a doctor.")

def ai_learning():
    print("\n[Learning Simulation]")
    known_facts = {
        "apple": "fruit",
        "carrot": "vegetable",
        "rose": "flower"
    }
    item = input("Enter an object (e.g., apple, carrot, rose): ").lower()
    category = known_facts.get(item, "unknown")
    print(f"AI Learning: '{item}' is a {category}.")

def categorize_ai_systems():
    print("\n[Categorization of Intelligent Systems]")
    categories = {
        "Reactive Machines": "React to current input only (e.g., chess engine).",
        "Limited Memory": "Use past data (e.g., self-driving cars).",
        "Theory of Mind": "Understand feelings/intentions (future AI).",
        "Self-aware": "Conscious AI (not yet developed)."
    }
    for system, desc in categories.items():
        print(f"{system}: {desc}")

def real_world_applications():
    print("\n[Real-world Applications of AI]")
    print("1. Healthcare - AI diagnoses based on symptoms or scans.")
    print("2. Finance - AI detects fraudulent transactions.")
    print("3. Virtual Assistants - Chatbots like Siri, Alexa.")
    print("4. Agriculture - AI predicts crop health and yield.")
    print("5. Transport - Self-driving car decision making.")

def main():
    print("=== AI DEMO SYSTEM ===")
    while True:
        print("\nChoose a section to explore:")
        print("1. AI Components (Perception, Reasoning, Learning)")
        print("2. Categorization of Intelligent Systems")
        print("3. Real-world AI Applications")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            ai_perception()
            ai_reasoning()
            ai_learning()
        elif choice == "2":
            categorize_ai_systems()
        elif choice == "3":
            real_world_applications()
        elif choice == "4":
            print("Thank you for exploring AI!")
            break
        else:
            print("Invalid choice. Please enter 1-4.")

if __name__ == "__main__":
    main()
