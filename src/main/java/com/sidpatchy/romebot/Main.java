package com.sidpatchy.romebot;

import com.sidpatchy.Robin.Discord.ParseCommands;
import com.sidpatchy.Robin.File.ResourceLoader;
import com.sidpatchy.Robin.File.RobinConfiguration;
import org.apache.logging.log4j.LogManager;
import org.apache.logging.log4j.Logger;
import org.javacord.api.DiscordApi;
import org.javacord.api.DiscordApiBuilder;

import java.awt.*;
import java.io.FileNotFoundException;
import java.io.IOException;
import java.util.Arrays;
import java.util.Collection;
import java.util.List;
import java.util.stream.Collectors;
import java.util.stream.Stream;

/**
 * RomeBot - The only discord bot dedicated to the Roman Republic (and Empire)
 * Copyright (C) 2018-2022  Sidpatchy
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with this program.  If not, see <https://www.gnu.org/licenses/>.
 *
 * @since November 2018
 * @version 3.0.0
 * @author Sidpatchy
 */
public class Main {

    private static final Logger logger = LogManager.getLogger(Main.class);

    private static DiscordApi api;

    private static final long startMillis = System.currentTimeMillis();

    // related to file handling
    private static String configFile = "config.yml";
    private static String commandsFile = "commands.yml";
    static ParseCommands parseCommands;
    private static RobinConfiguration config;

    // Related to config options
    private static String token;
    private static String colour;
    private static Integer current_shard;
    private static Integer total_shards;
    private static String video_url;

    private static List<String> informationalCommandList = Arrays.asList("info", "joined"); // intentionally excludes help
    private static List<String> regularCommandsList = Arrays.asList("assassinate", "birthday", "carthago-delanda-est", "crucify", "enslave", "impale", "jupiterhates", "sack", "stab");
    public static void main(String[] args) throws IOException {
        logger.info("RomeBot loading...");

        // Load config file if it doesn't exist
        ResourceLoader loader = new ResourceLoader();
        loader.saveResource(configFile, false);
        loader.saveResource(commandsFile, false);

        // Init config handlers
        config = new RobinConfiguration("config/" + configFile);
        parseCommands = new ParseCommands("config/" + commandsFile);

        // Read data from config file
        token = config.getString("token");
        colour = config.getString("colour");
        current_shard = config.getInt("current_shard");
        total_shards = config.getInt("total_shards");
        video_url = config.getString("video_url");

        api = DiscordLogin(token, current_shard, total_shards);

        if (api == null) {
            System.exit(0);
        }
        else {
            logger.info("Successfully logged in to Discord on shard " + current_shard + " with a total shard count of " + total_shards);
        }

        // Set the bot's status
        api.updateActivity("/help | Salting Carthage!", video_url);

        // Register slash commands
        registerSlashCommands();

        // Register slash command listeners
        api.addSlashCommandCreateListener(new SlashCommandListener());
    }

    private static DiscordApi DiscordLogin(String token, Integer current_shard, Integer total_shards) {
        if (token == null || token.equals("")) {
            logger.error("Token can't be null or empty. Check your config file!");
            System.exit(1);
        }
        else if (current_shard == null || total_shards == null) {
            logger.fatal("Shard config is empty, check your config file!");
            System.exit(3);
        }

        try {
            // Connect to Discord
            logger.info("Attempting discord login");
            return new DiscordApiBuilder()
                    .setToken(token)
                    .setAllIntents()
                    .setCurrentShard(current_shard)
                    .setTotalShards(total_shards)
                    .login().join();
        }
        catch (Exception e) {
            e.printStackTrace();
            logger.fatal(e.toString());
            logger.fatal("Unable to log in to Discord. Aborting startup!");
        }
        return null;
    }

    public static void registerSlashCommands() throws FileNotFoundException {
        try {
            RegisterSlashCommands.RegisterSlashCommand(api);
            logger.info("Slash commands registered successfully!");
        }
        catch (NullPointerException e) {
            e.printStackTrace();
            logger.fatal(e.toString());
            logger.fatal("There was an error while registering slash commands. There's a pretty good chance it's related to an uncaught issue with the commands.yml file, trying to read all commands and printing out results.");
            for (String s : getCommandsList()) {
                logger.fatal(parseCommands.getCommandName(s));
            }
            logger.fatal("If the above list looks incomplete or generates another error, check your commands.yml file!");
            System.exit(4);
        }
        catch (Exception e) {
            logger.fatal(e.toString());
            logger.fatal("There was an error while registering slash commands.");
            System.exit(5);
        }
    }

    public void migrateOldConfigFile() {
        // future me, you're going to need to migrate everything to Robin v1.1.1 or later.
    }

    public static void migrateOldLangFile() {

    }

    public static long getStartMillis() { return startMillis; }
    public static String getConfigFile() { return configFile; }
    public static String getCommandsFile() { return commandsFile; }
    public static List<String> getCommandsList() {
        return Stream.of(informationalCommandList, regularCommandsList)
                .flatMap(Collection::stream)
                .collect(Collectors.toList());
    }
    public static List<String> getInformationalCommandList() { return  informationalCommandList; }
    public static List<String> getRegularCommandsList() { return regularCommandsList; }
    public static Color getColour() { return  Color.decode(colour); }
}