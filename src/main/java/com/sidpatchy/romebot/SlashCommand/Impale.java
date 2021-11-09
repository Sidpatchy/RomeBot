package com.sidpatchy.romebot.SlashCommand;

import com.sidpatchy.romebot.Embed.CrucifyEmbed;
import com.sidpatchy.romebot.Embed.ImpaleEmbed;
import org.javacord.api.entity.server.Server;
import org.javacord.api.entity.user.User;
import org.javacord.api.event.interaction.SlashCommandCreateEvent;
import org.javacord.api.interaction.SlashCommandInteraction;
import org.javacord.api.listener.interaction.SlashCommandCreateListener;

import java.util.Objects;

public class Impale implements SlashCommandCreateListener {

    /**
     * Impales a mentioned user
     *
     * @param event
     */
    @Override
    public void onSlashCommandCreate(SlashCommandCreateEvent event) {
        SlashCommandInteraction slashCommandInteraction = event.getSlashCommandInteraction();
        Server server = slashCommandInteraction.getServer().orElse(null);
        String commandName = slashCommandInteraction.getCommandName();

        if (commandName.equalsIgnoreCase("impale")) {
            User user = (Objects.requireNonNull(slashCommandInteraction.requestFirstOptionUserValue().orElse(null))).getNow(slashCommandInteraction.getUser());
            if (user == null) {user = slashCommandInteraction.getUser();}
            slashCommandInteraction.createImmediateResponder()
                    .addEmbed(ImpaleEmbed.getImpaled(user, server))
                    .respond();
        }
    }
}
