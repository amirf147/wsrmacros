
# wsrmacros

> **Note:** This repository contains macros for the Microsoft program, Windows Speech Recognition Macros. This program is no longer officially available and would have to be found from alternate sources. Windows Speech Recognition Macros was a tool developed by Microsoft that allowed users to create custom voice commands for their computer, automate repetitive tasks, and even control their computer using their voice. It was a powerful tool for accessibility and productivity. However, please be aware that the macros in this repository will not work without this specific program.

## Six Key Press or Key Combo Streamer

This collection of macros features a 6 Key Press or Key Combo Streamer in the file `global-keyboard-shortcuts.WSRMac`.

It is a feature that recognizes a sequence of six key presses or key combinations. The structure is based on the XML syntax used in the speech grammar specification for Windows Speech Recognition. One of the six key presses or key combinations that gets executed can also be a free dictation of up to 30 words.

Each sequence is represented by a P (Phrase) element in the tree. P stands for Phrase, which is a sequence of words that the speech recognition system should listen for. Each P in the tree is a phrase that’s waiting to be recognized. Technically, each P in this case is optional as well because each of its contents consist of only O elements.

O stands for Option, which is a choice between different phrases or rules that the speech recognition system can recognize. Except for the first one, Each P has several O (Option) elements within it.

Here’s a breakdown of the options

1. **PRESS**: This is an optional word that can be uttered at the beginning to increase recognition accuracy thereby better activating the streamer.
2. **JUST TYPE**: This new option allows you to dictate up to 30 words at any point in the command sequence.
3. **Text Manipulation Key Combo**: If the user speaks this, the system will recognize it and perform the corresponding action. The user can also specify a number that represents how many times that key combo gets repeated.
4. **Key Combo**: This key combo only gets pressed one time. That’s why there is no second option for how many times it gets pressed.
5. **Keyboard Key**: This is a sequence of letters, numbers, and symbols and the user can specify up to 10 of them.
6. **ALL CAPS**: To activate this, the user has to preface the option with the keyword “ALL CAPS”. Afterwards, the system will accept a total of 10 capital letters.
7. **NUMBER**: To activate this, the user has to preface the option with the keyword “NUMBER”. Afterwards, the system will accept a sequence of 1 to 10 numbers.



```
Command
└── Rule
    ├── O ─ P: PRESS (Optional word that can be uttered at the beginning to increase recognition accuracy)
    ├── P
    │   ├── O
    │   │   ├── P: JUST TYPE 
    │   │   └── P: Free dictation of up to 30 words
    │   ├── O
    │   │   ├── P: TextManipulation
    │   │   └── O: Number between 1 and 20
    │   ├── O ─ P: KeyCombo2
    │   ├── O
    │   │   └── P: Keyboard Key (min=1, max=10)
    │   ├── O
    │   │   ├── P: ALL CAPS
    │   │   └── P: capitalLetters (min=1, max=10)
    │   └── O
    │       ├── P: NUMBER
    │       └── P: Number between 0 and 9 (min=1, max=10)
    ├── P
    │   ├── O
    │   │   ├── P: JUST TYPE 
    │   │   └── P: Free dictation of up to 30 words
    │   ├── O
    │   │   ├── P: TextManipulation
    │   │   └── O: Number between 1 and 20
    │   ├── O ─ P: KeyCombo2
    │   ├── O
    │   │   └── P: Keyboard Key (min=1, max=10)
    │   ├── O
    │   │   ├── P: ALL CAPS
    │   │   └── P: capitalLetters (min=1, max=10)
    │   └── O
    │       ├── P: NUMBER
    │       └── P: Number between 0 and 9 (min=1, max=10)
    ├── P
    │   ├── O
    │   │   ├── P: JUST TYPE 
    │   │   └── P: Free dictation of up to 30 words
    │   ├── O
    │   │   ├── P: TextManipulation
    │   │   └── O: Number between 1 and 20
    │   ├── O ─ P: KeyCombo2
    │   ├── O
    │   │   └── P: Keyboard Key (min=1, max=10)
    │   ├── O
    │   │   ├── P: ALL CAPS
    │   │   └── P: capitalLetters (min=1, max=10)
    │   └── O
    │       ├── P: NUMBER
    │       └── P: Number between 0 and 9 (min=1, max=10)
    ├── P
    │   ├── O
    │   │   ├── P: JUST TYPE 
    │   │   └── P: Free dictation of up to 30 words
    │   ├── O
    │   │   ├── P: TextManipulation
    │   │   └── O: Number between 1 and 20
    │   ├── O ─ P: KeyCombo2
    │   ├── O
    │   │   └── P: Keyboard Key (min=1, max=10)
    │   ├── O
    │   │   ├── P: ALL CAPS
    │   │   └── P: capitalLetters (min=1, max=10)
    │   └── O
    │       ├── P: NUMBER
    │       └── P: Number between 0 and 9 (min=1, max=10)
    └── P
        ├── O
        │   ├── P: JUST TYPE 
        │   └── P: Free dictation of up to 30 words
        ├── O
        │   ├── P: TextManipulation
        │   └── O: Number between 1 and 20
        ├── O ─ P: KeyCombo2
        ├── O
        │   └── P: Keyboard Key (min=1, max=10)
        ├── O
        │   ├── P: ALL CAPS
        │   └── P: capitalLetters (min=1, max=10)
        └── O
            ├── P: NUMBER
            └── P: Number between 0 and 9 (min=1, max=10)
```

