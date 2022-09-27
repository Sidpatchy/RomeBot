package com.sidpatchy.romebot;

import com.sidpatchy.romebot.Embed.*;
import org.apache.logging.log4j.LogManager;
import org.apache.logging.log4j.Logger;
import org.javacord.api.entity.server.Server;
import org.javacord.api.entity.user.User;
import org.javacord.api.event.interaction.SlashCommandCreateEvent;
import org.javacord.api.interaction.SlashCommandInteraction;
import org.javacord.api.listener.interaction.SlashCommandCreateListener;

// Eliminating the dumpster fire of having 20 individual listeners since 2022.
public class SlashCommandListener implements SlashCommandCreateListener {

    private static final Logger logger = LogManager.getLogger(Main.class);

    @Override
    public void onSlashCommandCreate(SlashCommandCreateEvent event) {
        SlashCommandInteraction slashCommandInteraction = event.getSlashCommandInteraction();
        Server server = slashCommandInteraction.getServer().orElse(null);
        String commandName = slashCommandInteraction.getCommandName();
        User author = slashCommandInteraction.getUser();
        User user = slashCommandInteraction.getOptionUserValueByName("user").orElse(null);

        if (user == null) {
            user = author;
            logger.warn("Unable to get user value for command: " + commandName);
        }

        switch (commandName) {
            case "assassinate":
                slashCommandInteraction.createImmediateResponder()
                        .addEmbed(AssassinateEmbed.getAssassinate(user, author, server))
                        .respond();
            case "birthday":
                slashCommandInteraction.createImmediateResponder()
                        .addEmbed(BirthdayEmbed.getBirthday())
                        .respond();
            case "carthago-delanda-est":
                slashCommandInteraction.createImmediateResponder()
                        .addEmbed(CarthagoDelandaEstEmbed.getCarthago())
                        .respond();
            case "crucify":
                slashCommandInteraction.createImmediateResponder()
                        .addEmbed(CrucifyEmbed.getCrucify(user, author, server))
                        .respond();
            case "enslave":
                slashCommandInteraction.createImmediateResponder()
                        .addEmbed(EnslaveEmbed.getEnslave(user, author, server))
                        .respond();
            case "help":
                String command = slashCommandInteraction.getOptionStringValueByName("command-name").orElse("help");
                slashCommandInteraction.createImmediateResponder()
                        .addEmbed(HelpEmbed.getHelp(command))
                        .respond();
            case "impale":
                slashCommandInteraction.createImmediateResponder()
                        .addEmbed(ImpaleEmbed.getImpaled(user, author, server))
                        .respond();
            case "info":
                slashCommandInteraction.createImmediateResponder()
                        .addEmbed(InfoEmbed.getInfo(event.getApi()))
                        .respond();
            case "joined":
                slashCommandInteraction.createImmediateResponder()
                        .addEmbed(JoinedEmbed.getJoined(user, author, server))
                        .respond();
        }
    }
}
