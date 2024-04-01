
# wsrmacros

> **Note:** This repository contains macros for the Microsoft program, Windows Speech Recognition Macros. This program is no longer officially available and would have to be found from alternate sources. Windows Speech Recognition Macros was a tool developed by Microsoft that allowed users to create custom voice commands for their computer, automate repetitive tasks, and even control their computer using their voice. It was a powerful tool for accessibility and productivity. However, please be aware that the macros in this repository will not work without this specific program.

## Five Key Press or Key Combo Streamer

This collection of macros features a 5 Key Press or Key Combo Streamer in the file `global-keyboard-shortcuts.WSRMac`.

It is a feature that recognizes a sequence of five key presses or key combinations. The structure is based on the XML syntax used in the speech grammar specification for Windows Speech Recognition.

Each sequence is represented by a P (Phrase) element in the tree. P stands for Phrase, which is a sequence of words that the speech recognition system should listen for. Each P in the tree is a phrase that’s waiting to be recognized. Technically, each P in this case is optional as well because each of its contents consist of only O elements.

O stands for Option, which is a choice between different phrases or rules that the speech recognition system can recognize. Each P has several O (Option) elements within it.

Here’s a breakdown of the options within each P:

The first option is a text manipulation key combo. If the user speaks this, the system will recognize it and perform the corresponding action. The user can also specify a number that represents how many times that key combo gets repeated.
The second option is a key combo that only gets pressed one time. That’s why there is no second option for how many times it gets pressed.
The third option is a sequence of letters, numbers, and symbols and the user can specify up to 10 them.
The fourth option is for capital letters. To activate this, the user has to preface the option with the keyword “ALL CAPS”. Afterwards, the system will accept a total of 10 capital letters.
The last option is for numbers. To activate this, the user has to preface the option with the keyword “NUMBER”. Afterwards, the system will accept a sequence of 1 to 10 numbers.

```
Command
└── Rule
    ├── P
    │   ├── O
    │   │   ├── TextManipulation
    │   │   └── O: Number between 1 and 20
    │   ├── O: KeyCombo2
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
    │   │   ├── TextManipulation
    │   │   └── O: Number between 1 and 20
    │   ├── O: KeyCombo2
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
    │   │   ├── TextManipulation
    │   │   └── O: Number between 1 and 20
    │   ├── O: KeyCombo2
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
    │   │   ├── TextManipulation
    │   │   └── O: Number between 1 and 20
    │   ├── O: KeyCombo2
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
        │   ├── TextManipulation
        │   └── O: Number between 1 and 20
        ├── O: KeyCombo2
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
git clone https://github.com/amirf147/WSR_macros.git .
```

3. **Run the setup script**: Run the `setup.sh` script to set up the Git filter that removes the signature block from files when they're staged for commit. You can do this with the following command:

```bashi
./setup.sh
```

Now you're ready to start using the repository!

## Tailoring to Your Use

If you want to tailor this repository to your own use and keep track of updates both locally and remotely, you can fork it and make changes in your forked repository. 

Please note that the `setup.sh` script and the Git filter it sets up are local to your machine. If you clone your forked repository to a new machine, you'll need to run the `setup.sh` script again on that machine.


## Acknowledgements

I would like to express my profound gratitude to @leeorhelps for his invaluable contributions to the field of Windows Speech Recognition macros with his project at [SpeechBird](https://github.com/leeorhelps/SpeechBird). His comprehensive collection of macros, generously shared on GitHub, has been instrumental in my understanding of how Windows Speech Recognition macros function. Without his pioneering work, the progress I’ve made would not have been possible. Thank you, Leeor, for your significant role in this journey.
