package com.sidpatchy.romebot.SlashCommand;

import com.sidpatchy.romebot.Embed.AssassinateEmbed;
import org.javacord.api.entity.server.Server;
import org.javacord.api.entity.user.User;
import org.javacord.api.event.interaction.SlashCommandCreateEvent;
import org.javacord.api.interaction.SlashCommandInteraction;
import org.javacord.api.listener.interaction.SlashCommandCreateListener;

import java.util.Objects;

public class Assassinate implements SlashCommandCreateListener {

    /**
     * Has a mentioned user assassinated
     *
     * @param event
     */
    @Override
    public void onSlashCommandCreate(SlashCommandCreateEvent event) {
        SlashCommandInteraction slashCommandInteraction = event.getSlashCommandInteraction();
        Server server = slashCommandInteraction.getServer().orElse(null);
        String commandName = slashCommandInteraction.getCommandName();

        if (commandName.equalsIgnoreCase("assassinate")) {
            User user = (Objects.requireNonNull(slashCommandInteraction.requestFirstOptionUserValue().orElse(null))).getNow(slashCommandInteraction.getUser());
            if (user == null) {user = slashCommandInteraction.getUser();}
            slashCommandInteraction.createImmediateResponder()
                    .addEmbed(AssassinateEmbed.getAssassinate(user, server))
                    .respond();
        }
    }
}
