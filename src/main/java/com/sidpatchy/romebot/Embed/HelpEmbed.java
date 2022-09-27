package com.sidpatchy.romebot.Embed;

import com.sidpatchy.romebot.Main;
import org.javacord.api.entity.message.embed.EmbedBuilder;
import java.awt.*;
import java.util.HashMap;
import java.util.Locale;

public class HelpEmbed {
    public static EmbedBuilder getHelp(String commandName) {

        // Create HashMaps for help command
        HashMap<String, String> informationalCommandUsage = new HashMap<String, String>() {{
            put("info", "/info");
            put("joined", "/joined <optional: @user>");
            put("servers", "/servers");
            put("time", "/time");
            put("uptime", "/uptime");
            put("version", "/version");
        }};
        HashMap<String, String> informationalCommandHelp = new HashMap<String, String>() {{
            put("info", "Get support, an invite link, and a link to RomeBot's GitHub");
            put("joined", "Reports when a user joined the server");
            put("servers", "Reports how many servers RomeBot is in");
            put("time", "Returns the current time");
            put("uptime", "Reports how long the bot has gone without crashing (record: 125 days)");
            put("version", "Gives info on the current version of RomeBot");
        }};
        HashMap<String, String> regularCommandUsage = new HashMap<String, String>() {{
            put("assassinate", "/assassinate <optional: @user>");
            put("birthday", "/birthday");
            put("carthago-delanda-est", "/carthago-delanda-est");
            put("crucify", "/crucify <optional: @user>");
            put("enslave", "/enslave <optional: @user>");
            put("impale", "/impale <optional: @user>");
            put("jupiterhates", "/jupiterhates <optional: @user>");
            put("sack", "/sack <optional: @user>");
            put("stab", "/stab <optional: @user>");
        }};
        HashMap<String, String> regularCommandHelp = new HashMap<String, String>() {{
            put("assassinate", "Has a mentioned user assassinated");
            put("birthday", "Reports how much longer we must wait for Julius Caesar's birthday");
            put("carthago-delanda-est", "Based salting of Carthage");
            put("crucify", "Crucifies a mentioned user");
            put("enslave", "Enslaves a user for the glory of Rome!");
            put("impale", "Impales a mentioned user");
            put("jupiterhates", "Strikes down a mentioned user");
            put("sack", "Ponea cullei, punishment of the sack; Sacks a mentioned user.");
            put("stab", "Stabs a mentioned user");
        }};

        String commandType;
        try {
            informationalCommandHelp.get(commandName);
            commandType = "informational";
        } catch (Exception e) {
            commandType = "regular";
        }

        if (commandName.equalsIgnoreCase("help")) {
            return new EmbedBuilder()
                    .setColor(Color.decode("#e74d3c"))
                    .setAuthor("Help")
                    .addField("Informational Commands", "```/info, /joined, /servers, /time, /uptime, /version```")
                    .addField("Regular Commands", "```/assassinate, /birthday/ carthago-delanda-est, /crucify, /enslave, /impale, /jupiterhates, /sack, /stab```");
        } else {
            String usage = null;
            String help = null;
            if (commandType.equals("informational")) {
                usage = informationalCommandUsage.get(commandName);
                help = informationalCommandHelp.get(commandName);
            } else {
                usage = regularCommandUsage.get(commandName);
                help = regularCommandHelp.get(commandName);
            }
            return new EmbedBuilder()
                    .setColor(Main.getColour())
                    .addField(commandName.toUpperCase(Locale.ROOT), help)
                    .addField("USAGE", "```" + usage + "```");
        }
    }
}
