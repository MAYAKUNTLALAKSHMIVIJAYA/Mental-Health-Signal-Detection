def get_suggestions(emotion):

    emotion = emotion.lower()

    suggestions = {

        # ---------------- POSITIVE ----------------
        "joy": {
            "movies": ["3 Idiots", "Zindagi Na Milegi Dobara", "The Pursuit of Happyness"],
            "songs": ["Happy - Pharrell Williams", "On Top of the World", "Ilahi"],
            "poems": ["Leisure - William Henry Davies", "A Happy Man"],
            "motivation": [
                "Keep spreading positivity.",
                "Celebrate small wins.",
                "Use happiness to fuel your goals."
            ]
        },

        "love": {
            "movies": ["Titanic", "Before Sunrise", "La La Land"],
            "songs": ["Perfect - Ed Sheeran", "Tum Hi Ho", "All of Me"],
            "poems": ["How Do I Love Thee - Elizabeth Browning"],
            "motivation": [
                "Express love freely.",
                "Appreciate meaningful connections.",
                "Kindness always returns."
            ]
        },

        "gratitude": {
            "movies": ["Pay It Forward", "The Blind Side"],
            "songs": ["Thank You - Dido", "Grateful"],
            "poems": ["Be Thankful"],
            "motivation": [
                "Gratitude multiplies happiness.",
                "Appreciate what you have.",
                "Small thanks create big impact."
            ]
        },

        "optimism": {
            "movies": ["Rocky", "Lakshya"],
            "songs": ["Hall of Fame", "Unstoppable"],
            "poems": ["Dreams - Langston Hughes"],
            "motivation": [
                "Stay hopeful.",
                "Great things take time.",
                "Keep moving forward."
            ]
        },

        "pride": {
            "movies": ["Chak De India", "Dangal"],
            "songs": ["Unstoppable", "Believer"],
            "poems": ["Invictus"],
            "motivation": [
                "Be proud of your growth.",
                "Confidence builds success.",
                "Keep achieving."
            ]
        },

        # ---------------- NEGATIVE ----------------
        "sadness": {
            "movies": ["Taare Zameen Par", "A Beautiful Mind"],
            "songs": ["Fix You", "Let Her Go"],
            "poems": ["Still I Rise - Maya Angelou"],
            "motivation": [
                "This moment will pass.",
                "You are not alone.",
                "Healing takes time."
            ]
        },

        "anger": {
            "movies": ["Batman Begins", "Gladiator"],
            "songs": ["Lose Yourself", "Stronger"],
            "poems": ["If - Rudyard Kipling"],
            "motivation": [
                "Control is real strength.",
                "Breathe before reacting.",
                "Use anger as energy."
            ]
        },

        "fear": {
            "movies": ["Harry Potter", "Life of Pi"],
            "songs": ["Unstoppable", "Rise"],
            "poems": ["Invictus"],
            "motivation": [
                "Fear is temporary.",
                "Face one step at a time.",
                "You are stronger than fear."
            ]
        },

        "nervousness": {
            "movies": ["The Social Network"],
            "songs": ["Shake it Off"],
            "poems": ["Try Again"],
            "motivation": [
                "Breathe slowly.",
                "Prepare calmly.",
                "You can handle this."
            ]
        },

        "grief": {
            "movies": ["The Fault in Our Stars"],
            "songs": ["See You Again"],
            "poems": ["Do Not Stand at My Grave and Weep"],
            "motivation": [
                "Allow yourself to heal.",
                "Memories live forever.",
                "Time helps recovery."
            ]
        },

        "disappointment": {
            "movies": ["Pursuit of Happyness"],
            "songs": ["Numb", "Fix You"],
            "poems": ["Try Again"],
            "motivation": [
                "Failure teaches success.",
                "Try again stronger.",
                "Progress takes time."
            ]
        },

        "remorse": {
            "movies": ["Atonement"],
            "songs": ["Sorry"],
            "poems": ["Mistakes"],
            "motivation": [
                "Learn and grow.",
                "Forgive yourself.",
                "Move forward stronger."
            ]
        },

        # ---------------- NEUTRAL ----------------
        "neutral": {
            "movies": ["Forrest Gump", "Interstellar"],
            "songs": ["Let it be", "Perfect"],
            "poems": ["Road Not Taken"],
            "motivation": [
                "Stay balanced.",
                "Focus on growth.",
                "Consistency wins."
            ]
        },

        "surprise": {
            "movies": ["Inception", "Avengers"],
            "songs": ["Counting Stars"],
            "poems": ["Dreams"],
            "motivation": [
                "Embrace change.",
                "Stay curious.",
                "Growth comes from surprises."
            ]
        },

        "confusion": {
            "movies": ["Inception"],
            "songs": ["Boulevard of Broken Dreams"],
            "poems": ["The Road Not Taken"],
            "motivation": [
                "Clarity comes with time.",
                "Take one step at a time.",
                "Seek guidance if needed."
            ]
        },

        "curiosity": {
            "movies": ["Interstellar"],
            "songs": ["A Sky Full of Stars"],
            "poems": ["Explore"],
            "motivation": [
                "Keep learning.",
                "Curiosity builds intelligence.",
                "Ask questions."
            ]
        },

        "realization": {
            "movies": ["The Matrix"],
            "songs": ["Numb"],
            "poems": ["Awakening"],
            "motivation": [
                "Awareness brings growth.",
                "Learn and evolve.",
                "Every realization matters."
            ]
        }
    }

    # default suggestions
    default = {
        "movies": ["The Pursuit of Happyness"],
        "songs": ["Hall of Fame"],
        "poems": ["If - Rudyard Kipling"],
        "motivation": [
            "Believe in yourself.",
            "Every day is a new chance.",
            "Stay strong and positive."
        ]
    }

    return suggestions.get(emotion, default)