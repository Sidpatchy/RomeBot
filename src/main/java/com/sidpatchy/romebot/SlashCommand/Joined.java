package com.sidpatchy.romebot.SlashCommand;

import com.sidpatchy.romebot.Embed.JoinedEmbed;
import org.javacord.api.entity.server.Server;
import org.javacord.api.entity.user.User;
import org.javacord.api.event.interaction.SlashCommandCreateEvent;
import org.javacord.api.interaction.SlashCommandInteraction;
import org.javacord.api.listener.interaction.SlashCommandCreateListener;

public class Joined implements SlashCommandCreateListener {

    /**
     * Provides the date a user joined the discord server
     *
     * @param event
     */
    @Override
    public void onSlashCommandCreate(SlashCommandCreateEvent event) {
        SlashCommandInteraction slashCommandInteraction = event.getSlashCommandInteraction();
        Server server = slashCommandInteraction.getServer().orElse(null);
        String commandName = slashCommandInteraction.getCommandName();
        User author = slashCommandInteraction.getUser();
        User user = slashCommandInteraction.getFirstOptionUserValue().orElse(null);

        if (commandName.equalsIgnoreCase("joined")) {
            slashCommandInteraction.createImmediateResponder()
                    .addEmbed(JoinedEmbed.getJoined(user, author, server))
                    .respond();
        }
    }
}
