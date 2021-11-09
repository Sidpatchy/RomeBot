package com.sidpatchy.romebot.SlashCommand;

import com.sidpatchy.romebot.Embed.InfoEmbed;
import org.javacord.api.event.interaction.SlashCommandCreateEvent;
import org.javacord.api.interaction.SlashCommandInteraction;
import org.javacord.api.listener.interaction.SlashCommandCreateListener;

public class Info implements SlashCommandCreateListener {

    /**
     * Command to provide info about RomeBot
     *
     * @param event
     */
    @Override
    public void onSlashCommandCreate(SlashCommandCreateEvent event) {
        SlashCommandInteraction slashCommandInteraction = event.getSlashCommandInteraction();
        String commandName = slashCommandInteraction.getCommandName();

        if (commandName.equalsIgnoreCase("info")) {
            slashCommandInteraction.createImmediateResponder()
                    .addEmbed(InfoEmbed.getInfo())
                    .respond();
        }
    }
}
