import random
import time
from datetime import datetime

class SimpleChatbot:
    def __init__(self, name="ChatBot"):
        self.name = name
        self.user_name = None
        self.conversation_count = 0
        self.mood = "happy"  # happy, tired, excited
        
        # Response patterns organized by categories
        self.responses = {
            'greetings': {
                'patterns': ['hello', 'hi', 'hey', 'good morning', 'good afternoon', 'good evening', 'howdy', 'greetings'],
                'replies': [
                    "Hello there! How can I help you today?",
                    "Hi! Great to see you!",
                    "Hey! What's on your mind?",
                    "Hello! Hope you're having a wonderful day!",
                    "Hi there! Ready to chat?"
                ]
            },
            'how_are_you': {
                'patterns': ['how are you', 'how do you feel', 'how are things', 'whats up', "what's up", 'how have you been'],
                'replies': [
                    "I'm doing great, thanks for asking! How about you?",
                    "I'm fantastic! Ready to help and chat!",
                    "Feeling good today! What about yourself?",
                    "I'm in a great mood! How are you doing?",
                    "Excellent! Thanks for asking. How's your day going?"
                ]
            },
            'name_questions': {
                'patterns': ['what is your name', 'whats your name', "what's your name", 'who are you', 'your name'],
                'replies': [
                    f"I'm {self.name}, your friendly chatbot assistant!",
                    f"My name is {self.name}. Nice to meet you!",
                    f"I go by {self.name}. What should I call you?",
                    f"You can call me {self.name}! What's your name?"
                ]
            },
            'age_questions': {
                'patterns': ['how old are you', 'what is your age', 'whats your age', 'your age'],
                'replies': [
                    "I'm as old as my code - timeless and always learning!",
                    "Age is just a number for a chatbot like me!",
                    "I was born when my program started, so pretty young!",
                    "I don't age like humans do - I just get smarter!"
                ]
            },
            'compliments': {
                'patterns': ['you are great', 'you are awesome', 'you are cool', 'you are nice', 'good job', 'well done', 'amazing', 'fantastic'],
                'replies': [
                    "Aww, thank you so much! You're pretty awesome too!",
                    "That's so kind of you to say! You made my day!",
                    "Thanks! I really appreciate the compliment!",
                    "You're too nice! Thank you!",
                    "That means a lot to me! You're wonderful too!"
                ]
            },
            'help_requests': {
                'patterns': ['help', 'can you help', 'i need help', 'assist me', 'support'],
                'replies': [
                    "Of course! I'm here to help. What do you need assistance with?",
                    "I'd be happy to help! What can I do for you?",
                    "Sure thing! How can I assist you today?",
                    "Help is on the way! What's the problem?",
                    "I'm here to help! What's troubling you?"
                ]
            },
            'time_questions': {
                'patterns': ['what time', 'current time', 'time now', 'what is the time'],
                'replies': []  # Will be handled specially with actual time
            },
            'weather': {
                'patterns': ['weather', 'how is the weather', 'is it raining', 'sunny', 'cloudy'],
                'replies': [
                    "I wish I could check the weather for you, but I don't have access to weather data!",
                    "I can't see outside, but I hope it's beautiful weather wherever you are!",
                    "Weather updates aren't my specialty, but I hope you're enjoying nice weather!",
                    "I'd love to tell you about the weather, but that's beyond my capabilities right now!"
                ]
            },
            'jokes': {
                'patterns': ['tell me a joke', 'joke', 'make me laugh', 'funny', 'humor'],
                'replies': [
                    "Why don't programmers like nature? It has too many bugs! 😄",
                    "I told my computer a joke about UDP... but I'm not sure it got it! 😂",
                    "Why do Python programmers prefer snakes? Because they don't like Java! 🐍",
                    "How many programmers does it take to change a light bulb? None, that's a hardware problem! 💡",
                    "Why did the chatbot go to therapy? It had too many issues to resolve! 🤖"
                ]
            },
            'goodbye': {
                'patterns': ['bye', 'goodbye', 'see you later', 'farewell', 'exit', 'quit', 'leave', 'see ya'],
                'replies': [
                    "Goodbye! It was great chatting with you!",
                    "See you later! Have a wonderful day!",
                    "Farewell! Come back anytime!",
                    "Bye! Thanks for the lovely conversation!",
                    "Take care! Hope to chat again soon!"
                ]
            },
            'thanks': {
                'patterns': ['thank you', 'thanks', 'appreciate it', 'grateful'],
                'replies': [
                    "You're very welcome! Happy to help!",
                    "No problem at all! Glad I could assist!",
                    "You're welcome! That's what I'm here for!",
                    "My pleasure! Always happy to help!",
                    "Don't mention it! Anytime!"
                ]
            }
        }
        
        # Default responses for unrecognized input
        self.default_responses = [
            "That's interesting! Can you tell me more?",
            "I'm not sure I understand. Could you rephrase that?",
            "Hmm, that's a new one for me! Can you explain?",
            "I'd love to learn more about what you mean!",
            "That sounds intriguing! Tell me more!",
            "I'm still learning. Can you help me understand?",
            "Interesting perspective! What makes you say that?",
            "I'm curious to know more about your thoughts on that!"
        ]
    
    def normalize_input(self, user_input):
        """Clean and normalize user input for better pattern matching."""
        # Convert to lowercase and strip whitespace
        normalized = user_input.lower().strip()
        
        # Remove common punctuation
        import string
        normalized = normalized.translate(str.maketrans('', '', string.punctuation))
        
        return normalized
    
    def get_current_time(self):
        """Get current time formatted nicely."""
        now = datetime.now()
        return now.strftime("It's currently %I:%M %p on %A, %B %d, %Y")
    
    def find_response_category(self, user_input):
        """Find which category the user input matches."""
        normalized_input = self.normalize_input(user_input)
        
        # Check each category for pattern matches
        for category, data in self.responses.items():
            for pattern in data['patterns']:
                if pattern in normalized_input:
                    return category
        
        return None
    
    def get_response(self, user_input):
        """Generate appropriate response based on user input."""
        self.conversation_count += 1
        
        # Handle special cases first
        if self.normalize_input(user_input) in ['quit', 'exit', 'bye', 'goodbye']:
            return 'goodbye'
        
        # Find matching category
        category = self.find_response_category(user_input)
        
        if category:
            # Handle special categories
            if category == 'time_questions':
                return self.get_current_time()
            elif category == 'goodbye':
                return random.choice(self.responses[category]['replies'])
            else:
                # Get random response from matched category
                response = random.choice(self.responses[category]['replies'])
                
                # Add personality based on conversation count
                if self.conversation_count > 10:
                    personality_additions = [
                        " We've been chatting for a while now!",
                        " I'm enjoying our conversation!",
                        " You're a great conversationalist!",
                        ""
                    ]
                    response += random.choice(personality_additions)
                
                return response
        else:
            # Return default response for unrecognized input
            return random.choice(self.default_responses)
    
    def ask_for_name(self):
        """Ask for user's name if not already known."""
        if not self.user_name:
            name_prompts = [
                "By the way, what should I call you?",
                "I'd love to know your name!",
                "What's your name, if you don't mind me asking?"
            ]
            return random.choice(name_prompts)
        return None
    
    def typing_effect(self, text, delay=0.03):
        """Simulate typing effect for more natural conversation."""
        for char in text:
            print(char, end='', flush=True)
            time.sleep(delay)
        print()  # New line after complete text
    
    def display_welcome(self):
        """Display welcome message and instructions."""
        welcome_msg = f"""
{'='*60}
🤖 WELCOME TO {self.name.upper()}! 🤖
{'='*60}
Hello! I'm your friendly rule-based chatbot assistant!
I can chat about various topics including:

• Greetings and small talk
• Questions about me
• Current time
• Jokes and humor
• General conversation

Type 'help' for assistance or 'quit' to exit.
Let's start chatting!
{'='*60}
"""
        print(welcome_msg)
    
    def display_help(self):
        """Display help information."""
        help_msg = """
🆘 CHATBOT HELP 🆘
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Things you can try:
• Say hello: "hi", "hello", "hey"
• Ask how I am: "how are you?"
• Ask my name: "what's your name?"
• Request jokes: "tell me a joke"
• Ask for time: "what time is it?"
• Say thanks: "thank you"
• Say goodbye: "bye", "goodbye", "quit"

I understand natural language, so feel free to chat normally!
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
"""
        print(help_msg)
    
    def chat(self):
        """Main chat loop."""
        self.display_welcome()
        
        while True:
            try:
                # Get user input
                user_input = input(f"\n{'You:':<8} ").strip()
                
                # Check for empty input
                if not user_input:
                    print(f"{self.name}:   Please say something! I'm here to chat! 😊")
                    continue
                
                # Check for help command
                if self.normalize_input(user_input) in ['help', 'assist', 'commands']:
                    self.display_help()
                    continue
                
                # Check if user is providing their name
                if self.user_name is None and len(user_input.split()) == 1 and user_input.isalpha():
                    self.user_name = user_input.title()
                    response = f"Nice to meet you, {self.user_name}! How can I help you today?"
                else:
                    # Get bot response
                    response = self.get_response(user_input)
                
                # Check if it's time to end conversation
                if self.find_response_category(user_input) == 'goodbye':
                    print(f"{self.name}:   ", end="")
                    self.typing_effect(response)
                    break
                
                # Display bot response with typing effect
                print(f"{self.name}:   ", end="")
                self.typing_effect(response)
                
                # Occasionally ask for name or add personality
                if random.random() < 0.1:  # 10% chance
                    name_prompt = self.ask_for_name()
                    if name_prompt:
                        print(f"{self.name}:   ", end="")
                        self.typing_effect(name_prompt)
                
            except KeyboardInterrupt:
                print(f"\n\n{self.name}: Goodbye! Thanks for chatting! 👋")
                break
            except Exception as e:
                print(f"{self.name}: Oops! Something went wrong. Let's keep chatting! 😅")

def main():
    """Main function to run the chatbot."""
    # Create and start chatbot
    bot_name = input("Enter a name for your chatbot (or press Enter for 'ChatBot'): ").strip()
    if not bot_name:
        bot_name = "ChatBot"
    
    chatbot = SimpleChatbot(bot_name)
    chatbot.chat()
    
    # Display conversation stats
    print(f"\n📊 Chat Statistics:")
    print(f"   • Total messages: {chatbot.conversation_count}")
    print(f"   • User name: {chatbot.user_name or 'Not provided'}")
    print(f"   • Thanks for using {chatbot.name}! 🤖")

if __name__ == "__main__":
    main()