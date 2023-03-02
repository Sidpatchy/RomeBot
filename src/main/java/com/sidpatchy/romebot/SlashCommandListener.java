package com.sidpatchy.romebot;

import com.sidpatchy.Robin.Discord.ParseCommands;
import com.sidpatchy.romebot.Embed.*;
import org.apache.logging.log4j.LogManager;
import org.apache.logging.log4j.Logger;
import org.javacord.api.entity.server.Server;
import org.javacord.api.entity.user.User;
import org.javacord.api.event.interaction.SlashCommandCreateEvent;
import org.javacord.api.interaction.SlashCommandInteraction;
import org.javacord.api.listener.interaction.SlashCommandCreateListener;

import java.io.FileNotFoundException;

// Eliminating the dumpster fire of having 20 individual listeners since 2022.
public class SlashCommandListener implements SlashCommandCreateListener {

    static ParseCommands parseCommands = new ParseCommands(Main.getCommandsFile());
    private static final Logger logger = LogManager.getLogger(Main.class);

    @Override
    public void onSlashCommandCreate(SlashCommandCreateEvent event) {
        SlashCommandInteraction slashCommandInteraction = event.getSlashCommandInteraction();
        Server server = slashCommandInteraction.getServer().orElse(null);
        String commandName = slashCommandInteraction.getCommandName();
        User author = slashCommandInteraction.getUser();
        User user = slashCommandInteraction.getArgumentUserValueByName("user").orElse(null);

        if (user == null) {
            user = author;
            logger.warn("Unable to get user value for command: " + commandName);
        }

        if (commandName.equalsIgnoreCase(parseCommands.getCommandName("assassinate"))) {
            slashCommandInteraction.createImmediateResponder()
                    .addEmbed(AssassinateEmbed.getAssassinate(user, author, server))
                    .respond();
        }
        else if (commandName.equalsIgnoreCase(parseCommands.getCommandName("birthday"))) {
            slashCommandInteraction.createImmediateResponder()
                    .addEmbed(BirthdayEmbed.getBirthday())
                    .respond();
        }
        else if (commandName.equalsIgnoreCase(parseCommands.getCommandName("carthago-delanda-est"))) {
            slashCommandInteraction.createImmediateResponder()
                    .addEmbed(CarthagoDelandaEstEmbed.getCarthago())
                    .respond();
        }
        else if (commandName.equalsIgnoreCase(parseCommands.getCommandName("crucify"))) {
            slashCommandInteraction.createImmediateResponder()
                    .addEmbed(CrucifyEmbed.getCrucify(user, author, server))
                    .respond();
        }
        else if (commandName.equalsIgnoreCase(parseCommands.getCommandName("enslave"))) {
            slashCommandInteraction.createImmediateResponder()
                    .addEmbed(EnslaveEmbed.getEnslave(user, author, server))
                    .respond();
        }
        else if (commandName.equalsIgnoreCase(parseCommands.getCommandName("help"))) {
            String command = slashCommandInteraction.getArgumentStringValueByName("command-name").orElse("help");
            try {
                slashCommandInteraction.createImmediateResponder()
                        .addEmbed(HelpEmbed.getHelp(command))
                        .respond();
            } catch (FileNotFoundException e) {
                e.printStackTrace();
                logger.error("Unable to read commands.yml file. Put simply, this is bad.");
            }
        }
        else if (commandName.equalsIgnoreCase(parseCommands.getCommandName("impale"))) {
            slashCommandInteraction.createImmediateResponder()
                    .addEmbed(ImpaleEmbed.getImpaled(user, author, server))
                    .respond();
        }
        else if (commandName.equalsIgnoreCase(parseCommands.getCommandName("info"))) {
            slashCommandInteraction.createImmediateResponder()
                    .addEmbed(InfoEmbed.getInfo(event.getApi()))
                    .respond();
        }
        else if (commandName.equalsIgnoreCase(parseCommands.getCommandName("joined"))) {
            slashCommandInteraction.createImmediateResponder()
                    .addEmbed(JoinedEmbed.getJoined(user, author, server))
                    .respond();
        }
        else if (commandName.equalsIgnoreCase(parseCommands.getCommandName("jupiterhates"))) {
            slashCommandInteraction.createImmediateResponder()
                    .addEmbed(JupiterHatesEmbed.getJupiterHates(user, author, server))
                    .respond();
        }
        else if (commandName.equalsIgnoreCase(parseCommands.getCommandName("sack"))) {
            slashCommandInteraction.createImmediateResponder()
                    .addEmbed(SackEmbed.getSacked(user, author, server))
                    .respond();
        }
        else if (commandName.equalsIgnoreCase(parseCommands.getCommandName("stab"))) {
            slashCommandInteraction.createImmediateResponder()
                    .addEmbed(StabEmbed.getStabbed(user, author, server))
                    .respond();
        }
    }
}
