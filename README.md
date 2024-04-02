# lolapialgo

To make sure your stuff work you need to have open ai subscription.

You would need to set up your open AI in your local environment.

From OpenAI API website

# MacOS

Open Terminal: You can find it in the Applications folder or search for it using Spotlight (Command + Space).

Edit Bash Profile: Use the command nano ~/.bash_profile or nano ~/.zshrc (for newer MacOS versions) to open the profile file in a text editor.

Add Environment Variable: In the editor, add the line below, replacing your-api-key-here with your actual API key:

export OPENAI_API_KEY='your-api-key-here'
Save and Exit: Press Ctrl+O to write the changes, followed by Ctrl+X to close the editor.

Load Your Profile: Use the command source ~/.bash_profile or source ~/.zshrc to load the updated profile.

Verification: Verify the setup by typing echo $OPENAI_API_KEY in the terminal. It should display your API key.

# Windows:
Open Command Prompt: You can find it by searching "cmd" in the start menu.

Set environment variable in the current session: To set the environment variable in the current session, use the command below, replacing your-api-key-here with your actual API key:

setx OPENAI_API_KEY "your-api-key-here"
This command will set the OPENAI_API_KEY environment variable for the current session.

Permanent setup: To make the setup permanent, add the variable through the system properties as follows:

Right-click on 'This PC' or 'My Computer' and select 'Properties'.
Click on 'Advanced system settings'.
Click the 'Environment Variables' button.
In the 'System variables' section, click 'New...' and enter OPENAI_API_KEY as the variable name and your API key as the variable value.
Verification: To verify the setup, reopen the command prompt and type the command below. It should display your API key: echo %OPENAI_API_KEY%
