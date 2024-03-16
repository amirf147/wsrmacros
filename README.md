
# wsrmacros

## Acknowledgements

I would like to express my profound gratitude to @leeorhelps for his invaluable contributions to the field of Windows Speech Recognition macros with his project at [SpeechBird](https://github.com/leeorhelps/SpeechBird). His comprehensive collection of macros, generously shared on GitHub, has been instrumental in my understanding of how Windows Speech Recognition macros function. Without his pioneering work, the progress I’ve made would not have been possible. Thank you, Leeor, for your significant role in this journey.

> **Note:** This repository contains macros for Windows Speech Recognition. If you're cloning this repository, please follow the setup instructions below to ensure the macros work correctly on your machine.

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