## Setup

Before you start using this repository, you need to set up your local environment. Follow these steps:

1. **Install Windows Speech Recognition Macros**: Using these macros requires that you have Windows Speech Recognition Macros installed on your system. If you haven't installed it yet, please do so before proceeding. This should automatically create a "Speech Macros" folder in your Documents directory.

2. **Prepare the Speech Macros folder**: Navigate to the "Speech Macros" folder in your Documents directory and make sure that it's empty.

3. **Clone the repository**: Open a terminal, navigate to the "Speech Macros" folder, and clone the repository with the following command:

```bash
git clone https://github.com/amirf147/wsrmacros.git .
```
4. **Add lines to your `.git/config` file**: Add the following lines to your `.git/config` file:

```bash
[filter "removesig"]
    clean = "sed '/<signature>/,/<\/signature>/d'"
    smudge = cat
    required
```

This sets up a filter called "removesig" that removes lines between `<signature>` and `</signature>` (replace these with your actual signature tags) when you run `git add`.

5. **Update your `.gitattributes` file**: Add this line to your `.gitattributes` file (create it in the same directory as your `.gitignore` if it doesn't exist):

```bash
*.WSRmac filter=removesig
```

This tells Git to use the "removesig" filter for all files with the `.WSRmac` extension.
Now you're ready to start using and updating your own version of the repository!

## Parsing Scripts

This repository includes a folder named `parsing_scripts`. This folder contains scripts that are functional but not fully fleshed out. They are designed to help with getting the macros into an Excel or a spreadsheet file, making it easier to view and understand the macros and keyboard shortcuts you have.

While these scripts are operational and can accomplish most tasks, they are not fully featured. This means they might not perform all the functionalities originally intended. However, they are still a valuable tool for managing and understanding your macros.

Please note that these scripts are a work in progress and improvements may be added over time.

## Acknowledgements

I would like to express my profound gratitude to @leeorhelps for his invaluable contributions to the field of Windows Speech Recognition macros with his project at [SpeechBird](https://github.com/leeorhelps/SpeechBird). His comprehensive collection of macros, generously shared on GitHub, has been instrumental in my understanding of how Windows Speech Recognition macros function. Without his pioneering work, the progress I’ve made would not have been possible. Thank you, Leeor, for your significant role in this journey.
