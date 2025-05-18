# IBM Hackathon 2025
### Yes, the word "hackathon" is mispelled in the Organization name. Wasn't me. LOL.

## Welcome

This hackathon is all about learning to leverage GitHub Copilot to drive innovation for our clients.  

All participants have been given access to Copilot Enterprise, which includes all of the currently released features of Copilot and most features that are in preview. You can find out more about the features [here](https://docs.github.com/en/copilot/about-github-copilot/github-copilot-features).

Your team should be created and have Admin access to your repository. You may rename your repository if you like. Reach out to hackathon organizers if you have questions or need help. 

# Azure AI Multi-Agent System

A system that processes user queries through a pipeline of specialized AI agents.

## Features
- Code Reader Agent: Analyzes and explains code
- Diagram Creator Agent: Generates visual representations
- Streamlit frontend for easy interaction

## Project details:

## Setup
1. Clone the repository
2. Create and activate a virtual environment `.\agentenv\Scripts\Activate`
3. Install dependencies: `pip install -r requirements.txt`
4. Create a `.env` file with your Azure details [Agentids, project connection string]
5. Start the backend: `python backend/server.py` in one terminal
6. Start the frontend: `streamlit run frontend/app.py` in another terminal
7. To stop the service - Kill frontend and then kill backend by pressing `ctrl+c`

## Configuration
Edit the `.env` file to configure:
- Azure AI connection string
- Agent IDs

##


## Getting Started

1. [Install the Copilot extensions for your IDE.](https://docs.github.com/en/copilot/using-github-copilot/using-extensions-to-integrate-external-tools-with-copilot-chat)
2. Create an SSH key or a Personal Access Token (PAT) to access your repository. Google is your friend here if you need help. 
3. Clone your repository.
4. Start coding!

## Copilot tips

1. Use `/help` in Copilot chat to get a list of commands.
2. Take a minute to examine the UI around Copilot chat. There are some great features that are easy to miss, such as the model selection dropdown and the ability to change the context of the chat.
3. Context is everything. In chat, you can delete bad prompts that produced bad responses, and this will improve the quality of the responses you get in the future.
4. By default, Copilot uses the context of your current file, specifically the viewport of your editor. You can use `#file` to specify an entire file, and you can add more than 1 file to the context this way. 
5. Don't forget to use Copilot Chat in GitHub itself. Using this, [you can add personal instructions to Copilot](https://docs.github.com/en/copilot/customizing-copilot/adding-personal-custom-instructions-for-github-copilot) that will help it understand your preferences and style. 

## Video Resources

* [Essentials](https://www.youtube.com/watch?v=b5xcWdzAB5c&list=PL0lo9MOBetEHEHi9h0k_lPn0XZdEeYZDS&index=2)
* [Agent mode](https://www.youtube.com/watch?v=C95drFKy4ss&list=PL0lo9MOBetEHEHi9h0k_lPn0XZdEeYZDS&index=1)
* [Series on Copilot in VS Code ](https://www.youtube.com/watch?v=Fi3AJZZregI&list=PLj6YeMhvp2S5_hvBl2SE-7YCHYlLQ0bPt)
* [GitHub's Copilot Playlist](https://youtube.com/playlist?list=PL0lo9MOBetEHEHi9h0k_lPn0XZdEeYZDS&si=ktHbJpkKZkHrA2WS)
* [GitHub's YouTube Channel](https://www.youtube.com/@GitHub)

## Don't Forget!

In this GitHub environment, we have access to all the toys that IBM's internal GitHub doesn't have yet. So that means you can utilize:

* GitHub Actions ([docs](https://docs.github.com/en/actions))
* GitHub Advanced Security ([docs](https://docs.github.com/en/get-started/learning-about-github/about-github-advanced-security))
* GitHub Codepsaces ([docs](https://docs.github.com/en/codespaces))

With Advanced Security in particular, you can take advantage of Copilot Autofix to automatically fix security vulnerabilities in your code.

Check GitHub's YouYube channel linked above for more information on these features or dive into the docs.
