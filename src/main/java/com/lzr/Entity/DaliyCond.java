package com.lzr.Entity;

public class DaliyCond {
    private String name;
    private int value;

    public DaliyCond(String name, int value) {
        this.name = name;
        this.value = value;
    }

    @Override
    public String toString() {
        return "provinceDaliyCond{" +
                "name='" + name + '\'' +
                ", value=" + value +
                '}';
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public int getValue() {
        return value;
    }

    public void setValue(int value) {
        this.value = value;
    }
}
