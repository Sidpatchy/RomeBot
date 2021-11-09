package com.sidpatchy.romebot.SlashCommand;

import com.sidpatchy.romebot.Embed.BirthdayEmbed;
import org.javacord.api.event.interaction.SlashCommandCreateEvent;
import org.javacord.api.interaction.SlashCommandInteraction;
import org.javacord.api.listener.interaction.SlashCommandCreateListener;

public class Birthday implements SlashCommandCreateListener {

    /**
     * Crucifies a mentioned user
     *
     * @param event
     */
    @Override
    public void onSlashCommandCreate(SlashCommandCreateEvent event) {
        SlashCommandInteraction slashCommandInteraction = event.getSlashCommandInteraction();
        String commandName = slashCommandInteraction.getCommandName();

        if (commandName.equalsIgnoreCase("birthday")) {
            slashCommandInteraction.createImmediateResponder()
                    .addEmbed(BirthdayEmbed.getBirthday())
                    .respond();
        }
    }
}
