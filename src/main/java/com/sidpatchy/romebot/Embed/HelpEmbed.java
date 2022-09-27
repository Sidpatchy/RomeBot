package com.sidpatchy.romebot.Embed;

import com.sidpatchy.Discord.ParseCommands;
import com.sidpatchy.romebot.Main;
import org.apache.logging.log4j.LogManager;
import org.apache.logging.log4j.Logger;
import org.javacord.api.entity.message.embed.EmbedBuilder;
import java.awt.*;
import java.io.FileNotFoundException;
import java.util.Arrays;
import java.util.HashMap;
import java.util.List;
import java.util.Locale;

public class HelpEmbed {

    static ParseCommands parseCommands = new ParseCommands(Main.getCommandsFile());
    private static final Logger logger = LogManager.getLogger(Main.class);
    public static EmbedBuilder getHelp(String commandName) throws FileNotFoundException {
        List<String> informationalCommandsList = Main.getInformationalCommandList();
        List<String> regularCommandsList = Main.getRegularCommandsList();

        // Create HashMaps for help command
        HashMap<String, HashMap<String, String>> allCommands = new HashMap<String, HashMap<String, String>>();
        HashMap<String, HashMap<String, String>> informationalCommands = new HashMap<String, HashMap<String, String>>();
        HashMap<String, HashMap<String, String>> regularCommands = new HashMap<String, HashMap<String, String>>();

        for (String s : informationalCommandsList) {
            informationalCommands.put(s, parseCommands.get(s));
        }
        for (String s : regularCommandsList) {
            regularCommands.put(s, parseCommands.get(s));
        }

        allCommands.putAll(informationalCommands);
        allCommands.putAll(regularCommands);

        // Commands list
        if (commandName.equalsIgnoreCase("help")) {
            StringBuilder info = new StringBuilder("```");
            for (String s : informationalCommandsList) {
                if (info.toString().equalsIgnoreCase("```")) {
                    info.append(parseCommands.getCommandName(s));
                } else {
                    info.append(", ")
                            .append(parseCommands.getCommandName(s));
                }
            }
            info.append("```");

            StringBuilder reg = new StringBuilder("```");
            for (String s : regularCommandsList) {
                if (reg.toString().equalsIgnoreCase("```")) {
                    reg.append(parseCommands.getCommandName(s));
                } else {
                    reg.append(", ")
                            .append(parseCommands.getCommandName(s));
                }
            }
            reg.append("```");

            return new EmbedBuilder()
                    .setColor(Main.getColour())
                    .addField("Informational", info.toString(), false)
                    .addField("Regular Commands", reg.toString(), false);
        }
        // Command details
        else {
            if (allCommands.get(commandName) == null) {
                logger.error("Unable to locate command \"" + commandName + "\" while building help command.");
                return new EmbedBuilder()
                        .setColor(Main.getColour())
                        .setAuthor("ERROR")
                        .setDescription("There was an error when processing that command. Please try again later.");
            } else {
                return new EmbedBuilder()
                        .setColor(Main.getColour())
                        .setAuthor(commandName.toUpperCase())
                        .setDescription(allCommands.get(commandName).get("help"))
                        .addField("Command", "Usage\n" + "```" + allCommands.get(commandName).get("usage") + "```");
            }
        }
    }
}
