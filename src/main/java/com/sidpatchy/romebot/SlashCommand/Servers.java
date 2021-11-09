package com.sidpatchy.romebot.SlashCommand;

import com.sidpatchy.romebot.Embed.ServersEmbed;
import com.sidpatchy.romebot.Embed.TimeEmbed;
import org.javacord.api.DiscordApi;
import org.javacord.api.event.interaction.SlashCommandCreateEvent;
import org.javacord.api.interaction.SlashCommandInteraction;
import org.javacord.api.listener.interaction.SlashCommandCreateListener;

public class Servers implements SlashCommandCreateListener {


    private final DiscordApi api;

    public Servers(DiscordApi api) {
        this.api = api;
    }


    /**
     * Gets the number of servers RomeBot is in
     *
     * @param event
     */
    @Override
    public void onSlashCommandCreate(SlashCommandCreateEvent event) {
        SlashCommandInteraction slashCommandInteraction = event.getSlashCommandInteraction();
        String commandName = slashCommandInteraction.getCommandName();

        if (commandName.equalsIgnoreCase("servers")) {
            slashCommandInteraction.createImmediateResponder()
                    .addEmbed(ServersEmbed.getServers(api))
                    .respond();
        }
    }
}