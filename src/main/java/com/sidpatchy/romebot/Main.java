package com.sidpatchy.romebot;

import com.sidpatchy.romebot.File.ReadConfig;
import com.sidpatchy.romebot.File.ResourceLoader;
import com.sidpatchy.romebot.SlashCommand.*;
import org.apache.logging.log4j.LogManager;
import org.apache.logging.log4j.Logger;
import org.javacord.api.DiscordApi;
import org.javacord.api.DiscordApiBuilder;

import java.io.IOException;

/**
 * RomeBot - The only discord bot dedicated to the Roman Republic (and Empire)
 * Copyright (C) 2021  Sidpatchy
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
 * @version 3.0
 * @author Sidpatchy
 */
public class Main {

    private static final Logger logger = LogManager.getLogger(Main.class);

    public static void main(String[] args) throws IOException {
        logger.info("RomeBot loading...");

        // Load config file if it doesn't exist
        String configFile = "config.yml";
        ResourceLoader loader = new ResourceLoader();
        loader.saveResource(configFile, false);

        // Read data from config file
        ReadConfig config = new ReadConfig();
        String token = config.getString(configFile, "token");
        Integer current_shard = config.getInt(configFile, "current_shard");
        Integer total_shards = config.getInt(configFile, "total_shards");
        String video_url = config.getString(configFile, "video_url");

        DiscordApi api = DiscordLogin(token, current_shard, total_shards);

        if (api == null) {
            System.exit(0);
        }
        else {
            logger.info("Successfully logged in to Discord on shard " + current_shard + " with a total shard count of " + total_shards);
        }

        // Set the bot's status
        api.updateActivity("RomeBot v3.0-a.3", video_url);

        // Register slash commands
        //RegisterSlashCommands.RegisterSlashCommand(api);

        // Register slash command listeners
        // Informational commands
        api.addSlashCommandCreateListener(new Info());
        api.addSlashCommandCreateListener(new Help());
        api.addSlashCommandCreateListener(new Joined());
        api.addSlashCommandCreateListener(new Version());
        api.addSlashCommandCreateListener(new Time());
        api.addSlashCommandCreateListener(new Servers(api));

        // Regular commands
        api.addSlashCommandCreateListener(new Assassinate());
        api.addSlashCommandCreateListener(new Birthday());
        api.addSlashCommandCreateListener(new Crucify());
        api.addSlashCommandCreateListener(new Impale());
        api.addSlashCommandCreateListener(new CarthagoDelandaEst());
    }

    static DiscordApi DiscordLogin(String token, Integer current_shard, Integer total_shards) {
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
            logger.fatal(e.toString());
            logger.fatal("Unable to log in to Discord. Aborting startup!");
        }
        return null;
    }
}