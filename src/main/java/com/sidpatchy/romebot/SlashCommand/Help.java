package com.sidpatchy.romebot.SlashCommand;

import com.sidpatchy.romebot.Embed.HelpEmbed;
import org.javacord.api.event.interaction.SlashCommandCreateEvent;
import org.javacord.api.interaction.SlashCommandInteraction;
import org.javacord.api.listener.interaction.SlashCommandCreateListener;

public class Help implements SlashCommandCreateListener {

    /**
     * Command to provide RomeBot's help command
     *
     * @param event
     */
    @Override
    public void onSlashCommandCreate(SlashCommandCreateEvent event) {
        SlashCommandInteraction slashCommandInteraction = event.getSlashCommandInteraction();
        String commandName = slashCommandInteraction.getCommandName();
        if (commandName.equalsIgnoreCase("help")) {
            String command = slashCommandInteraction.getFirstOptionStringValue().orElse("help");
            slashCommandInteraction.createImmediateResponder()
                    .addEmbed(HelpEmbed.getHelp(command))
                    .respond();
        }
    }
}
