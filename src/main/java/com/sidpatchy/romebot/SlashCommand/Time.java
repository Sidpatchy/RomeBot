package com.sidpatchy.romebot.SlashCommand;

import com.sidpatchy.romebot.Embed.InfoEmbed;
import com.sidpatchy.romebot.Embed.TimeEmbed;
import org.javacord.api.event.interaction.SlashCommandCreateEvent;
import org.javacord.api.interaction.SlashCommandInteraction;
import org.javacord.api.listener.interaction.SlashCommandCreateListener;

public class Time implements SlashCommandCreateListener {

    /**
     * Command which provides the current time
     *
     * @param event
     */
    @Override
    public void onSlashCommandCreate(SlashCommandCreateEvent event) {
        SlashCommandInteraction slashCommandInteraction = event.getSlashCommandInteraction();
        String commandName = slashCommandInteraction.getCommandName();

        if (commandName.equalsIgnoreCase("time")) {
            slashCommandInteraction.createImmediateResponder()
                    .addEmbed(TimeEmbed.getTime())
                    .respond();
        }
    }
}
