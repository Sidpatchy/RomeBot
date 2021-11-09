package com.sidpatchy.romebot;

import com.sidpatchy.romebot.File.ReadConfig;
import com.sidpatchy.romebot.File.ResourceLoader;
import com.sidpatchy.romebot.SlashCommand.*;
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

    public static void main(String[] args) throws IOException {
        // Load config file if it doesn't exist
        String configFile = "config.yml";
        ResourceLoader loader = new ResourceLoader();
        loader.saveResource(configFile, false);

        // Read data from config file
        ReadConfig config = new ReadConfig();
        String token = config.getString(configFile, "token");

        // Connect to Discord
        DiscordApi api = new DiscordApiBuilder()
                .setToken(token)
                .setAllIntents()
                .login().join();

        // Set the bot's status
        api.updateActivity("RomeBot v3.0-a.2", config.getString(configFile, "video_url"));

        // Register slash commands
        RegisterSlashCommands.RegisterSlashCommand(api);

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
}
