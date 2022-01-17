package com.sidpatchy.romebot.SlashCommand;

import com.sidpatchy.romebot.Embed.CrucifyEmbed;
import org.javacord.api.entity.server.Server;
import org.javacord.api.entity.user.User;
import org.javacord.api.event.interaction.SlashCommandCreateEvent;
import org.javacord.api.interaction.SlashCommandInteraction;
import org.javacord.api.listener.interaction.SlashCommandCreateListener;

import java.util.Objects;

public class Crucify implements SlashCommandCreateListener {

    /**
     * Crucifies a mentioned user
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

        if (commandName.equalsIgnoreCase("crucify")) {
            if (user == null) {user = slashCommandInteraction.getUser();}
            slashCommandInteraction.createImmediateResponder()
                    .addEmbed(CrucifyEmbed.getCrucify(user, author, server))
                    .respond();
        }
    }
}
