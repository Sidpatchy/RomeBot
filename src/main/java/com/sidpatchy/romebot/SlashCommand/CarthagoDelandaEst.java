package com.sidpatchy.romebot.SlashCommand;

import com.sidpatchy.romebot.Embed.CarthagoDelandaEstEmbed;
import org.javacord.api.event.interaction.SlashCommandCreateEvent;
import org.javacord.api.interaction.SlashCommandInteraction;
import org.javacord.api.listener.interaction.SlashCommandCreateListener;

public class CarthagoDelandaEst implements SlashCommandCreateListener {

    /**
     * Command to salt Carthage
     *
     * @param event
     */
    @Override
    public void onSlashCommandCreate(SlashCommandCreateEvent event) {
        SlashCommandInteraction slashCommandInteraction = event.getSlashCommandInteraction();
        String commandName = slashCommandInteraction.getCommandName();

        if (commandName.equalsIgnoreCase("carthago-delanda-est")) {
            slashCommandInteraction.createImmediateResponder()
                    .addEmbed(CarthagoDelandaEstEmbed.getCarthago())
                    .respond();
        }
    }
}
