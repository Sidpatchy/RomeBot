package com.sidpatchy.romebot.File;

import org.yaml.snakeyaml.Yaml;

import java.io.File;
import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.InputStream;
import java.util.Map;

public class ReadConfig {

    Yaml yaml = new Yaml();

    public Map<String, Object> GetConfig(String file) throws FileNotFoundException {
        InputStream inputStream = new FileInputStream(new File("config/" + file));
        return yaml.load(inputStream);
    }

    public boolean getBool(String file, String parameter) throws FileNotFoundException {
        Map<String, Object> config = GetConfig(file);
        return (boolean) config.get(parameter);
    }

    public String getString(String file, String parameter) throws FileNotFoundException {
        Map<String, Object> config = GetConfig(file);
        return (String) config.get(parameter);
    }

    public Integer getInt(String file, String parameter) throws FileNotFoundException {
        Map<String, Object> config = GetConfig(file);
        return (Integer) config.get(parameter);
    }

    public Float getFloat(String file, String parameter) throws FileNotFoundException {
        Map<String, Object> config = GetConfig(file);
        return (Float) config.get(parameter);
    }

    public Object getObj(String file, String parameter) throws FileNotFoundException {
        Map<String, Object> config = GetConfig(file);
        return config.get(parameter);
    }
}
