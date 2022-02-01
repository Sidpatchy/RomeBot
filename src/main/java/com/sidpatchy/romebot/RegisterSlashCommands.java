package com.sidpatchy.romebot;

import org.javacord.api.DiscordApi;
import org.javacord.api.interaction.*;

import java.util.Arrays;
import java.util.List;

public class RegisterSlashCommands {

    public static void DeleteSlashCommands (DiscordApi api) {
        api.bulkOverwriteGlobalApplicationCommands(List.of()).join();
    }

    /**
     * Function to register slash commands
     *
     * @param api pass API into function
     */
    public static void RegisterSlashCommand(DiscordApi api) {
        api.bulkOverwriteGlobalApplicationCommands(Arrays.asList(
                // Information commands
                new SlashCommandBuilder().setName("info").setDescription("Get to know more about RomeBot"),
                new SlashCommandBuilder().setName("help").setDescription("Help command").addOption(SlashCommandOption.createWithChoices(SlashCommandOptionType.STRING, "command-name", "Command to get more info on", false,
                        Arrays.asList(
                                SlashCommandOptionChoice.create("info", "info"),
                                SlashCommandOptionChoice.create("joined", "joined"),
                                SlashCommandOptionChoice.create("servers", "servers"),
                                SlashCommandOptionChoice.create("time", "time"),
                                SlashCommandOptionChoice.create("uptime", "uptime"),
                                SlashCommandOptionChoice.create("version", "version"),
                                SlashCommandOptionChoice.create("assassinate", "assassinate"),
                                SlashCommandOptionChoice.create("birthday", "birthday"),
                                SlashCommandOptionChoice.create("carthago-delanda-est", "carthago-delanda-est"),
                                SlashCommandOptionChoice.create("crucify", "crucify"),
                                SlashCommandOptionChoice.create("enslave", "enslave"),
                                SlashCommandOptionChoice.create("impale", "impale"),
                                SlashCommandOptionChoice.create("jupiterhates", "jupiterhates"),
                                SlashCommandOptionChoice.create("sack", "sack"),
                                SlashCommandOptionChoice.create("stab", "stab")
                        ))),
                new SlashCommandBuilder().setName("joined").setDescription("Get a user's join date").addOption(SlashCommandOption.create(SlashCommandOptionType.USER, "user", "Optionally mention a user")),
                new SlashCommandBuilder().setName("version").setDescription("Get RomeBot's version info"),
                new SlashCommandBuilder().setName("time").setDescription("Get the current time"),
                new SlashCommandBuilder().setName("servers").setDescription("Reports the number of servers the bot is in"),

                // Regular commands
                new SlashCommandBuilder().setName("assassinate").setDescription("Have a user assassinated").addOption(SlashCommandOption.create(SlashCommandOptionType.USER, "user", "Optionally mention a user")),
                new SlashCommandBuilder().setName("crucify").setDescription("Crucify a user").addOption(SlashCommandOption.create(SlashCommandOptionType.USER, "user", "Optionally mention a user")),
                new SlashCommandBuilder().setName("carthago-delanda-est").setDescription("Salt Carthage"),
                new SlashCommandBuilder().setName("impale").setDescription("Impale a user").addOption(SlashCommandOption.create(SlashCommandOptionType.USER, "user", "Optionally mention a user")),
                new SlashCommandBuilder().setName("stab").setDescription("Stab a user").addOption(SlashCommandOption.create(SlashCommandOptionType.USER, "user", "Optionally mention a user")),
                new SlashCommandBuilder().setName("uptime").setDescription("How long the bot has gone since crashing"),
                new SlashCommandBuilder().setName("enslave").setDescription("Enslave a user").addOption(SlashCommandOption.create(SlashCommandOptionType.USER, "user", "Optionally mention a user")),
                new SlashCommandBuilder().setName("sack").setDescription("Sack a user").addOption(SlashCommandOption.create(SlashCommandOptionType.USER, "user", "Optionally mention a user")),
                new SlashCommandBuilder().setName("jupiterhates").setDescription("Smites a user").addOption(SlashCommandOption.create(SlashCommandOptionType.USER, "user", "Optionally mention a user")),
                new SlashCommandBuilder().setName("birthday").setDescription("Reports how long it is until Julius Caesar's birthday")
        )).join();
    }
}
