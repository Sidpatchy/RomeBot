package com.sidpatchy.romebot.SlashCommand;

import com.sidpatchy.romebot.Embed.VersionEmbed;
import org.javacord.api.event.interaction.SlashCommandCreateEvent;
import org.javacord.api.interaction.SlashCommandInteraction;
import org.javacord.api.listener.interaction.SlashCommandCreateListener;

public class Version implements SlashCommandCreateListener {

    /**
     * Provides the version and release date of the version being run
     *
     * @param event
     */
    @Override
    public void onSlashCommandCreate(SlashCommandCreateEvent event) {
        SlashCommandInteraction slashCommandInteraction = event.getSlashCommandInteraction();
        String commandName = slashCommandInteraction.getCommandName();

        if (commandName.equalsIgnoreCase("version")) {
            slashCommandInteraction.createImmediateResponder()
                    .addEmbed(VersionEmbed.getVersion())
                    .respond();
        }
    }
}
