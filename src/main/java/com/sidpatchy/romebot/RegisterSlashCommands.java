package com.sidpatchy.romebot;

import com.sidpatchy.Discord.ParseCommands;
import org.javacord.api.DiscordApi;
import org.javacord.api.interaction.*;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class RegisterSlashCommands {

    static ParseCommands parseCommands = new ParseCommands(Main.getCommandsFile());

    public static void DeleteSlashCommands (DiscordApi api) {
        api.bulkOverwriteGlobalApplicationCommands(List.of()).join();
    }

    /**
     * Function to register slash commands
     *
     * @param api pass API into function
     */
    public static void RegisterSlashCommand(DiscordApi api) {
        ArrayList<SlashCommandOptionChoice> helpCommandOptions = new ArrayList<>();
        for (String s : Main.getCommandsList()) {
            helpCommandOptions.add(SlashCommandOptionChoice.create(parseCommands.getCommandName(s), parseCommands.getCommandName(s)));
        }

        api.bulkOverwriteGlobalApplicationCommands(Arrays.asList(
                // Informational commands
                new SlashCommandBuilder().setName(parseCommands.getCommandName("info")).setDescription(parseCommands.getCommandHelp("info")),
                new SlashCommandBuilder().setName(parseCommands.getCommandName("help")).setDescription(parseCommands.getCommandHelp("help"))
                        .addOption(SlashCommandOption.createWithChoices(SlashCommandOptionType.STRING, "command-name", "Command to get more info on", false, helpCommandOptions)),
                new SlashCommandBuilder().setName(parseCommands.getCommandName("joined")).setDescription(parseCommands.getCommandHelp("joined")).addOption(SlashCommandOption.create(SlashCommandOptionType.USER, "user", "Optionally mention a user")),

                // Regular commands
                new SlashCommandBuilder().setName(parseCommands.getCommandName("assassinate")).setDescription(parseCommands.getCommandHelp("assassinate")).addOption(SlashCommandOption.create(SlashCommandOptionType.USER, "user", "Optionally mention a user")),
                new SlashCommandBuilder().setName(parseCommands.getCommandName("crucify")).setDescription(parseCommands.getCommandHelp("crucify")).addOption(SlashCommandOption.create(SlashCommandOptionType.USER, "user", "Optionally mention a user")),
                new SlashCommandBuilder().setName(parseCommands.getCommandName("carthago-delanda-est")).setDescription(parseCommands.getCommandHelp("carthago-delanda-est")),
                new SlashCommandBuilder().setName(parseCommands.getCommandName("impale")).setDescription(parseCommands.getCommandHelp("impale")).addOption(SlashCommandOption.create(SlashCommandOptionType.USER, "user", "Optionally mention a user")),
                new SlashCommandBuilder().setName(parseCommands.getCommandName("stab")).setDescription(parseCommands.getCommandHelp("stab")).addOption(SlashCommandOption.create(SlashCommandOptionType.USER, "user", "Optionally mention a user")),
                new SlashCommandBuilder().setName(parseCommands.getCommandName("enslave")).setDescription(parseCommands.getCommandHelp("enslave")).addOption(SlashCommandOption.create(SlashCommandOptionType.USER, "user", "Optionally mention a user")),
                new SlashCommandBuilder().setName(parseCommands.getCommandName("sack")).setDescription(parseCommands.getCommandHelp("sack")).addOption(SlashCommandOption.create(SlashCommandOptionType.USER, "user", "Optionally mention a user")),
                new SlashCommandBuilder().setName(parseCommands.getCommandName("jupiterhates")).setDescription(parseCommands.getCommandHelp("jupiterhates")).addOption(SlashCommandOption.create(SlashCommandOptionType.USER, "user", "Optionally mention a user")),
                new SlashCommandBuilder().setName(parseCommands.getCommandName("birthday")).setDescription(parseCommands.getCommandHelp("birthday"))
        )).join();
    }
}
