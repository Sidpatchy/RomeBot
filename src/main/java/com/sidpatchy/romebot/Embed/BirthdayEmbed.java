package com.sidpatchy.romebot.Embed;

import org.javacord.api.entity.message.embed.EmbedBuilder;

import java.awt.*;
import java.time.*;


public class BirthdayEmbed {
    public static EmbedBuilder getBirthday() {
        Instant birthday = Instant.parse(LocalDate.now().getYear() + "-07-12T12:00:00.00Z");
        if (! birthday.isAfter(Instant.now())) {
            int year = ZonedDateTime.now(ZoneId.of("UTC")).getYear() + 1;
            birthday = Instant.parse(year + "-07-12T12:00:00.00Z");
        }
        return new EmbedBuilder()
                .setColor(Color.decode("#e74d3c"))
                .setDescription("Caesar's party will be <t:" + getEpochDiff(birthday) + ":R>");
    }

    /**
     * Get a diff between two dates
     * @param instant the newest date
     * @return the diff value, in the provided unit
     */
    static long getEpochDiff(Instant instant) {
        LocalTime time = LocalTime.parse("00:00:00");
        ZoneOffset zone = ZoneOffset.of("Z");
        Duration diff = Duration.between(Instant.now(), instant);
        long epochDiff = diff.toSeconds();
        return Instant.now().getEpochSecond() + epochDiff;
    }
}
